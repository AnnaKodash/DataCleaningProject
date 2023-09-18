from flask import Flask,request, jsonify
import datetime

app = Flask(__name__)


@app.route('/')
def index():
    return 'Test message. The server is running'

@app.route('/hello')
def hello_func():
    name = request.args.get('name')
    return f'hello, {name}!'

@app.route('/time')
def current_time():
    now = datetime.datetime.now()
    time = {'time': now}
    return time


@app.route('/add', methods=['POST'])
def add():
    num = request.json.get('num')
    if num>10:
        return 'too much', 400
    return jsonify({'result':num+1})

if __name__ == '__main__':
    app.run('localhost', 5000)
    
