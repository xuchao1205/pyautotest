"""for i in range(1,10):
    for j in range(1,i+1):
        print(i,"x",j,"=",i*j,end=" ")
    print()
    """
import pymysql #调用包
class Db:#这是类的固定写法，首字母必须是大写
    def __init__(self,host,user,password,db):#再给Db赋值
        self.host = host
        self.user = user
        self.password = password
        self.db = db
    def commit(self,sql):#封装方法，固定写法。
        db = pymysql.connect(host=self.host,user=self.user,password=self.password,db=self.db)#链接数据库
        cursor = db.cursor()#获取游标
        try:#异常捕获
            cursor.execute(sql)#执行括号里面的命令，让游标执行SQL语句
            db.commit()#应用代码，让SQL生效
            db.close()#关闭数据库
            return True#返回结果，给提示
        except Exception as e:#错误都是属于Exception里面的
            print(sql,e)
            return False


    def query(self,sql):
        """查询数据库的方法
        """
        db = pymysql.connect(host=self.host,user=self.user,password=self.password,db=self.db)
        cursor = db.cursor()
        try:
            cursor.execute(sql)
            res = cursor.fetchall()
            db.close()
            return res
        except Exception as e:
            print(sql,e)


# db = Db("localhost","root","","testdb")#类的初始化
# res = db.query("select * from t_banji;")#输入SQL语句，并赋值给res
# print(res)

# #类的继承。
# class Db2(Db):#此时Db已经继承了Db的属性。有了Db的功能
#     pass

# db=Db2("localhost","root","","testdb")
# res=db.query("show tables;")
# print(res)


