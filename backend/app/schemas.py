from flask_marshmallow import Marshmallow

ma = Marshmallow()


class BrandSchema(ma.Schema):
    class Meta:
        fields = ("id", "name")


class ShoeSchema(ma.Schema):
    class Meta:
        fields = (
            "id",
            "brand",
            "model",
            "nickname",
            "distance",
            "notes",
            "alert_distance",
        )
        include_fk = True

    brand = ma.Function(lambda obj: brand_schema.dump(obj.brand))


brand_schema = BrandSchema()
brands_schema = BrandSchema(many=True)

shoe_schema = ShoeSchema()
shoes_schema = ShoeSchema(many=True)
