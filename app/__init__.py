from flask import Flask
from app.routes import home, dashboard, api
from app.db import init_db
from app.utils import filters


def create_app(text_config=None):
    # set up app config
    app = Flask(__name__, static_url_path='/')
    app.url_map.strict_slashes = False
    app.config.from_mapping(
        SECRET_KEY='super_secret_key'
    )

    # register routes
    app.register_blueprint(home)
    app.register_blueprint(dashboard)
    app.register_blueprint(api)

    # add filters
    app.jinja_env.filters['format_date'] = filters.format_date
    app.jinja_env.filters['format_plural'] = filters.format_plural

    init_db(app)

    return app
