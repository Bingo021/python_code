from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index21.html')

@app.route('/home/')
def home():
    return 'Home!!'

@app.route('/home1/<int:id>')
def home1(id):
    return 'Home!!'

if __name__ =='__main__':
    app.run(debug=True)