import sys
import os

# Add backend directory to PYTHONPATH
sys.path.append(os.path.join(os.path.dirname(__file__), 'backend'))

from app.main import app

if __name__ == '__main__':
    app.run(debug=True)
