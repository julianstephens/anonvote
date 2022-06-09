from flask import Flask, render_template
from flask_migrate import Migrate


from .extensions import *
from .routes import poll_bp, item_bp


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile("dev.cfg")

    poll_bp.register_blueprint(item_bp)
    app.register_blueprint(poll_bp)

    db.init_app(app)

    migrate = Migrate(app, db)

    with app.app_context():
        db.create_all()

        @app.route("/")
        def index():
            return render_template("index.html")

    return app
