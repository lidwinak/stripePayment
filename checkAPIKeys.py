import os
from dotenv import load_dotenv

load_dotenv()

secret_key = os.getenv("API_secret_KEY")
print(f"Secret Key: {secret_key}")

publishable_key = os.getenv("API_publisher_KEY")
print(f"Publishable Key: {publishable_key}")
