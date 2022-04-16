from collections import UserList
from typing import List

from app import db
from app.utils.brands import brand_names


class Brand(db.Model):
    __tablename__ = "brands"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    shoes = db.relationship("Shoe", backref="brands", lazy="dynamic")

    @staticmethod
    def create(brand):
        new_brand = Brand(brand=brand)
        db.session.add(new_brand)
        db.session.commit()

    @staticmethod
    def insert_brands():
        for b in brand_names:
            brand = Brand.query.filter_by(name=b).first()
            if brand is None:
                brand = Brand(name=b)
            db.session.add(brand)
        db.session.commit()

    @staticmethod
    def get_brands() -> List[dict]:
        return [{"id": i.id, "name": i.name} for i in Brand.query.order_by("id").all()]


class Shoe(db.Model):
    __tablename__ = "shoes"

    id = db.Column(db.Integer, primary_key=True)
    brand_id = db.Column(db.Integer, db.ForeignKey("brands.id"))
    brand = db.relationship("Brand", uselist=False, lazy="select")
    model = db.Column(db.String(64))
    nickname = db.Column(db.String(64), unique=True)
    distance = db.Column(db.Integer)
    notes = db.Column(db.String(128))
    alert_distance = db.Column(db.Integer, default=500)


# TODO: Add nullable=False to applicable fields; update endpoints to reflect this
