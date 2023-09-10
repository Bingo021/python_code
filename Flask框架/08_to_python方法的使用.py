from flask import Flask
from werkzeug.routing import BaseConverter

app = Flask(__name__)

#需求：路径参数传递多信息并以一个参数形式接收
#比如：获取姓名：zs年龄18的信息
#/user/zs+18

class LiConverter(BaseConverter):
    def to_python(self, value: str):
        return value.split('+')

app.url_map.converters['li'] = LiConverter

@app.route('/')
def index():
    return "Hello"

@app.route('/user/<info>')
def user(info):
    args = info.split('+')
    #sql :select * from t_user where uname = args[0] and age = args[1];
    return f'获取了某某信息{args}'

@app.route('/user_info/<li:info>')
def user_info(info):
    #sql :select * from t_user where uname = args[0] and age = args[1];
    return f'获取了某某信息{info}'

if __name__ =="__main__":
    app.run(debug=True)