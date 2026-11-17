from utils.report import attach_request_response
from utils.get_siswa import get_siswa_param, hit_get_siswa
from utils.report import attach_request_response, save_response, load_json
from pytest_html import extras as html_extras

FIELD_DICEK = ["nis", "nama", "kelas", "jurusan", "email", "telepon", "alamat"]

def test_get_siswa_success(auth_headers, extra):
    params = get_siswa_param()
    response = hit_get_siswa(params, headers=auth_headers)
    attach_request_response(extra, params, response)
    path = save_response(response, "get_siswa.json")

    assert response.status_code in (200, 201)
    assert response.json()["success"] is True

def test_get_siswa_match_create(auth_headers, extra):
    created = load_json("payloads", "create_siswa.json")

    params = get_siswa_param()
    response = hit_get_siswa(params, headers=auth_headers)
    attach_request_response(extra, params, response)

    assert response.status_code == 200
    daftar_siswa = response.json()["data"]["data"]
    assert len(daftar_siswa) == 1, f"Harusnya 1 siswa, ditemukan {len(daftar_siswa)}"
    siswa = daftar_siswa[0]

    perbandingan = {
        field: {
            "create": created.get(field),
            "get": siswa.get(field),
            "cocok": created.get(field) == siswa.get(field),
        }
        for field in FIELD_DICEK
    }

    extra.append(html_extras.json(perbandingan, name="Perbandingan Create vs Get"))
    for field, hasil in perbandingan.items():
        status = "OK" if hasil["cocok"] else "BEDA"
        print(f"[{status}] {field}: create={hasil['create']!r} | get={hasil['get']!r}")

    tidak_cocok = [f for f, h in perbandingan.items() if not h["cocok"]]
    assert not tidak_cocok, f"Field tidak cocok: {tidak_cocok}"