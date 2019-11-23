from flask import Flask,request,jsonify,render_template#导入包，固定写法，flask是一个框架，可以灵活的添加相应功能
from dier import Db

db = Db("localhost","root","","testdb")#链接数据库
app = Flask(__name__)#启动文件，固定写法



@app.route("/")#@为装饰器
def index():
    return "首页"
@app.route("/regist",methods=["post","get"])
def regist():
    resdata = {}
    if request.method == "POST":
        userinfo = request.get_json()
        username = userinfo.get("username")
        password = userinfo.get("password")
        res = db.query("select * from t_user where username='{}';".format(username))
        if len(res) ==0:
            res = db.commit("insert into t_user (username,password) values ('{}','{}');".format(username,password))
            resdata["msg"] = res
        else:
            msg = "账号已存在"
            resdata["msg"] = msg
        return jsonify(resdata)
    else:
        return "1"
if __name__=="__main__":#固定
    app.run(host='0.0.0.0')#让程序运行起来