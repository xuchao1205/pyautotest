'''print(233)

整数  233 int 
小数  3.33  float
字符串 "2333","hahah","汉子","#@%$#%"   str
布尔值 True=1 False=0   bool
空 None/NULL NoneType
元组  tuple
数组、列表   list
字典   dict
'''


'''a = int(input("请输入："))  # 这是用int方法，获取的字符串，转行成数字
b = input("请输入：")
print(int(a)+int(b))
print('777')
print('下面是减法')
c = int(input('减数'))
d = int(input('被减数'))
print(type(c-d))
print(c+d)
print(110)#为什么打的字符串输出后是整数，没有引号

什么
print(str(110))



a = (11,25,55,"222","haha",True,None,5,5,5)  # 元组,下标
b = [23,55,25,45,"drr","haha","哈哈"]  # 数组
c = {}  # 字典

print(a.index(5))
print(a.count(5))


b.append("新输入的数据")
print(b)

print(b[1])
print(a)
print(b.count(55))
print(a[1])

c = (11,22,33,"文字","元组",1,5,6,)
d = [99,"this",99,"什么",c]
print(d)
print(c[1])
print(c.count(22))
print(d[4])


d.append("111")  # 向数组的尾巴上插入数据。
d.insert(1,"插入的值")
print(d)
# d.clear() # 把整个数组清空
e =  d.copy() # 复制一个新的数组
d.extend([1,1,1,1,1])  # 将一个数组合并进去
f = d.pop(0)  # 将下标0的数据取走
d.reverse()  # 颠倒数组的顺序
'''

g = [1,1,1,1,1,[2,2,2,2,2],3,3,3]
print(g[1])
g.insert(1,9)
g.append("最后")
print(g)
print(g.pop(6))


zidian = {
    0:"hahah",
    "name":"zhangsan",
    2:"xixixi"
}  # key:value  键值对

# print(zidian.pop("name"))

print(zidian.get("name"))
# print(zidian["name"])
print("结果为",zidian[2],zidian)

#没有就添加
print(zidian.pop("name"))

