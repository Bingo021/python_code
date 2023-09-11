from flask import Flask,url_for

app = Flask(__name__)

@app.route('/index/')
def index():
    return f"Hello!"

@app.route('/show_url')
def show_url():
    url = url_for('index',next='/')
    return f"反向找到的url地址是：{url}"


if __name__=="__main__":
    app.run(debug=True)