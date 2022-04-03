from flask_marshmallow import Marshmallow

ma = Marshmallow()


class BrandSchema(ma.Schema):
    class Meta:
        fields = ("id", "name")

class ShoeSchema(ma.Schema)
    class Meta:
        # TODO: replace brand_id with brand name?
        fields = {"id", "brand_id", "model", "nickname", "distance", "notes", "alert_distance"}

brand_schema = BrandSchema()
brands_schema = BrandSchema(many=True)

shoe_schema = ShoeSchema()
shoes_schema = ShoeSchema(many=True)