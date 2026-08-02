import os 
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
my_api_key = os.getenv("Groq api key")
if not my_api_key:
    return ValueError("api error")