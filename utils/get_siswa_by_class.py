import os
import random
from utils.report import load_json

import requests
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL")

print("BASE URL:", BASE_URL)

def get_siswa_by_class_param(**overrides):
    created = load_json("responses", "update_siswa.json")
    params = {
    "kelas" : created["data"]["kelas"],
    }
    params.update(overrides)
    return params

def hit_get_siswa_by_class(params, headers=None):
        url = f"{BASE_URL}/api/siswa"
       
        response = requests.get(
        url,
        params=params,
        headers=headers,
        timeout=30,
        )

        response.raise_for_status()

        return response

