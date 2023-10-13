from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    items = ['Python', 'HTML', 'CSS', 'JavaScript', 'SQL', 'Lua']
    person = {'uname':'张三','age':18,'height':180,'nick':'法外狂徒'}
    return render_template('index30.html', items=items,person=person)


if __name__ == '__main__':
    app.run(debug=True)
