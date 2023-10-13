from flask import Flask,render_template

app = Flask(__name__)

@app.template_filter("cut")
def cut(value):
    value = value.replace('我是九，你是三，除了你，还是你','你不用多好，我喜欢就好')
    return value

@app.route('/')
def index():
    info = '=========== 我是九，你是三，除了你，还是你============'
    return render_template("index26.html",info= info)

if __name__ == "__main__":
    app.run(debug=True)