from dier import Db
db = Db("localhost","root","","testdb")
username = input("请输入用户名：")
res = db.query("select * from t_user where username='{}';".format(username))
if len(res) == 0:
    print("你输入的账号不存在")
else:
    password = input("请输入你的密码：")
    res1 = db.query("select t_user.password from t_user where username='{}';".format(username))
    if password == res1[0][0]:
        print("登录成功")
    else:
        print("你输入的密码错误")