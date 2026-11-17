import json
from pytest_html import extras
from pathlib import Path

RESPONSE_DIR = Path(__file__).resolve().parent.parent / "reports" / "responses"
PAYLOAD_DIR = Path(__file__).resolve().parent.parent / "reports" / "payloads"
REPORT_DIR = Path(__file__).resolve().parent.parent / "reports"

def attach_request_response(extra, payload, response):
    extra.append(extras.json(payload, name="Request Payload"))
    try:
        body = response.json()
        extra.append(extras.json(body, name=f"Response ({response.status_code})"))
    except ValueError:   # response bukan JSON
        extra.append(extras.text(response.text, name=f"Response ({response.status_code})"))

def save_response(response, filename):
    RESPONSE_DIR.mkdir(parents=True, exist_ok=True)
    path = RESPONSE_DIR / filename
    path.write_text(
    json.dumps(response.json(), indent=2, ensure_ascii=False),
    encoding="utf-8",
    )
    return path

def load_json(folder, filename):
     path = REPORT_DIR / folder / filename
     return json.loads(path.read_text(encoding="utf-8"))

def save_payload(payload, filename):
    PAYLOAD_DIR.mkdir(parents=True, exist_ok=True)
    path = PAYLOAD_DIR / filename
    path.write_text(
        json.dumps(payload, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    return path