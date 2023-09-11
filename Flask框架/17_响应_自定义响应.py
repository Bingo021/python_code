from flask import Flask,Response,make_response

app = Flask(__name__)

@app.route('/')
def index():
    # return Response('你好，少年！！',status=500,headers={'itbaizan':'python!!!'})
    # return Response('')
    return Response('无法找到页面',status=404)

@app.route('/home')
def home():
    resp = make_response('这个是创建的Response对象')
    resp.headers['itbaizan'] = 'SQL+Pyhton+Flask'
    resp.status = '404 NOT FOUND'
    return  resp

if __name__=="__main__":
    app.run(debug=True)