from flask import Flask
from markupsafe import escape

# Creating an instance of Flask class
app = Flask(__name__)

#Using the decorator to tell python what URL should trigger our function
@app.route("/owner")
def hello_world():
    name = "Carlos"
    #Returns the message we want to display in the user’s browser
    return f" Hello {escape(name)}!"


#Main page
@app.route("/main_page")
def Tests():
    return "<h>THIS IS THE MAIN PAGE<h>"

