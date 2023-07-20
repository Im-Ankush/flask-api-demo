from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/login/<username>",methods=['POST','GET'])
def user_login(username):
    
    return "Login Successful! "+username