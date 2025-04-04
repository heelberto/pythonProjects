from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
import os


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)
imdb_token = os.environ.get('_TMDB_TOKEN_')
IMDB_MOVIE_INFO = 'https://api.themoviedb.org/3/movie'
IMDB_MOVIE_IMG = 'https://image.tmdb.org/t/p/w500'


# CREATE DB
class Base(DeclarativeBase):
    pass


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movie-collection.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# CREATE THE EXTENSTION
db = SQLAlchemy(model_class=Base)

#INITIALISE THE APP WITH THE EXTENSION
db.init_app(app)


# CREATE TABLE
class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(500), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=True)
    ranking: Mapped[int] = mapped_column(Integer, nullable=True)
    review: Mapped[str] = mapped_column(String(500), nullable=True)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


# Creating the form to update a movie rating
class Movie_Update_Form(FlaskForm):
    new_rating = StringField(label="Your Rating /10")
    new_review = StringField(label='Your Review')
    submit = SubmitField('Submit')

class Movie_Title_Search(FlaskForm):
    title_query = StringField(label='Movie Title')
    submit = SubmitField('Add Movie')

# Create table schema in the database, requires application context
with app.app_context():
    db.create_all()

"""
# Create and add a new movie
with app.app_context():
    new_movie = Movie(
        title="Avatar The Way of Water",
        year=2022,
        description="Set more than a decade after the events of the first film, learn the story of the Sully family (Jake, Neytiri, and their kids), the trouble that follows them, the lengths they go to keep each other safe, the battles they fight to stay alive, and the tragedies they endure.",
        rating=7.3,
        ranking=9,
        review="I liked the water.",
        img_url="https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg"
    )
    db.session.add(new_movie)
    db.session.commit()
"""


@app.route("/")
def home():
    #all_movies = Movie.query.all()
    result = db.session.execute(db.select(Movie).order_by(Movie.rating))
    movies_ranked = result.scalars().all()


    for i in range(len(movies_ranked)):
        movies_ranked[i].ranking = len(movies_ranked) - 1
    db.session.commit()

    return render_template("index.html", movies=movies_ranked)


@app.route("/edit", methods=["GET", "POST"])
def edit():
    form = Movie_Update_Form()
    movie_id = request.args.get('movie_id')
    movie = db.get_or_404(Movie, movie_id)
    if form.validate_on_submit():
        movie.rating = float(form.new_rating.data)
        movie.review = form.new_review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html', movie=movie, form=form)


@app.route('/delete')
def delete():
    movie_id = request.args.get('movie_id')
    movie = db.get_or_404(Movie, movie_id)
    if movie:
        db.session.delete(movie)
        db.session.commit()
    return redirect(url_for('home'))


@app.route('/add', methods=["GET", "POST"])
def add():
    form = Movie_Title_Search()
    if form.validate_on_submit():
        title_query = form.title_query.data
        url = f"https://api.themoviedb.org/3/search/movie?query={title_query}&include_adult=false&language=en-US&page=1"
        headers = {
            'accept': 'applications/json',
            'Authorization': f'Bearer {imdb_token}'
        }
        response = requests.get(url, headers=headers)
        data = response.json()
        query_list = data['results']
        return render_template('select.html', query_list=query_list)
    return render_template('add.html', form=form)


@app.route("/find")
def find():
    movie_id = request.args.get("movie_id")
    if movie_id:
        movie_api_url = f'{IMDB_MOVIE_INFO}/{movie_id}'

        headers = {
            'accept': 'applications/json',
            'Authorization': f'Bearer {imdb_token}'
        }
        result = requests.get(url=movie_api_url, headers=headers)
        data = result.json()
        new_movie = Movie(
            title=data['title'],
            year=data['release_date'].split('-')[0],
            img_url=f'{IMDB_MOVIE_IMG}{data['poster_path']}',
            description=data['overview']
        )
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for('edit', movie_id=new_movie.id))

if __name__ == '__main__':
    app.run(debug=True)
