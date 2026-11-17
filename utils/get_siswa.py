import os
import random
from utils.report import load_json

import requests
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL")

def get_siswa_param(**overrides):
    created = load_json("payloads", "create_siswa.json")
    params = {
    "search" : created["nis"],
    }
    params.update(overrides)
    return params

def hit_get_siswa(params, headers=None):
        url = f"{BASE_URL}/api/siswa"
       
        response = requests.get(
        url,
        params=params,
        headers=headers,
        timeout=30,
        )

        response.raise_for_status()

        return response

