

##  open data space 数据共享空间

愿景:<br>
  数据联盟小平台，反国内外技术、数据垄断。<br>
  加密数据只对贡献成员开放。<br>
<br>




## 一、 有多少人工，才有多少智能，从0到1构建预训练大语言模型
    搜集开源数据收集、构造，清洗方法，包括预训练数据和指令数据<br>
        ChatGLM-6B 全套微调代码，经过两周对ChatGLM-6B的指令微调，两条经验如下：<br>
    1. glm-6B是经过SFT和RLHF后的版本,另外sft模板未开放，再次微调不够友好<br>
    2. 需要在一个干净的纯基座模型上进行微调（SFT），使用高质量的业务指令数据；RLHF，是一个难题，需要一个高质量的reward model，目前正确的rlhf pipeline比较稀少，训练出来好的效果也是一个挑战。<br>



## 二、 Open-data for LLMs 

 If you like the project, please show your support by leaving a star ⭐.

 | No. |                                            project                                             | description |  secret |
 |-----|:----------------------------------------------------------------------------------------------:|:-----------:|:-------:|
 | 1   |                 [悟道 - 200G](https://data.baai.ac.cn/details/WuDaoCorporaText)                  |             |    不需要秘钥    |
 | 2   |                         [Pile英文数据 - 1.3T的](https://pile.eleuther.ai/)                          |   需要强力清洗    |  不需要秘钥  |
 | 3    | [Tigerbot 中文开源预训练集 - 55G](https://huggingface.co/datasets/TigerResearch/pretrain_zh/tree/main) |             |  不需要秘钥  |

...

github 不经常更新， 更多数据参见 [数据分享](http://101.42.176.124:8080)

释放6个邀请码
```text
    68812a3a4d1c48e39626aeb47a3f4052KhKC0CLbNQv6KIAgm4i4d0Zj4XiGssLWrcA7TlvjwBg8vydB22S6XEbUwDEOfuFkHrQAilImXCQC5tgMU0TJ9eI9tdP2F3Ni
    7c07076a2ded4fa6aa16bc484b7192a3ZajgaQrTvbSjDegTCyKVg6iKd1hwwLM6onwxew386vCyUh8Ey1E9CsKQdkIv5vFLL6LTRX8bsV7lA9TZ4csbHDKecyVcllk5
    c8a340f435be43ac8e72f265764c987fnRXB9E7hiarIPOrEy3aC5lDzfjArBmjvQP7L3EfBvBnQj7fCpDn1wLKP8dq96sLBw6X5U7Hazkv4MUQ8w9BNqWfyEs5T9WTH
    2df70a0d62d542d8b8919fd63603dc33OMpvf0kOPSkOtRzl0jdv0NO3x5MGccGItIc3WRCLqWA7kWIOTUnkzqFfr3so8AtgpyI2UYlDbNp7H6nUtBNTcr4IwN2gGVe6
    5b461015581c4b46aa979060b899ea94eBumlAmhsA6ZfFMGuXax6L8tjFHGANOnVNTnuOvHuTUXF2HbkNc7jfJXWUMzcAwP8GWBPz2cqlzDL0N5L0Z6Vg2p3Jll1S3M
    67f806e9bd95467889acacc75ff1e3aaDLnjPYcI54tS1YACGQB3t1v5Qcfaua1PPCZQjCRID29XZaFHCTLCtSVXL9jQplzERxg0MBAJsdwESiwGZ6jAGTYAnV04FMXg
```

<br>
=======

## 四、数据质量6大标准

数据质量公认的六大评价标准为：完整性、有效性、及时性、一致性、准确性、唯一性。

数据质量六大评价标准

1、数据的准确性

数据的准确性是指数据与其描述的客观实体的特征是否一致，即数据采集值或者观测值和真实值之间的接近程度，也叫做误差值，误差越大，准确度越低。

2、数据的一致性

一致性是指存储在不同的系统中的同一个数据，是否存在差异或相互矛盾。例如航班始发站，在不同系统中记录的应该是同一个站点。

3、数据的唯一性

唯一性用于度量哪些数据是重复数据或者数据的哪些属性是重复的。例如一个人只能有唯一的身份证号码。

4、数据的规范性

规范指的是一项数据存在它特定的格式，规范性用于约束数据按统一标准存储。例如IP地址必定是由 4个0到255间的数字加上”.”组成的手机号码必定是13位的数字。

5、数据的及时性

数据的及时性是指数据从产生到可以查看的时间间隔，也叫数据的延时时长。就是数据能否在需要的时候得到保证。如果数据延时超出统计的要求，就可能导致分析得出的结论失去了意义。特别是业务覆盖多个市场、多个国家的大型企业，如果数据不能及时汇总，会影响到高层决策的及时程度。例如销售日报，用于要求每天统计T-1的销售数据，但是数据只能提供T-2，显然达不到用户的要求。

6、数据的完整性

数据的完整性是从数据采集到的程度来衡量的，是应采集和实际采集到数据之间的比例。指的是数据信息是否存在缺失的情况，数据缺失的情况可能是整个数据记载缺失，也可能是数据中某个字段信息的记载缺失。一个公司数据的完整性体现着这个公司对数据的重视程度。

## 五、数据清洗九大方法
   
清理数据的基础知识
```text
你并不一定始终可控制从数据库、文本文件或网页等外部数据源导入的数据格式和类型。 通常需要先清理数据，才能分析数据。 
```

拼写检查
```text
使用拼写检查不仅可查找拼写错误的单词，还可查找使用不一致的值（如产品或公司名称），只需将这些值添加到自定义词典即可。

```

删除重复行
```text
导入数据时，重复行是一个常见问题。 最好先筛选唯一值，确认结果是所需结果，然后再删除重复值。
```

查找和替换文本
```text
可能需要删除常见的前导字符串（例如后跟冒号和空格的标签）或后缀（例如已过时或不必要的字符串结尾处的附加说明短语）。 若要执行此操作，可查找文本的实例，然后将其替换为无文本或其他文本。
```
更改文本大小写
```text
有时文本格式混乱，尤其是文本大小写方面。 使用三种 Case 函数中的一种或多种，可将文本转换为小写字母（如电子邮件地址）、大写字母（如产品代码）或首字母大写（如姓名或书名）。
```
删除文本中的空格和非打印字符
```text
有时文本值包含前导空格、尾随空格或多个嵌入空格字符（Unicode 字符集值 32 和 160），或非打印字符（Unicode 字符集值 0 到 31、127、129、141、143、144 和 157）。 执行排序、筛选或搜索操作时，这些字符有时会导致意外结果。 例如，在外部数据源中，用户可能会无意添加额外的空格字符，从而导致打字错误，或者从外部源导入的文本数据可能包含嵌入在文本中的非打印字符。 由于这些字符不容易引起注意，因此意外结果可能很难理解。 若要删除这些不需要的字符，可组合使用 TRIM、CLEAN 和 SUBSTITUTE 函数。
```
修复数字和数字符号
```text
主要有两个数字问题可能需要你进行数据清理：无意中将数字导入为文本，以及需要根据你组织的标准更改负号。
```

修复日期和时间
```text
由于存在许多不同的日期格式，并且这些格式可能混杂有编号部件代码或其他包含斜杠标记或连字符的字符串，因此日期和时间通常需要进行转换和重新设置格式。
```

合并和拆分列
```text
从外部数据源导入数据后的常见任务是将两列或多列合并为一列，或将一列拆分为两列或多列。 例如，可能需要将包含全名的列拆分为名字和姓氏。 或者可能需要将包含地址字段的列拆分为单独的街道、城市、地区和邮政编码列。 反之亦可。 可能需要将名字和姓氏列合并为一个全名列，或者将单独的地址列合并为一列。 其他可能需要合并为一列或拆分为多列的常见值包括产品代码、文件路径和 Internet 协议 (IP) 地址。
```


## 欢迎加入
 QQ group 185144988