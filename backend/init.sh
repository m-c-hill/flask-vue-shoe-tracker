# Delete after development
flask shell

from app.models import Shoe
from app import db

shoe_1 = Shoe(brand_id=10, model="Ghost 14", nickname="blue",distance=78, notes=None, alert_distance=500)
shoe_2 = Shoe(brand_id=11, model="Endorphin Speed 2", nickname="green",distance=120, notes=None, alert_distance=500)
shoe_3 = Shoe(brand_id=1, model="Zoom Fly 4", nickname="black",distance=0, notes=None, alert_distance=500)

db.session.add(shoe_1)
db.session.add(shoe_2)
db.session.add(shoe_3)

db.session.commit()
