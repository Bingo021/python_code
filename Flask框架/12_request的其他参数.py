from flask import Flask,request

app = Flask(__name__)

@app.route('/args',methods=['GET','POST'])
def args():
    url = request.url
    method = request.method
    headeers = request.headers.get('Content-Type')
    user_agent = request.headers.get('User-Agent')
    uid = request.cookies.get('uid')
    return f"Hello!==={url}==={method}=={headeers}=={user_agent}==={uid}"

if __name__ =="__main__":
    app.run(debug=True)