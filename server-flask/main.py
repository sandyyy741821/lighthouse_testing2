from flask import Flask
from flask-cors import CORS

app = Flask(__name__)
CORS(app) #enable CORS on all routes

@app.route('/')
def hello_world():
    return 'Hello, world'

@app.route('/api/fruits')
def get_fruits():
    return{
        'users': ['Apple', 'Banana', 'Cherry']
    }

@app.route('/api/users')
def get_users():
    return{
        'users': ['Alice', 'Bob', 'Charlie']
    }


if __name__ == '__main__':
    app.run(debug=True) #By default, Flask runs on port 5000
    