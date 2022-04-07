from flask import jsonify, request

from .. import db
from ..models import Brand, Shoe
from ..schemas import brand_schema, brands_schema, shoe_schema, shoes_schema
from . import main


@main.route("/")
def index():
    return "Hello World"


# ==============
# Dummy endpoint
# ==============


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
    return {"brands": brands_schema.dump(all_brands)}


@main.route("/shoe/<id>", methods=["GET"])
def get_shoe(id):
    shoe = db.session.query(Shoe).get(id)
    return {"success": True, "resource": jsonify(shoe_schema.dump(shoe))}


@main.route("/shoes", methods=["GET"])
def all_shoes():
    all_shoes = db.session.query(Shoe).all()
    return (
        jsonify(
            {
                "success": True,
                "resource": {"shoes": shoes_schema.dump(all_shoes)},
            },
        ),
        200,
    )


@main.route("/new_shoe", methods=["GET", "POST"])
def add_shoe():
    post_data = request.get_json()
    shoe = Shoe(**post_data)
    db.session.add(shoe)
    db.session.commit()

    return {"success": True, "resource": shoe_schema.dump(shoe)}, 200


@main.route("/remove_shoe/<id>", methods=["GET", "DELETE"])
def remove_shoe(id: int):
    if db.session.query(Shoe).get(id):
        shoe = db.session.get(Shoe, id)
        db.session.delete(shoe)
        db.session.commit()
        return f"Shoe (id={id}) deleted", 200
    return f"Shoe (id={id}) not found", 404


# TODO: add "abort" method from Werkzeug; add success, resource method to all endpoints


# TODO:
#   - Write unit tests for end points
#   - Continue with course: https://www.youtube.com/watch?v=lenV5aVOMp8
#   - Watch front end course internet intro
