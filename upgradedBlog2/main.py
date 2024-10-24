from flask import Flask, render_template
import requests

FAKE_BLOG_ENDPOINT = 'https://api.npoint.io/661093b156c4cc278ba1'

response = requests.get(url=FAKE_BLOG_ENDPOINT)
response.raise_for_status()
posts = response.json()



app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html",all_posts=posts)


@app.route("/contact")
def get_contact():
    return render_template("contact.html")


@app.route("/about")
def get_about():
    return render_template("about.html")


@app.route("/post/<int:post_id>")
def post_detail():
    return render_template("post.html", all_posts=posts)


if __name__ == "__main__":
    app.run(debug=True)
