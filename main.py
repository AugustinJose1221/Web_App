from flask import Flask, flash, redirect, render_template,request,session,abort

app = Flask(__name__)

@app.route("/")
def my_form():
    return render_template('test.html')

@app.route("/",methods=['POST'])
def my_form_post():
    nearest_park = "Django's garage" #str(h_list[pos,0])
    greet = "Nearest parking lot is "+nearest_park
    return render_template("test.html",name=greet)#processed_text

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080, debug=True)

