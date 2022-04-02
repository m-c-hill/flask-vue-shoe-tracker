from flask import jsonify
from . import main
from .. import db


@main.route("/")
def index():
    return "Hello World"


@main.route("/shark", methods=["GET"])
def greetings():
    return "Shark! 🦈"


# ===================
# Shoe app endpoints
# ===================


@main.route("/all_brands", methods=["GET"])
def all_brands():
    return jsonify(db.session.query(Brand).all())


@main.route("/all_shoes", methods=["GET"])
def all_shoes():
    return "List of all shoes"


@main.route("/shoe/<id>", methods=["GET"])
def shoe_by_id(id):
    return id


@main.route("/new_brand", methods=["GET", "POST"])
def new_brand():
    return "New brand"


@main.route("/new_shoe", methods=["GET", "POST"])
def new_shoe():
    return "New shoe"
