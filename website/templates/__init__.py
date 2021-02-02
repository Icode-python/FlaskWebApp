from flask import Flask

# Setting up the Flask App
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'helloworld'
    # Secret key can be whatever you want
    return app


