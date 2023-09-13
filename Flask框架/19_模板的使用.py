from flask import Flask,render_template

app = Flask(__name__,template_folder='templates')

# 模板默认查找的目录是templates
# 如果想要修改模板的目录，可以设置template_folder参数
@app.route('/')
def index():
    return render_template('index19.html')

if __name__ == "__main__":
    app.run(debug=True)