from utils.report import attach_request_response
from utils.delete_siswa import delete_siswa_param, hit_delete_siswa


def test_delete_siswa_success(auth_headers, extra):
    params = delete_siswa_param()
    response = hit_delete_siswa(params, headers=auth_headers)
    attach_request_response(extra, params, response)

    assert response.status_code in (200, 201)
    assert response.json()["success"] is True