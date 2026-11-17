from utils.report import attach_request_response, save_response, load_json
from utils.update_siswa import update_siswa_payload, hit_update_siswa
# + import hit_update_siswa dan update_siswa_payload dari file masing-masing

def test_update_siswa_success(auth_headers, extra):
    saved = load_json("responses", "get_siswa.json")
    daftar_siswa = saved["data"]["data"]
    assert daftar_siswa, "get_siswa.json kosong, jalankan test get siswa dulu"
    siswa_id = daftar_siswa[0]["id"]

    payload = update_siswa_payload()
    response = hit_update_siswa(siswa_id, payload, headers=auth_headers)
    attach_request_response(extra, payload, response)
    save_response(response, "update_siswa.json")

    assert response.status_code == 200
    body = response.json()
    assert body["success"] is True