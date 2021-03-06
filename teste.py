# import flask dependencies
from flask import Flask, request, make_response, jsonify

# initialize the flask app
app = Flask(__name__)

# default route
@app.route('/')
def index():
    return 'Build via Jenkins via CI/CD ;)'

# run the app
if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5000)
