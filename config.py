import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    # Flask Core Settings
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-default-secret-key-for-dev'
    DEBUG = False
    TESTING = False
    
    # Database Settings
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # API Settings
    API_TITLE = 'NFL Predictive Analytics API'
    API_VERSION = '1.0'
    
    # Scheduler Settings
    SCHEDULER_API_ENABLED = True
    JOBS = [
        {
            'id': 'data_collection',
            'func': 'app.scheduler.jobs:collect_data',
            'trigger': 'interval',
            'minutes': 60  # Run every hour by default
        },
        {
            'id': 'model_training',
            'func': 'app.scheduler.jobs:train_model',
            'trigger': 'cron',
            'hour': 2  # Run at 2 AM every day by default
        }
    ]

class DevelopmentConfig(Config):
    DEBUG = True
    # Shorter intervals for testing
    JOBS = [
        {
            'id': 'data_collection',
            'func': 'app.scheduler.jobs:collect_data',
            'trigger': 'interval',
            'minutes': 5  # Run every 5 minutes in development
        },
        {
            'id': 'model_training',
            'func': 'app.scheduler.jobs:train_model',
            'trigger': 'interval',
            'minutes': 30  # Run every 30 minutes in development
        }
    ]

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'  # Use in-memory database for tests
    SCHEDULER_API_ENABLED = False  # Disable scheduler during tests

class ProductionConfig(Config):
    # Production-specific settings
    DEBUG = False
    
    # Use strong secret key in production
    SECRET_KEY = os.environ.get('SECRET_KEY')
    
    # Ensure all sensitive configs come from environment variables
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    
    # Production logging
    LOG_LEVEL = 'INFO'

# Dictionary to easily access different configs
config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
