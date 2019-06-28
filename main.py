from flask import Flask, flash, redirect, render_template,request,session,abort

app = Flask(__name__)

@app.route("/")
def my_form():
    greet = "The nearest parking lot is St. Paul's parking centre"
    return render_template("test.html",name=greet)#processed_text

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080, debug=True)

