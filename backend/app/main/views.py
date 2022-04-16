from flask import jsonify, request
from sqlalchemy.exc import IntegrityError

from .. import db
from ..models import Brand, Shoe
from ..schemas import brand_schema, brands_schema, shoe_schema, shoes_schema
from . import main


@main.route("/")
def index():
    return "Shoe Tracker API"


# ===================
# Brand endpoints
# ===================


@main.route("/brands", methods=["GET"])
def get_all_brands():
    all_brands = db.session.query(Brand).all()
    return (
        jsonify(
            {"success": True, "resource": {"brands": brands_schema.dump(all_brands)}}
        ),
        200,
    )


@main.route("/brands/<id>", methods=["GET"])
def get_brand_by_id(id):
    brand = db.session.query(Brand).get(id)

    if brand:
        return jsonify({"success": True, "resource": brand_schema.dump(brand)}), 200

    return {
        "success": False,
        "message": f"Brand (id={id} not found",
    }, 404


# ===================
# Shoe endpoints
# ===================


@main.route("/shoes", methods=["GET"])
def get_all_shoes():
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


@main.route("/shoes/<id>", methods=["GET"])
def get_shoe_by_id(id):
    shoe = db.session.query(Shoe).get(id)

    if shoe:
        return jsonify({"success": True, "resource": shoe_schema.dump(shoe)}), 200

    return {
        "success": False,
        "message": f"Shoe (id={id} not found",
    }, 404


@main.route("/shoes", methods=["POST"])
def create_new_shoe():
    breakpoint()
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


@main.route("/shoes/<id>", methods=["DELETE"])
def delete_shoe_by_id(id: int):
    if db.session.query(Shoe).get(id):
        shoe = db.session.get(Shoe, id)
        db.session.delete(shoe)
        db.session.commit()
        return {"success": True, "message": f"Shoe (id={id}) deleted"}, 200

    return {"success": False, "message": f"Shoe (id={id}) not found"}, 404


@main.route("/shoes/<id>", methods=["PUT"])
def update_shoe(id: int):
    update_data = request.get_json()
    shoe = db.session.get(Shoe, id)

    if shoe:
        shoe.brand_id = update_data["brand_id"]
        shoe.model = update_data["model"]
        shoe.nickname = update_data["nickname"]
        shoe.distance = update_data["distance"]
        shoe.notes = update_data["notes"]
        shoe.alert_distance = update_data["alert_distance"]
        db.session.commit()

        return jsonify({"success": True, "resource": shoe_schema.dump(shoe)}), 200

    return {"success": False, "message": f"Shoe (id={id}) not found"}, 404
