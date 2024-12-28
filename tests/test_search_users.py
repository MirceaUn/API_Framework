from requests_folder.users_api import search_user


class TestSearchUsers:

    def test_search_user(self):
        response = search_user("Lily")
        assert response.status_code == 200, "Unexpected status code"

        response_body = response.json()
        print(f"Total search results: {response_body['total']}")
