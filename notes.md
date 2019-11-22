1. 数组的深度复制
example : 
words = ['cat', 'window', 'defenestrate']
new_wds = words[:]
words is new_wds   # False

2. range序列
为了节省空间，python3的range并不生成真正的序列。
example :
range(10)    #result: range(0,10)
list(range(10))  #result : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]



