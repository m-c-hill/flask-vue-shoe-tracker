import os

import click
from flask_migrate import Migrate, upgrade

from app import create_app, db
from app.schemas import BrandSchema, ma

app = create_app(os.getenv("FLASK_CONFIG") or "default")
migrate = Migrate(app, db)
ma.init_app(app)


@app.cli.command()
def deploy():
    """Run deployment tasks."""
    # migrate database to latest revision
    upgrade()

    Brand.insert_brands()
