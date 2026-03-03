from flask import Flask
app=Flask(__name__)
@app.route("/")
def welcome():
    return ("Welcome to this best course,this is an amazing course,thankyou")
@app.route("/index")
def index():
    return("Thus is an index page")
if __name__=='__main__':
    app.run(debug=True)