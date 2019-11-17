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
