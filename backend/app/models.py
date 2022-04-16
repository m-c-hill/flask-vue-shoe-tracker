from app import db


class Brand(db.Model):
    __tablename__ = "brands"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    shoes = db.relationship("Shoe", backref="brands", lazy="dynamic")

    def __init__(self, name):
        self.name = name


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
