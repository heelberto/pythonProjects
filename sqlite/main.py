from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

app = Flask(__name__)

##CREATE DATABASE
class Base(DeclarativeBase):
    pass

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"

# Create the extension
db = SQLAlchemy(model_class=Base)
# Initialise the app with the extension
db.init_app(app)


##CREATE TABLE
class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)

    # Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f'<Book {self.title}>'


# Create table schema in the database. Requires application context.
with app.app_context():
    db.create_all()

# CREATE RECORD
# with app.app_context():
#    new_book = Book(title="Harry Potter and Scorcer's Stone", author="J. K.", rating=9.3)
#    db.session.add(new_book)
#    db.session.commit()

# editing an existing record
with app.app_context():
    book_to_update = db.session.execute(db.select(Book).where(Book.id == 1)).scalar()
    book_to_update.title = "New title"
    db.session.commit()

# displaying all books
with app.app_context():
    result = db.session.query(Book).all()
    for book in result:
        print(f"ID: {book.id}, Title: {book.title}, Author: {book.author}, Rating: {book.rating}")
