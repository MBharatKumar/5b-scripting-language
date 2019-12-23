from flask import Flask,redirect,render_template,request,url_for,session
import time
import re

app = Flask(__name__)
app.secret_key = "secret"

@app.route("/",methods=["GET","POST"])
def index():
    if request.method == "GET":
        return render_template("student.html", msg="")

    elif request.method == "POST":
        if request.form["usn"] == "" or request.form["dob"] == "" or request.form["m1"] == "" or request.form["m2"] == "" or request.form["m3"] == "":
            return render_template("student.html", msg = "fields are empty")

        elif int(request.form["m1"])<0 or int(request.form["m2"])<0 or int(request.form["m3"])<0:
             return render_template("student.html", msg = "invalid marks entered")

        else:
            try:
                time.strptime(request.form["dob"], "%d/%m/%Y")
            except ValueError:
                return render_template("student.html", msg = "date is invalid")

            if re.match("^[1][A-Z][A-Z][0-9][0-9][A-Z][A-Z][0-9][0-9][0-9]$", request.form["usn"]):
                avg = (int(request.form["m1"]) + int(request.form["m2"]) + int(request.form["m3"]))/3
                return render_template("student.html", msg="average is "+str(avg))

            else:
                return render_template("student.html", msg = "invalid usn")

if __name__ == '__main__':
    app.run(host='localhost', port=80, debug=True)