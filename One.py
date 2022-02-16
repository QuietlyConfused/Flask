from flask import Flask
app=Flask(__name__)
@app.route("/aboutus")
def Message():
    return "Hello my friends"
@app.route("/nbs")
def Boom():
    return "Welcome to Nationwide"
app.run()