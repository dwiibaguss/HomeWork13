import os
import random
from utils.report import load_json

import requests
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL")

def delete_siswa_param(**overrides):
    created = load_json ("responses", "get_siswa.json")
    params = {
          "userid" : created["data"]["data"][0]["id"]
    }
    params.update(overrides)
    return params

def hit_delete_siswa(params, headers=None):
        url = f"{BASE_URL}/api/siswa/{params['userid']}"

        return requests.delete(
        url,
        headers=headers,
        timeout=30,
            )