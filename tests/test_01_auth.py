from utils.auth import login


def test_login_success():
    response = login()
    assert response.status_code == 200
        
    body = response.json()
    assert body["success"] is True
    assert body["message"] == "Login berhasil"
    assert body["data"]["token"]
    assert body["data"]["user"]["email"] == "dwii.baguss92@gmail.com" 


def test_token_is_jwt_format(token):
    # JWT terdiri dari 3 bagian dipisah titik: header.payload.signature
    assert len(token.split(".")) == 3


def test_login_wrong_password():
    response = login(password="SalahTotal123")
    assert response.status_code in (400, 401)
    assert response.json()["success"] is False

def test_login_user_tidak_terdaftar():
    response = login(email="dwii.bagus92@gmail.com")
    assert response.status_code in (400, 401)
    assert response.json()["success"] is False