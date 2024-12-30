About the project

The API tests from this repository were built in Python using:
- requests module
- pytest, pytest-html and pytest_tagging modules
- POSTMAN app

The documentation for the API tests can be found at: https://dummyjson.com/docs/users

----------------------------------------------------------------------------------------------------------------------------------------------

API Interactions and Tests description

Tests were made for all the types of API interactions:
- POST - A new user is created and the test asserts that the status code is successful and also prints the ID of the new entry
- PATCH - For a given user ID the value of the "firstName" key is updated and the test asserts that the status code is successful and the updated value is different from the initial one
        - In the second test an incorrect user ID is given and the test asserts that the status code is unsuccessful and the error message is diplayed
- DELETE - A given user ID is deleted and the test asserts that the status code is successful
- GET - has been used for multiple tests, as follows:
        1. To check the internet status -> the test asserts that the status code is successful and also prints a status message
        2. To check, when asked about displaying the list of users, if the "limit" and "skip" parameters function correctly
        3. To check, when asked about a filtered list of users, if the parameters for "key" and "value" function correctly
        4. To check, when asked to search for a specific name, that it displays the correct entries from the database
