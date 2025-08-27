from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # Load configuration
    app.config.from_object('config')

    # Import and register blueprints
    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # Initialize extensions
    from .models import db
    db.init_app(app)

    from flask_migrate import Migrate
    migrate = Migrate(app, db)

    return app