from requests_folder.users_api import add_user


class TestAddUser:

    def test_success_add_user(self):
        response = add_user("Gigi", "Prodan", 24, "Male")
        response_body = response.json()
        assert response.status_code == 201, "Unexpected status code"
        print(f"Codul noii inregistrari este: {response_body['id']}")

