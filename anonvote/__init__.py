from flask import Flask, render_template
from flask_assets import Bundle, Environment
from flask_sqlalchemy import SQLAlchemy


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile("dev.cfg")

    scss = Bundle(
        "scss/main.scss",
        filters="pyscss",
        depends=("scss/*"),
        output="gen/css/main.css",
    )
    assets = Environment(app)
    assets.register("scss", scss)

    db = SQLAlchemy(app)

    with app.app_context():
        db.create_all()

        @app.route("/")
        def index():
            return render_template("index.html")

    return app
