from requests_folder.users_api import get_list_of_users


class TestListUsers:

    def test_list_users_limit_skip(self):
        response = get_list_of_users(4, 2)
        assert response.status_code == 200, "Unexpected status code"
        response_body = response.json()
        assert len(response_body) == 4, "Unexpected number of users"

    def test_all_users(self):
        response = get_list_of_users(0, 0)
        assert response.status_code == 200, "Unexpected status code"
        response_body = response.json()
        assert response_body["total"] == response_body["limit"], "Unexpected different number of users presented"
        assert response_body["skip"] == 0, "Unexpected skipped users"
        print(f"Primul id_user este: {response_body['users'][0]['id']}")
        print(f"Ultimul id_user este: {response_body['users'][-1]['id']}")
