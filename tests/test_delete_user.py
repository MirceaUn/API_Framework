from requests_folder.users_api import delete_user


class TestDeleteUser:

    def test_delete_user(self):
        response = delete_user(6)

        assert response.status_code == 200, "Unexpected status code"
