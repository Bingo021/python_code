#因为需要创建一个web应用，而flask中创建应用对象是Flask，因此引入此对象
from flask import Flask

#创建对象
app = Flask(__name__)

#路由的地址
@app.route('/index')
def index():
    #return 代表将数据返回给浏览器
    return '尚学堂——Python'

if __name__ ==  "__main__":
    #启动web应用服务
    # app.run()
    app.run(port=8000)