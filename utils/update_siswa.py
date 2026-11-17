import os
import random
import requests

from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL")

def update_siswa_payload():
    return {"nama": "Pergi Jauh",
            "kelas": "X-IPA-100"}

def hit_update_siswa(siswa_id, payload, headers=None):
    url = f"{BASE_URL}/api/siswa/{siswa_id}"

    response = requests.put(
        url,
        json=payload,
        headers=headers,
        timeout=30,
    )

    return response

