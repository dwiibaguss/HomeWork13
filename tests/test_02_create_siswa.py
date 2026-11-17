from utils.report import attach_request_response, save_response, load_json, save_payload
from utils.create_siswa import build_siswa_payload, hit_create_siswa


def test_create_siswa_success(auth_headers, extra):
    payload = build_siswa_payload()
    response = hit_create_siswa(payload, headers=auth_headers)
    attach_request_response(extra, payload, response)
    save_payload(payload, "create_siswa.json")

    assert response.status_code in (200, 201)
    assert response.json()["success"] is True

"""
def test_create_siswa_nama_kosong(auth_headers):
    payload = build_siswa_payload(nama="")
    response = create_siswa(payload, headers=auth_headers)

    assert response.status_code in (400, 422)
    assert response.json()["success"] is False
"""
