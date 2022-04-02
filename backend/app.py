from flask import Flask, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

import os

db = SQLAlchemy()


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(__name__)
    basedir = os.path.abspath(os.path.dirname(__file__))
    app.config[
        "SQLALCHEMY_DATABASE_URI"
    ] = f"sqlite:///{os.path.join(basedir, 'data.sqlite')}"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    return app


app = create_app()
from models import Brand, Shoe

with app.app_context():
    db.create_all()
CORS(app, resources={r"/*": {"origins": "*"}})


@app.route("/", methods=["GET"])
def home():
    return "Hello World!"


@app.route("/shark", methods=["GET"])
def greetings():
    return "Shark!"


# ===================
# Shoe app endpoints
# ===================


@app.route("/all_brands", methods=["GET"])
def all_brands():
    return jsonify(db.session.query(Brand).all())


@app.route("/all_shoes", methods=["GET"])
def all_shoes():
    return "List of all shoes"


@app.route("/shoe/<id>", methods=["GET"])
def shoe_by_id(id):
    return id


@app.route("/new_brand", methods=["GET", "POST"])
def new_brand():
    return "New brand"


@app.route("/new_shoe", methods=["GET", "POST"])
def new_shoe():
    return "New shoe"


def create_dummy_records():
    brands = [
        Brand("Brooks"),
        Brand("Saucony"),
        Brand("Nike"),
    ]

    db.session.bulk_save_objects(brands)
    # db.session.bulk_save_objects(shoes)
    db.session.commit()


if __name__ == "__main__":
    create_dummy_records()
    app.run(debug=True)
