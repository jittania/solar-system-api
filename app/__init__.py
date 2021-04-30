from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# make a database/SQLAl object and a migrate object
db = SQLAlchemy()
migrate = Migrate()

def create_app(test_config=None):
    app = Flask(__name__)

    #DB Config
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@localhost:5432/ada_planets_development'
    
    db.init_app(app)
    migrate.init_app(app, db)
    from app.models.planet import Planet

    from .routes import planets_bp
    app.register_blueprint(planets_bp)

    return app
