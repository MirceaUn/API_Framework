from requests_folder.users_api import get_internet_status


class TestInternetStatus:

    def test_internet_status(self):
        response = get_internet_status()

        response_body = response.json()
        assert response.status_code == 200, "Unexpected status code"
        assert response_body["status"] == "ok", "Unexpected status message"
