#第二章 Python基础
1. 代码中修改不可变数据导致运行异常，抛出TypeError异常
example: 
x = (1,2,3); x[0]=5  
result:
TypeError: 'tuple' object does not support item assignment

2. a=1,b=2,不用中间变量交换a和b的值
方法一：
a = a + b
b = a - b
a = a - b
方法二：
a = a^b
b = b^a
a = a^b
方法三：
a,b=b,a

3. print调用Python底层的什么方法
sys.stdout.write(),即往控制台打印字符串，可以参考help(print)

4. 简述input()函数的理解
python3中，input()获取到的均是字符串类型
python2中，raw_input()与python3相同，input()输入什么类型，获取什么类型

5. zip函数功能	
将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，python2返回元组组成的列表(python3返回对象）
python3 example:
x=('a','b','c')
y=(1,2,3)
A0 = zip(x,y)
result:
print(A0)   <zip object at 0x1011b20f0>
list(A0)   [('a', 1), ('b', 2), ('c', 3)]

6. 4G内存怎么读区一个5G数据
方法一：通过生成器，分多次读取
def read_file(fpath):
  BLOCK_SIZE = 1024
  with open(fpath, 'rb') as f:
    while True:
      block = f.read(BLOCK_SIZE)
      if block:
        yield block
      else:
        return
方法二：通过split切割成小文件，然后再对数据进行处理(split -b 1024 file)

7.read, readline和readlines的区别
read读取整个文件，readline读区在一行，readlines读取整个文件到迭代器

8. 遍历文件夹
import os
def print_directory_content(sPath):
  for sChild in os.listdir(sPath):
    sChildPath = os.path.join(sPath,sChild)
    if os.path.isdir(sChildPath):
      print_directory_content(sChildPath)
    else:
      print(sChildPath)


