from utils.report import attach_request_response
from utils.get_siswa_by_class import get_siswa_by_class_param, hit_get_siswa_by_class
from utils.report import attach_request_response, save_response


def test_get_siswa_success(auth_headers, extra):
    params = get_siswa_by_class_param()
    response = hit_get_siswa_by_class(params, headers=auth_headers)
    attach_request_response(extra, params, response)
    path = save_response(response, "get_siswa_by_class.json")

    assert response.status_code in (200, 201)
    assert response.json()["success"] is True