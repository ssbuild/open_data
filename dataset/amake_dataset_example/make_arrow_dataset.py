# -*- coding: utf-8 -*-
# @Time:  22:31
# @Author: tk
# @File：make_dataset
import json
import os

from fastdatasets.arrow.writer import PythonWriter
from fastdatasets.arrow.dataset import load_dataset,arrow
from fastdatasets import gfile



with_stream = True
schema = {
    'id': 'int32',
    'instruction': 'str',
    'input': 'str',
    'output': 'str',
    'file': 'str',
}


class DataWriter:
    def get_file_data(self,in_files):
        all_data = []
        for file in in_files:
            with open(file, mode='r', encoding='utf-8') as f:
                if os.path.basename(file).find('未完成') != -1:
                    continue
                jds = json.loads(f.read())
                all_data.append((os.path.basename(file), jds))
        return all_data

    def write(self,in_files,outfile):
        all_data = self.get_file_data(in_files)
        fs = PythonWriter(outfile,schema=schema,with_stream=with_stream,options=None)
        N = 1000
        for file, jds in all_data:
            batch = {k: [] for k in schema}
            for i, jd in enumerate(jds):
                batch["id"].append(i)
                batch["file"].append(file)

                for k, v in jd.items():
                    if k == 'history':
                        continue
                    batch[k].append(v)
                if 'input' not in jd:
                    batch['input'].append('')

                if len(batch["id"]) % N == 0:
                    status = fs.write_batch(batch.keys(), batch.values())
                    assert status.ok(), status.message()
                    for k, v in batch.items():
                        v.clear()
            if len(batch["id"]):
                status = fs.write_batch(batch.keys(), batch.values())
                assert status.ok(), status.message()
                for k, v in batch.items():
                    v.clear()
        fs.close()

    @staticmethod
    def read(file):
        dataset = load_dataset.RandomDataset(file,with_share_memory=not with_stream)
        print(file,'total', len(dataset))
        for i in range(len(dataset)):
            print(dataset[i])
            break




if __name__ == '__main__':

    base_dir = r'../alpaca_chinese_dataset'
    in_files = [
        (gfile.glob(os.path.join(base_dir,'原始英文数据/*.json')), os.path.join(base_dir,'english.arrow')),
        (gfile.glob(os.path.join(base_dir,'翻译后的中文数据/*.json')), os.path.join(base_dir,'chinese.arrow')),
        (gfile.glob(os.path.join(base_dir,'其他中文问题补充/*.json')), os.path.join(base_dir,'other_chinese.arrow')),
    ]
    for files,outfile in in_files:
        DataWriter().write(files,outfile)
        DataWriter.read(outfile)
