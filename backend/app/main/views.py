from flask import jsonify

from .. import db
from ..models import Brand, Shoe
from ..schemas import brand_schema, brands_schema, shoe_schema, shoes_schema
from . import main


@main.route("/")
def index():
    return "Hello World"


@main.route("/shark", methods=["GET"])
def greetings():
    return "Shark! 🦈"


# ===================
# Shoe app endpoints
# ===================


@main.route("/brand/<id>", methods=["GET", "POST"])
def get_brand(id):
    brand = db.session.query(Brand).get(id)
    return jsonify(brand_schema.dump(brand))


@main.route("/brands", methods=["GET"])
def all_brands():
    all_brands = db.session.query(Brand).all()
    return jsonify({"brands": brands_schema.dump(all_brands)})


@main.route("/shoe/<id>", methods=["GET"])
def get_shoe(id):
    shoe = db.session.query(Shoe).get(id)
    return jsonify(shoe_schema.dump(shoe))


@main.route("/shoes", methods=["GET"])
def all_shoes():
    all_shoes = db.session.query(Shoe).all()
    return jsonify({"shoes": shoes_schema.dump(all_shoes)})


@main.route("/new_brand", methods=["GET", "POST"])
def new_brand():
    return None


@main.route("/new_shoe", methods=["GET", "POST"])
def new_shoe():
    return "New shoe"


# TODO:
#   - Add dummy data to database: https://stackoverflow.com/questions/19334604/creating-seed-data-in-a-flask-migrate-or-alembic-migration
#   - Create all endpoints
#   - Write unit tests for end points
#   - Continue with course: https://www.youtube.com/watch?v=lenV5aVOMp8
#   - Watch front end course internet intro
