from flask import Flask
app=Flask(__name__)
@app.route("/")
def Homepage():
    return """
    <html>
    <center> <h1> Welcome to my homepage </h1> </center>
    <center> We are the only Building Society in the UK </center> <br>
    <a href="http://localhost:5000/aboutus"> Who we are </a> <br>
    <a href="http://localhost:5000/services"> Here are our services </a> <br>
    </html>
    """
@app.route("/aboutus")
def Aboutus():
    return """
    <html>
    <center> <h2> This is who we are </h2> </center> <br>
    <a href="http://localhost:5000"> Homepage </a> <br>
    <ul>
        <li> Stew </li>
        <li> Nicola </li>
        <li> James </li>
    </ul>
    </html>
    """
@app.route("/services")
def Services():
    return """
    <html>
    <center> <h2> We provide the following services: </h2> </center> <br>
    <a href="http://localhost:5000"> Homepage </a> <br>
    <ul>
        <li> Open Account </li>
        <li> Deposit Money </li>
        <li> Withdraw Money </li>
    </ul>
    </html>
    """
app.run()