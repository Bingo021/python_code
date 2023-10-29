from flask import Flask, render_template

app = Flask(__name__,static_folder='static2')


@app.route('/')
def index():
    return render_template('index37.html')


if __name__ == '__main__':
    app.run(debug=True)