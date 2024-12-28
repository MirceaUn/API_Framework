from requests_folder.users_api import filter_users


class TestFilterUsers:

    def test_filter_users(self):
        response = filter_users("address.city", "Washington")
        assert response.status_code == 200, "Unexpected status code"
        response_body = response.json()
        print(f"Total number of filtered results: {response_body['total']}")
