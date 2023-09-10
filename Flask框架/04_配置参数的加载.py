import json

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'hello'

class Config:
    DEBUG = True

if __name__ == "__main__":
    # app.run()
    #方法1
    # app.config['DEBUG'] = True
    # app.config.update({'DEBUG':True})
    # app.run()
    #方式2
    # app.config.from_mapping({'DDEBUG':True})
    # app.run()
    #方式3
    # app.config.from_object(Config)
    # app.run()
    #方式4
    # app.config.from_file("config.json",json.load)
    # app.run()
    #方式5
    app.config.from_pyfile("setting.py")
    app.run()
