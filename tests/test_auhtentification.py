from services.api import *
from services.payloads import *
from services.json_schema import *
import pytest
import allure


@allure.epic('Authorization')
@allure.feature('Positive')
@allure.story('Correct login, password')
def test_success_authentification():

    # 1) Post authentificate request with correct credentionals
    # 2) Asserting status code is 200
    # 3) Validating response's JSON schema
    # 4) Checking key 'token' in response
    # 5) Updating header with token

    response = APIClient().authenticate(credentionals)
    APIClient().check_status_is_200(response)
    APIClient().validate_json_schema(AuthOkResponse, response.json())
    APIClient().exist_key_in_json(response.json()['token'])


@allure.epic('Authorization')
@allure.feature('Negative')
@pytest.mark.parametrize("auth_data, model, key_json, status",
                             [(wrong_credentionals, BadCredentionalsResponse, 'reason', 200),
                              (empty_credentionals, BadCredentionalsResponse, 'reason', 200)], 
                              ids=
                              ["Wrong login, password ",
                                "Empty login, password"])
def test_incorrect_authentification(auth_data, model, key_json, status):
    
    # 1) Post authentificate request with incorrect credentionals
    # 2) Asserting status code is 200
    # 3) Validating response's JSON schema
    # 4) Checking key 'reason' in response

    response = APIClient().authenticate(auth_data)
    APIClient().check_status(status, response)
    APIClient().validate_json_schema(model, response.json())
    APIClient().exist_key_in_json(response.json()[key_json])