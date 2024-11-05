from flask import Flask, render_template, request
import requests
import smtplib
import os

FAKE_BLOG_ENDPOINT = 'https://api.npoint.io/661093b156c4cc278ba1'
my_email = os.environ.get('_PYTHON_EMAIL_')
email_pw = os.environ.get('_PYTHON_EMAIL_PASSWORD_')

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
        message = data['message']
        name = data['name']
        phone = data['phone']
        contacting_email = data['email']

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=email_pw)
            connection.sendmail(from_addr=my_email, to_addrs=my_email, msg=f"{message}From: {name}\nPhone: {phone}\nEmail: {contacting_email}")
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
