from flask_marshmallow import Marshmallow

ma = Marshmallow()


class BrandSchema(ma.Schema):
    class Meta:
        fields = ("id", "name")


brand_schema = BrandSchema()
brands_schema = BrandSchema(many=True)
