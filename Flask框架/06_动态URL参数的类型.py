from flask import Flask

app = Flask(__name__)

@app.route('/artical/<id>')
def index(id):
    print(f"/接收到的文章id是：{id}")
    print(type(id))
    return f"返回了{id}的文章"

@app.route('/int/<int:id>')
def index_int(id):
    print(f"/接收到的文章id是：{id}")
    print(type(id))
    return f"返回了{id}的文章"

@app.route('/float/<float:id>')
def index_float(id):
    print(f"/接收到的文章id是：{id}")
    print(type(id))
    return f"返回了{id}的文章"

@app.route('/string/<string:id>')
def index_string(id):
    print(f"/接收到的文章id是：{id}")
    print(type(id))
    return f"返回了{id}的文章"

@app.route('/path/<path:id>')
def index_path(id):
    print(f"/接收到的文章id是：{id}")
    print(type(id))
    return f"返回了{id}的文章"

@app.route('/uuid/<uuid:id>')
def index_uuid(id):
    print(f"/接收到的文章id是：{id}")
    print(type(id))
    return f"返回了{id}的文章"

@app.route('/<any(user,item):tmp>/<int:id>')
def index_any(tmp,id):
    if tmp == 'user':
        return f'返回了一个编号为{id}的用户信息'
    elif tmp =="user":
        return f"返回一个编号为{id}的元素信息"

if __name__ == "__main__":
    app.run(debug=True)