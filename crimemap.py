from flask import Flask, render_template, request
from dbhelper import DBHelper

app = Flask(__name__)
DB = DBHelper()

@app.route("/")
def home():
    data = None

    try:
        data = DB.get_all()
    except Exception as e:
        print(e)

    return render_template("home.html", data=data)

@app.route("/add", methods=["POST"])
def add():
    try:
        data = request.form.get("crimedata")

        DB.add(data)
    except Exception as e:
        print(e)

    return home()

@app.route("/clear")
def clear():
    try:
        DB.clear_all()
    except Exception as e:
        print(e)

    return home()


if __name__ == "__main__":
    app.run("0.0.0.0", port=5000, debug=True)