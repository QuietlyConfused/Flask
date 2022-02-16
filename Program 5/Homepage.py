from flask import Flask,render_template
app=Flask(__name__)
@app.route("/")
def Homepage():
    return render_template("Homepage.html")
@app.route("/timestable/<num>")
def Timestable(num):
    return render_template("Timestable.html",T=int(num))
app.run()