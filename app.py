from flask import Flask


app = Flask(__name__)

@app.route('/')
def index():
    return "hello root"

@app.route('/world')
def world():
    return "hello world"

@app.route('/town')
def world():
    return "hello town"

if __name__ == '__main__':
    app.run(debug=True)