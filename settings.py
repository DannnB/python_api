# settings.py
from dotenv import load_dotenv
load_dotenv()

import os

if os.getenv("FLASK_ENV") == "development":
    print("Running in development mode...")
