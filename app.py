from flask import Flask,render_template,request
app = Flask(__name__)


@app.route("/",methods=["GET","POST"]) #webアプリのトップURLにリクエストが来たらindex()
def index():
    message = "こんにちは！"
    if request.method == "POST":
        name = request.form["name"]
        message = name + "さんこんにちは！"
    return render_template("index.html",message=message)