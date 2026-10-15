from flask import Flask,render_template,request
app = Flask(__name__)


@app.route("/",methods=["GET","POST"]) #webアプリのトップURLにリクエストが来たらindex()
def index():
    message = "こんにちは！"
    if request.method == "POST":
        name = request.form["name"]

        if name =="":
            message = "名前を入力してください"
        else:
            message = name + "さんこんにちは！"
    return render_template("index.html",message=message) #message(html)=message(python)

@app.route("/next",methods=["GET","POST"])
def next():
    if request.method == "POST":
        ans = request.form["ans"]

        if ans != "yes" and ans != "no":
            ans = "回答はyesかnoで入力してください"
    else:
        ans = "回答を入力してください"
    return render_template("next.html",answer=ans)