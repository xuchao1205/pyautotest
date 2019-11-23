
# age = int(input("请输入你的年龄："))
"""age = 10

if age > 30:
    if age > 50:
        print("zisuanmantang")
    else:
        print("家庭的辛酸啊")
elif age > 22:
    print("work")
elif age > 18:
    print("daxue")
elif age > 12:
    print("zongxue")
else:
    print("tongnian")


for i in range(1,10):
    for j in range(1,i+1):
        print(i,"X",j,"=",i*j,end="  ")
    print()

time = int(input("时间:"))

# a = int(input("自定义"))
if time> 10:
    print("吃饭")
else:
    print("不吃饭")
  

for i in range(1,10):
    for j in range(1,i+1):
        # print(i,"x",j,"=",i*j,end=" ")
        print(i,j,end="")
    print()

for i in range(1,10):
    for j in range(1,i+1):
        print(i,"x",j,"=",i*j,end=" ")
    print()
    

if 9==10:
    if 5!=6:
        print("cuowu")
    else:
        print("正确")
else:
        print("错误")


a = 1
while a < 10:
    print("哈哈哈")
    a = a + 1


a = [1,2,3,4,5,6,7,8,9]
i = 0
while i < len(a):
    print(a[i])
    i = i + 1




比如有一个数组[8778,878,56,67,997,26,8787,75,677,22,344,56,46,4343,3453,343]
以100为界限，拆分为2个数组

a=[8778,878,56,67,997,26,8787,75,677,22,344,56,46,4343,3453,343]
b=[]
c=[]
for i in a:
    if i>100:
        b.append(i)
    else:
        c.append(i)
print(b,c)

循环红黄蓝 黄3  红绿  连续30次  

a=["红","黄","绿"]
for i in a:
    if i=="黄":
        for j in range(3):
            print(i,3-j)
    else:
        for j in range(30):
            print(i,30-j)
      

a = input("账号：")
b = input("密码：")
if a=="lianxiang":
    if b=="123":
        print("成功")
    else:
        print("失败")
        
else:
    print("失败")
  

a = input("请输入账号：")
if a=="":
    print("请输入账号")
elif a=="zhangsan":
    print("账号已被占用")
else:
    print("此账号可用")
b = input("请输入密码：")
c = input("请确认密码：")
if b==c:
    print("密码验证通过")
else:
    print("两次输入的密码不一致")
d = {"zhangsan":123}
d[a]=int(b)
print(d)



def commit(sql):#封装方法，固定写法。
    db = pymysql.connect(host="localhost",user="root",password="",db="testdb")
    cursor = db.cursor()
username = input("请输入：")
if len(username)!=0 and commit("select 'username' from t_user;")==None:
    password = input("请输入密码：")
    password1 = input("请再次输入密码：")
    if password == password1:
        print("注册成功") 
        res=commit("insert into t_user (username,password) values ('{}','{}');".format(username,password))
        print(res)

    else:
         print("两次输入的密码不一致")
else:
    print("用户名不正确")

"""

from dier import Db
db = Db("localhost","root","","testdb")

while True:
    u = input("请输入用户名：")
    res = db.query("select * from t_user where username='{}';".format(u))
    if len(res) == 0:
        print("你输入的账户不存在")
    else:
        break



password = input("请输入你的密码：")
res1 = db.query("select t_user.password from t_user where username='{}';".format(u))
while password != res1[0][0]:
    password=input("你输入的密码错误，请重新输入：")

print("登录成功")

