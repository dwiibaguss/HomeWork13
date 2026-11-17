import os
import random
import time

import requests
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL")


def build_siswa_payload(**overrides):
    """Bikin data siswa unik supaya tidak bentrok (NIS/email duplikat)."""
    stamp = str(int(time.time() * 1000))                       # 13 digit
    nis = stamp + "".join(random.choices("0123456789", k=7))   # total 20 digit
    payload = {
        "nis": nis,
        "nama": "Jhon Thor",
        "kelas": "X-IPA-4",
        "jurusan": "IPA",
        "email": f"siswa{stamp}@pas.com",
        "telepon": "0812" + "".join(random.choices("0123456789", k=7)),
        "alamat": "Jl. Contoh No. 777",
    }
    payload.update(overrides)   # timpa field tertentu untuk skenario negatif
    return payload


def hit_create_siswa(payload, headers=None):
    return requests.post(
        f"{BASE_URL}/api/siswa",
        json=payload,
        headers=headers,
        timeout=30,
    )