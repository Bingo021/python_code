from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index20.html')

@app.route('/index')
def index2():
    return render_template('index20.html',arg='Pyhton中的Flask',info='Flask模板传参')

@app.route('/home')
def home():
    context = {
        'uname':'吕布',
        'age':18,
        'height':180,
        'wu_qi':{'jin':'方天画戟','yuan':'弓箭'}
    }
    return render_template('index20.html',**context)

if __name__ == "__main__":
    app.run(debug=True)