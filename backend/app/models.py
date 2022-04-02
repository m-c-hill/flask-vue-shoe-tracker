from app import db


class Brand(db.Model):
    __tablename__ = "brands"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    shoes = db.relationship("Shoe", backref="brands", lazy="dynamic")


class Shoe(db.Model):
    __tablename__ = "shoes"
    id = db.Column(db.Integer, primary_key=True)
    brand_id = db.Column(db.Integer, db.ForeignKey("brands.id"))
    model = db.Column(db.String(64))
    nickname = db.Column(db.String(64), unique=True)
    distance = db.Column(db.Integer)
    notes = db.Column(db.String(128))
    alert_distance = db.Column(db.Integer)
