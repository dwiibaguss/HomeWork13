import os
import requests
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL")


def login(email=None, password=None):
    payload = {
        "email": email or os.getenv("LOGIN_EMAIL"),
        "password": password or os.getenv("LOGIN_PASSWORD"),
    }
    return requests.post(
        f"{BASE_URL}/api/auth/login",
        json=payload,
        timeout=30,
    )


def get_token():
    response = login()
    response.raise_for_status()
    body = response.json()
    return response.json()["data"]["token"]   # sesuaikan dengan response API