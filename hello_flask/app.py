from flask import Flask, request

app = Flask(__name__)

app.config['DEBUG']

@app.route('/')
def index_handler():
    for key, value in request.args.items():
        print(key, value)
    return value
    
    
@app.route('/another')
def index_home():
    return "not this one"

if __name__ == "__main__":
    app.run(port=8008)