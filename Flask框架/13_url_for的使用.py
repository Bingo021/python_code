from flask import Flask,url_for

app = Flask(__name__)

@app.route('/index')
def index():
    return f"Hello!"

@app.route('/home/<int:uid>')
def home(uid):
    return f"Hello!=={uid}"

@app.route('/show_url')
def show_url():
    # url = url_for('index')#第一个参数是函数的名字
    # url = url_for('home',uid=10001)#第二个参数默认匹配路径参数了
    url = url_for('home',uid=10001,addr='beijing')#第二个参数默认匹配路径参数了，匹配不上就会以查询参数进行传递
    return f'反向查找到的url地址：{url}'

if __name__=="__main__":
    app.run(debug=True)