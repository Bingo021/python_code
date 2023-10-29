from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    nick = '吕布'
    return render_template('index33.html',nick = nick)


if __name__ == '__main__':
    app.run(debug=True)