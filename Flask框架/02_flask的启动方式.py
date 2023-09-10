from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello!!!"

if __name__ =="__main__":
    app.run(host='0.0.0.0',port=8000)
#第一种通过app.run()运行
    #python filename
    #右键 ——run python file in terminal
#第二种通过flask命令行运行
    #可以不写app.run()
    #不要用中文