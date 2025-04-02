import datetime

from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import date


app = Flask(__name__)
ckeditor = CKEditor(app)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


class PostForm(FlaskForm):
    title = StringField('Blog Post Title')
    subtitle = StringField('Subtitle')
    author = StringField('Your Name')
    bg_url = StringField('Blog Image URL')
    body = CKEditorField('Blog Content')
    submit = SubmitField('Submit')

# CREATE DATABASE
class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CONFIGURE TABLE
class BlogPost(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


with app.app_context():
    db.create_all()


@app.route('/')
def get_all_posts():
    posts = db.session.execute(db.select(BlogPost)).scalars()
    return render_template("index.html", all_posts=posts)


@app.route('/show_post/<post_id>')
def show_post(post_id):
    requested_post = db.get_or_404(BlogPost, post_id)
    return render_template("post.html", post=requested_post)


# TODO: add_new_post() to create a new blog post
@app.route('/new-post', methods=['GET', 'POST'])
def add_new_post():
    source = request.args.get('source')
    form = PostForm()
    if form.validate_on_submit():
        # print(form.title.data)
        newPost = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            #date= 'July 13, 2023',
            date=datetime.datetime.now().strftime("%B %d, %Y"),
            body=form.body.data,
            author=form.author.data,
            img_url='https://imgs.search.brave.com/BW__i2u-_aUDX7WcqOc0ZZIrdXUDN73s-jcnwRqSN8k/rs:fit:1024:704:1/g:ce/aHR0cHM6Ly9zdGF0/aWMwMS5ueXQuY29t/L2ltYWdlcy8yMDEx/LzAxLzE0L2FydHMv/MTRNT1ZJTkctc3Bh/bi9NT1ZJTkctanVt/Ym8uanBn'
        )
        db.session.add(newPost)
        db.session.commit()
        return redirect(url_for('get_all_posts'))
    return render_template('make-post.html', form=form, source=source)


@app.route('/edit-post/<post_id>', methods=['GET','POST'])
def edit_post(post_id):
    source = request.args.get('source')
    requested_post = db.get_or_404(BlogPost, post_id)
    form = PostForm(obj=requested_post)

    if form.validate_on_submit():
        requested_post.title=form.title.data
        requested_post.subtitle=form.subtitle.data
        requested_post.author=form.author.data
        requested_post.img_url=form.bg_url.data
        requested_post.body=form.body.data
        print(form.body.data)

        db.session.commit()
        return redirect(url_for('get_all_posts'))

    return render_template('make-post.html', form=form, source=source)


# TODO: delete_post() to remove a blog post from the database

# Below is the code from previous lessons. No changes needed.
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5003)
