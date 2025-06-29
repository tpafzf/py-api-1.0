from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_apscheduler import APScheduler
from config import config

# Initialize extensions
db = SQLAlchemy()
api = Api()
scheduler = APScheduler()

def create_app(config_name='default'):
    # Create Flask app instance
    app = Flask(__name__)
    
    # Use the config dictionary to get the correct configuration class
    app.config.from_object(config[config_name])

    # Initialize extensions with app
    # db.init_app(app)
    api.init_app(app)
    # scheduler.init_app(app)

    # Register blueprints
    from app.players.players_bp import players_bp
    app.register_blueprint(players_bp)
    
    # Import routes after blueprint registration to avoid circular imports
    from app.players import routes

    # Initialize scheduler jobs
    """ with app.app_context():
        from app.scheduler.jobs import init_jobs
        init_jobs(scheduler)
        scheduler.start() """

    return app 