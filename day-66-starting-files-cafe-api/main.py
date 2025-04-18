from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
import random
app = Flask(__name__)


# CREATE DB
class Base(DeclarativeBase):
    pass
# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    def to_dict(self):
        dictionary = {}
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record - return all current cafes in db
@app.route("/random")
def random_cafe():
    cafes = db.session.execute(db.select(Cafe)).scalars()
    cafes_list = list(cafes)
    rand_cafe = random.choice(cafes_list)

    def cafe_to_dict(cafe):
        return {
            "id": cafe.id,
            "name": cafe.name,
            "map_url": cafe.map_url,
            "img_url": cafe.img_url,
            "location": cafe.location,
            "seats": cafe.seats,
            "has_toilet": cafe.has_toilet,
            "has_wifi": cafe.has_wifi,
            "has_sockets": cafe.has_sockets,
            "can_take_calls": cafe.can_take_calls,
            "coffee_price": cafe.coffee_price,
        }
    return jsonify(cafe_to_dict(rand_cafe))

    # alternate way of passing each 'column' from a cafe individually
    # return jsonify(name=rand_cafe.name)

# return all cafes
@app.route("/all")
def get_all():
    cafes = db.session.execute(db.select(Cafe)).scalars().all()
    return jsonify(cafes=[cafe.to_dict() for cafe in cafes])


# Search for a cafe by city name
@app.route("/search")
def cafe_search():
    query_location = request.args.get("loc")
    result = db.session.execute(db.select(Cafe).where(Cafe.location == query_location))
    all_cafes = result.scalars().all()
    if all_cafes:
        return jsonify(cafes=[cafe.to_dict() for cafe in all_cafes])
    else:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."}), 404


# HTTP POST - Create Record
@app.route("/add", methods=["POST"])
def post_new_cafe():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url") or request.args.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("loc"),
        has_sockets=bool(request.form.get("sockets")),
        has_toilet=bool(request.form.get("toilet")),
        has_wifi=bool(request.form.get("wifi")),
        can_take_calls=bool(request.form.get("calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={'success': 'Successfully added the new cafe.'}), 200

# HTTP PUT/PATCH - Update Record


@app.route("/update-price/<cafe_id>", methods=["PATCH"])
def update_price(cafe_id):
    if db.get_or_404(Cafe, cafe_id):
        cafe_to_edit = db.get_or_404(Cafe, cafe_id)
        cafe_to_edit.coffee_price = request.form.get('new_price')
        db.session.commit()
        return jsonify(response={'success': 'Successfully updated the price.'})
    else:
        return jsonify(error={'error': 'Sorry a cafe with that id was not found in the database'})

@app.route("/report-closed/<cafe_id>", methods=["DELETE"])
def report_closed(cafe_id):
    if db.get_or_404(Cafe, cafe_id):
        cafe_to_delete = db.get_or_404(Cafe, cafe_id)
        db.session.delete(cafe_to_delete)
        db.session.commit()
        return  jsonify(response={'success': 'Successfully removed the cafe from the list.'})


# HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)
