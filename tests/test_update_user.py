from requests_folder.users_api import update_user
from requests_folder.users_api import get_user_by_id


class TestUpdateUser:

    def test_update_user(self):
        initial_response = get_user_by_id(3)
        initial_response_body = initial_response.json()
        print(initial_response_body["firstName"])

        response = update_user(3, "Gigi")
        response_body = response.json()

        assert response.status_code == 200, "Unexpected status code"
        assert initial_response_body["firstName"] != response_body["firstName"]

    def test_bad_id_update_user(self):
        response = update_user(9000, "Gigi")
        response_body = response.json()
        assert response.status_code == 404, "Unexpected status code"
        print(response_body["message"])
