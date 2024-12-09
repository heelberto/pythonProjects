from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

app = Flask(__name__)
app.config['SECRET_KEY'] = 'RANDOMTEXT'


# first create the database
class Base(DeclarativeBase):
    pass


# configure the extension and initialise the app with the extension
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"
db = SQLAlchemy(model_class=Base)
db.init_app(app)

all_books = []
# Create a table
class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)


# create the table schema in the database
with app.app_context():
    db.create_all()


@app.route('/')
def home():
    # pull all books
    with app.app_context():
        all_books = db.session.query(Book).all()

    return render_template('index.html', books=all_books)


@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == 'POST':

        with app.app_context():
            new_book = Book(title=request.form['title'], author=request.form['author'], rating=request.form['rating'])
            db.session.add(new_book)
            db.session.commit()
        # new_book = {
        #    'title': request.form['title'],
        #    'author': request.form['author'],
        #    'rating': request.form['rating']
        # }
        # all_books.append(new_book)

        # pull all books once more before heading back to the home directory
        with app.app_context():
            all_books = db.session.query(Book).all()
        return redirect(url_for('home'))
    else:
        return render_template('add.html')


@app.route("/edit", methods=['GET', 'POST'])
def edit():
    if request.method == 'POST':
        book_id = request.form['id']
        book_to_update = db.get_or_404(Book, book_id)
        book_to_update.rating = request.form['new_rating']
        db.session.commit()
        return redirect(url_for('home'))
    book_id = request.args.get('id')
    book_selected = db.get_or_404(Book, book_id)
    return render_template('edit.html', book=book_selected)


@app.route("/delete")
def delete():
    book_id = request.args.get("id")

    book_to_delete = db.get_or_404(Book, book_id)

    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)
