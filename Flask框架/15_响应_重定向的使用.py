from flask import Flask,redirect,url_for

app = Flask(__name__)

@app.route('/user_login/')
def login():
    return f"登录页面！！"

@app.route('/info')
def info():
    print("===========这个是个人信息=============")
    # return redirect('/login/',code=301)
    return redirect(url_for('login'))#重定向和url_for结合使用

if __name__=="__main__":
    app.run(debug=True)