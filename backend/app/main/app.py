"""
from flask import jsonify
from . import main
from flask_sqlalchemy import SQLAlchemy


app = create_app()
from backend.app.models import Brand, Shoe


@app.route("/", methods=["GET"])
def home():
    return "Hello World!"





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
"""
