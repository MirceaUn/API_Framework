import requests


def get_internet_status():
    endpoint = "https://dummyjson.com/test"
    response = requests.get(endpoint)
    return response


def add_user(firstname, lastname, age, gender):
    endpoint = "https://dummyjson.com/users/add"

    request_body = {
        "firstName": firstname,
        "lastName": lastname,
        "age": age,
        "gender": gender
    }

    return requests.post(endpoint, json=request_body)


def update_user(id_user, newfirstname):
    endpoint = f"https://dummyjson.com/users/{id_user}"

    request_body = {
        "firstName": newfirstname
    }

    return requests.patch(endpoint, json=request_body)


def delete_user(id_user):
    endpoint = f"https://dummyjson.com/users/{id_user}"
    return requests.delete(endpoint)

def get_user_by_id(id_user):
    endpoint = f"https://dummyjson.com/users/{id_user}"
    return requests.get(endpoint)

def get_list_of_users(limit, skip):
    endpoint = f"https://dummyjson.com/users?limit={limit}&skip={skip}"
    return requests.get(endpoint)

def search_user(name):
    endpoint = f"https://dummyjson.com/users/search?q={name}"
    return requests.get(endpoint)

def filter_users(filter_key,filter_value):
    endpoint = f"https://dummyjson.com/users/filter?key={filter_key}&value={filter_value}"
    return requests.get(endpoint)
