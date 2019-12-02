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

9. 在except中，return后还会不会执行finally中的代码？怎么抛出自定义异常？
会继续处理finally中的代码；用raise方法可以抛出自定义的异常。

10. 介绍except的作用和用法。
except：捕获所有异常
except <异常名>: 捕获指定异常
except <异常名1，异常名2>: 捕获异常1或者异常2
except <异常名>,<参数>: 捕获指定异常，及其参数
except <异常名1，异常名2>:<参数>:捕获指定异常，及其附加数据

11. 常用的Python标准库
os、time、random、pymysql、threading、multiprocessing、queue
django、flask、requests、virtualenv、selenium、scrapy、xadmin、celery、re、hashlib、md5
Numpy、scipy、Pandas

12. 赋值、浅拷贝、深拷贝的区别
赋值操作不会开辟新的内存空间，它只是复制了对象的引用。
浅拷贝会创建新的对象，其内容非原对象本身的引用，而是对象内第一层对象的引用。包含三种形式：切片操作、工厂操作、copy模块中的copy函数。例如：
a = [1,2,3]
切片操作：b = a[:] 或者 b = [x for x in a]
工厂函数：b = list(a)
copy函数：b = copy.copy(a)
深拷贝：拷贝了对象中的所有元素，包含多层嵌套。

13. 拷贝的注意点
对于非容器类型，如数字、字符以及其他的原子类型，没有拷贝一说，产生的都是原对象的引用。如果元组变量值包含原子类型对象，即使采用了深拷贝，也只能得到浅拷贝。

14. __init__和__new__的区别
init在创建对象后，对对象进行初始化
new是新创建一个对象，并将该对象返回给init

15. Python如何生成随机数
import random
random.random():生成0-1之间的随机浮点数
random.uniform(a,b):生成[a,b]之间的浮点数
random.randint(a,b):生成[a,b]之间的整数
random.randrange(a,b,step):在指定的集合[a,b)中，以step为基数，随机取一个数
random.choice(sequence)：从特定序列中取一个元素

16. 判断一年中的第几天
import datetime
date1 = datetime.date(year=2019,month=1,day=1)
date2 = datetime.date(year=2019,month=10,day=1)
date1-date2

17. 打乱排序的list对象
import random
random.shuffle(alist)

18. os.path和sys.path代表什么
os.path是对系统文件路径的操作
sys.path是对python解释器的系统环境参数的操作（动态改变Python解释器的搜索路径）

19. os模块常见的方法
os.remove():删除文件
os.rename()：重命名文件
os.walk()：生成目录树下的所有文件名
os.chdir()：改变目录
os.mkdir/mkdirs：创建目录/多层目录
os.rmdir/removedirs：删除目录/多层目录
os.listdir：列出指定目录文件
os.getcwd:取得当前工作目录
os.chmod：改变目录权限
os.path.basename():去掉目录路径，返回文件名
os.path.dirname()：去掉文件名，返回目录路径
os.path.join():将分离的各部分组成路径名
os.path.split()：返回（dirname(),basename())元组
os.path.splitext():返回filename,extension元组
os.path.getatime\ctime\mtime：分别返回最近访问、创建、修改时间
os.path.getsize()：返回文件大小
os.path.exists():是否存在
os.path.isabs():是否为绝对路径
os.path.isdir():是否为目录
os.path.isfile()：是否为文件

