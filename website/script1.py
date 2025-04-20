import generator
from flask import Flask, render_template, request
app=Flask(__name__)

@app.route('/greet', methods=['POST'])
def greet():
    inputName = request.form['myName']
    inputWeight = request.form['myWeight']
    inputHeight = request.form['myHeight']
    inputSpeed = request.form['mySpeed']
    inputFoot = request.form['myFoot']

    myPosition = generator.assign_position(inputHeight, inputWeight, inputSpeed, inputFoot)

    return render_template("home.html", myName=inputName, myWeight=inputWeight, myHeight=inputHeight, mySpeed=inputSpeed, myFoot=inputFoot, myPosition=myPosition)

@app.route('/')
def home():  
    return render_template("home.html")

@app.route('/about/')
def about():
    return render_template("about.html")

if __name__=="__main__":
    app.run(debug=True)
