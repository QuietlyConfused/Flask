from flask import Flask,render_template
app=Flask(__name__)
@app.route("/salary/<name1>/<salary1>")
def Salary(name1,salary1):
    return render_template("SalarySlip.html",name=name1,salary=int(salary1))
app.run()