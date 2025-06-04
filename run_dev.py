import os
from app import create_app

# Set environment variables for development
os.environ['FLASK_ENV'] = 'development'
os.environ['FLASK_DEBUG'] = '1'

# Create app with development config
app = create_app('development')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000) 