from flask import Flask

import os

def create_app():
    template_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'templates')
    app = Flask(__name__, template_folder=template_dir)
    
    # Load configuration
    app.config.from_object('config.Config')

    # Import and register blueprints
    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # Initialize extensions
    from .models import db
    db.init_app(app)

    from flask_migrate import Migrate
    migrate = Migrate(app, db)

    return app