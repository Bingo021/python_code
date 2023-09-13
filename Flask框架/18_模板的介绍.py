from flask import Flask

app = Flask(__name__)

@app.route('/index/<int:id>')
def index(id):
    # select * from t_item where id = id
    # id name addr size
    return '<h1>Hello!!</h1><p style="color:red">这个是内容!!</p>{name}'

if __name__ == "__main__":
    app.run(debug=True)