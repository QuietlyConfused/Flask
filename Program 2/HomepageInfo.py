from flask import Flask,render_template
app=Flask(__name__)
@app.route("/info1")
def Info1():
    return render_template("information.html",na="Stew",addr="Bournemouth",colour="cyan")
@app.route("/info2")
def Info2():
    return render_template("information.html",na="Nicola",addr="Hereford",colour="blue")
@app.route("/info3")
def Info3():
    return render_template("information.html",na="Helen",addr="Mars",colour="orange")
app.run()