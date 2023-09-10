from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    a = 1
    b = 0
    c = a/b
    return 'Hello123!!!'

#Debug的好处是：
#1.可以热加载，更新完代码后，不用手动重新启动服务，系统会自动给我们重启
#2.可以直接把错误信息加载到浏览器
if __name__ == "__main__":
    # app.run(debug=True)
    app.debug = True
    app.run()