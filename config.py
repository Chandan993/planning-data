import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()   # loads .env file

client = OpenAI(api_key=os.getenv("DEEPSEEK_API_KEY"))
