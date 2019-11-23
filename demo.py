from dier import Db

db = Db("localhost","root","","testdb")

username = input("请输入你的账号：")
res = db.query("select * from t_user where username = '{}';".format(username))
if len(res) != 0:
    print("{}账号已存在".format(username))
else:
    password = input("请输入密码：")
    password1 = input("请输入密码：")
    if password == password1:
        res = db.commit("insert into t_user (username,password) values ('{}','{}');".format(username,password))
        print(res)
    else:
        print("密码不一致")
#注册
