from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def index():
    # return render_template('index23.html',nick_name='吕布')
    # return render_template('index23.html')
    return render_template('index23.html', nick_name='')

if __name__=="__main__":
    app.run(debug=True)