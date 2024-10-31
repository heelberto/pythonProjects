from flask import Flask, render_template, request
import requests

FAKE_BLOG_ENDPOINT = 'https://api.npoint.io/661093b156c4cc278ba1'

response = requests.get(url=FAKE_BLOG_ENDPOINT)
response.raise_for_status()
posts = response.json()

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", all_posts=posts)


@app.route("/contact", methods=['POST', 'GET'])
def get_contact():
    if request.method == 'POST':
        data = request.form
        print(data['name'])
        # print(f"{}")
        # \n{request.form['email']}\n{request.form['phone']}\n{request.form['message']}")
        return render_template("contact.html", success=1)
    elif request.method == 'GET':
        return render_template("contact.html")
    else:
        return "Error"


@app.route("/about")
def get_about():
    return render_template("about.html")


@app.route("/post/<int:post_id>")
def post_detail(post_id):
    return render_template("post.html", all_posts=posts, post_id=post_id)




if __name__ == "__main__":
    app.run(debug=True)
