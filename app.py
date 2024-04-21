from flask import Flask, request, redirect, render_template
from dotenv import load_dotenv
from models import User, session
load_dotenv()

app = Flask(__name__)
@app.route('/post')
def post():
    if request.method == "POST":
        title = request.form["title"]

        text = request.form["text"]

        post = User(
            title=title,
            text=text
        )
        try:
            session.add(post)
            session.commit()
            return redirect("/index")
        except Exception as exc:
            return f"ПРи збереженні запису у базу даних виникла помилка: {exc}"
    else:
        return render_template("create_article.html")

@app.route('index')
def index():
    return render_template('index.html')
