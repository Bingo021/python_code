from flask import Flask

app = Flask(__name__)

@app.route('/artical/details/<id>')
def index(id):
    print(f"接收到的文章ID是：{id}")
    #获取到id后，去数据库查询数据
    return f"返回了{id}的文章"

if __name__ == "__main__":
    app.run()