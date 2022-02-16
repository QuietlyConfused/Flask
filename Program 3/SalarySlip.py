from flask import Flask,render_template
app=Flask(__name__)
@app.route("/salary")
def Salary():
    name1="Stew"
    salary1=1900
    return render_template("SalarySlip.html",name=name1,salary=salary1)
app.run()