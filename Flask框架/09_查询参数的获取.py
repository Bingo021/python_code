from flask import Flask,request

app = Flask(__name__)

# https://www.baidu.com/s?wd=python&rsv_spt=1&rsv_iqid=0xfde5d8d20010c29d&issp=1&f=8&rsv_bp=1&rsv_idx=2&ie=utf-8&tn=baiduhome_pg&rsv_dl=tb&rsv_enter=1&rsv_sug3=7&rsv_sug1=7&rsv_sug7=101&rsv_sug2=0&rsv_btype=i&prefixsug=python&rsp=6&inputT=2288&rsv_sug4=3172
@app.route('/')
def index():
    #方式1
    # uname = request.args.get('uname')
    # pwd = request.args.get('pwd')
    #方式2
    uname = request.values.get('uname')
    pwd = request.values.get('pwd')

    return f'Hello!==={uname}==={pwd}'

if __name__ == "__main__":
    app.run(debug=True)