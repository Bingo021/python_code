from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return f"你好，少年"

app.config['JSON_AS_ASCII']=False
@app.route('/json1')
def r_json():
    return {'key':'python语言'}

@app.route('/json2')
def r_json2():
    return jsonify({'key':'python语言'})

@app.route('/tuple')
def r_tuple():
    # return "tuple",202
    # return 'tuple',{'itbaizan':'python'}
    # return 'tuple',300,{'itbaizan':'python'}
    return 'tuple',300,[('itbaizan','python_sql')]

if __name__=="__main__":
    app.run(debug=True)