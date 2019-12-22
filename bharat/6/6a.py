from flask import Flask, redirect, render_template, request, url_for, session

app = Flask(__name__)
app.secret_key = "secret"

@app.route("/",methods=("GET","POST"))
def index():
    try:
        amt = session["amt"]
    except KeyError:
        amt = session["amt"] = 0

    if request.method == "GET":
        return render_template("mart.html", msg="")

    elif request.method == "POST":
        if request.form["egg"] == "" or request.form["bre"] == "" or request.form["mil"] == "":
            msg = "the fields are empty"
            return render_template("mart.html", msg=msg)

        if int(request.form["egg"])<0 or int(request.form["bre"])<0 or int(request.form["mil"])<0:
            msg = "invalid values entered"
            return render_template("mart.html", msg=msg)

        else:
            amt = amt + int(request.form["egg"])*5 + int(request.form["bre"])*20 + int(request.form["mil"])*10
            session["amt"] = amt
            msg = "total amount is Rs."+str(session["amt"])
            return render_template("mart.html", msg=msg)

if __name__ == '__main__':
    app.run(host="localhost", port=80, debug=True)
