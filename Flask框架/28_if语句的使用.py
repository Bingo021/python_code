from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def index():
    uname = "sxt"
    return render_template('index28.html',uname=uname)

if __name__ =='__main__':
    app.run(debug=True)