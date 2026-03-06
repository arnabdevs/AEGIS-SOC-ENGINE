# wsgi.py at repository root
import sys
import os

# Add the backend directory to the Python path
backend_path = os.path.join(os.path.dirname(__file__), 'backend')
if backend_path not in sys.path:
    sys.path.insert(0, backend_path)

# Import the actual Flask app from the backend folder
from app import app

if __name__ == "__main__":
    app.run()
