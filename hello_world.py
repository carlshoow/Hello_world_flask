from flask import Flask

# Creating an instance of Flask class
app = Flask(__name__)

#Using the decorator to tell python what URL should trigger our function
@app.route("/")

def hello_world():
    #Returns the message we want to display in the user’s browser
    return "<h1>Hello World</h1>"
