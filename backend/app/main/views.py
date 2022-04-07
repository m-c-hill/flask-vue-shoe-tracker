from flask import jsonify, request
from sqlalchemy.exc import IntegrityError

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
    if brand:
        return jsonify({"success": True, "resource": brand_schema.dump(brand)}), 200
    return {
        "success": False,
        "message": f"Brand (id={id} not found",
    }, 404


@main.route("/brands", methods=["GET"])
def all_brands():
    all_brands = db.session.query(Brand).all()
    return (
        jsonify(
            {"success": True, "resource": {"brands": brands_schema.dump(all_brands)}}
        ),
        200,
    )


@main.route("/shoe/<id>", methods=["GET"])
def get_shoe(id):
    shoe = db.session.query(Shoe).get(id)
    if shoe:
        return jsonify({"success": True, "resource": shoe_schema.dump(shoe)}), 200
    return {
        "success": False,
        "message": f"Shoe (id={id} not found",
    }, 404


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
    try:
        db.session.add(shoe)
        db.session.commit()
    except IntegrityError:
        return {
            "success": False,
            "message": f"Nickname '{post_data['nickname']}' has already been assigned to another shoe",
        }, 422

    return {"success": True, "resource": shoe_schema.dump(shoe)}, 200


@main.route("/remove_shoe/<id>", methods=["GET", "DELETE"])
def remove_shoe(id: int):
    if db.session.query(Shoe).get(id):
        shoe = db.session.get(Shoe, id)
        db.session.delete(shoe)
        db.session.commit()
        return f"Shoe (id={id}) deleted", 200
    return f"Shoe (id={id}) not found", 404


# TODO: PUT method to update shoe values
# TODO: Write unit tests for all end points.
