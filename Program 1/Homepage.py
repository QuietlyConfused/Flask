from flask import Flask,render_template
app=Flask(__name__)
@app.route("/")
def Homepage():
    return render_template("homepage.html")
@app.route("/aboutus")
def Aboutus():
    return render_template("aboutus.html")
@app.route("/services")
def Services():
    return render_template("services.html")
app.run()