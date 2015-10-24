from flask import Flask
from flask_bootstrap import Bootstrap

def create_app():
    app = Flask(__name__)
    app.config.from_object('config')
    Bootstrap(app)

    return app

app = create_app()

from app import views