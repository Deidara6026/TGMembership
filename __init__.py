from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    """Construct the core application."""
    server = Flask(__name__, instance_relative_config=False)
    server.config.from_object('config.Config')

    db.init_app(server)

    with server.app_context():
        from . import routes  # Import routes
        db.create_all()  # Create sql tables for our data models

        return server