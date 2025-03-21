from services.api import *
from services.payloads import payload_correct_dates as payload, credentionals, wrong_credentionals
from services.json_schema import *
import pytest
import allure


@allure.epic("Update booking")
@allure.feature("Positive")
@allure.story("Update booking by 'put'")
def test_update_booking_put():

    # 1) Creating new booking
    # 2) Authentificating and updating booking
    # 3) Checking status code is 200
    # 4) Checking values in updated payload and response
    # 5) Validating response's JSON schema
    # 6) Deleting booking by id

    response = APIClient().create_booking(payload)
    id_booking = response.json()['bookingid']
    updated_payload = payload
    updated_payload['additionalneeds'] = "breakfast, pool, lunch"
    response = APIClient().update_booking(id_booking, payload, credentionals)
    APIClient().check_status(200, response)
    APIClient().check_value(updated_payload["firstname"], response.json()["firstname"])
    APIClient().check_value(updated_payload["lastname"], response.json()["lastname"])
    APIClient().check_value(updated_payload["bookingdates"]["checkin"], response.json()["bookingdates"]["checkin"])
    APIClient().check_value(updated_payload["bookingdates"]["checkout"], response.json()["bookingdates"]["checkout"])
    APIClient().check_value(updated_payload["additionalneeds"], response.json()["additionalneeds"])
    APIClient().validate_json_schema(BookingPerson, response.json())    
    APIClient().delete_booking(id_booking, credentionals)


@allure.epic("Update booking")
@allure.feature("Negative")
@allure.story("Update booking by 'put' with wrong type data")
def test_wrong_data_update_booking_put():

    # 1) Creating new booking
    # 2) Authentificating and updating booking
    # 3) Checking status code is 200
    # 4) Checking values in updated payload and response. Wrong type data in updated payload becomes None type.
    # 5) Validating response's JSON schema
    # 6) Deleting booking by id

    response = APIClient().create_booking(payload)
    id_booking = response.json()['bookingid']
    updated_payload = payload
    updated_payload['totalprice'] = "thousand"
    response = APIClient().update_booking(id_booking, payload, credentionals)
    APIClient().check_status(200, response)
    APIClient().check_value(updated_payload["firstname"], response.json()["firstname"])
    APIClient().check_value(updated_payload["lastname"], response.json()["lastname"])
    APIClient().check_value(updated_payload["bookingdates"]["checkin"], response.json()["bookingdates"]["checkin"])
    APIClient().check_value(updated_payload["bookingdates"]["checkout"], response.json()["bookingdates"]["checkout"])
    APIClient().check_value(None, response.json()["totalprice"])
    APIClient().validate_json_schema(BookingPerson, response.json())    
    APIClient().delete_booking(id_booking, credentionals)

@allure.epic("Update booking")
@allure.feature("Negative")
@allure.story("Update booking by 'put' without auth")
def test_update_booking_put_without_auth():

    # 1) Creating new booking
    # 2) Authentificating with wrong credentionals and updating booking
    # 3) Checking status code is 403

    response = APIClient().create_booking(payload)
    id_booking = response.json()['bookingid']
    updated_payload = payload
    updated_payload['additionalneeds'] = "breakfast, pool, lunch"
    response = APIClient().update_booking(id_booking, payload, wrong_credentionals)
    APIClient().check_status(403, response)    
    APIClient().delete_booking(id_booking, credentionals)


@allure.epic("Update booking")
@allure.feature("Positive")
@allure.story("Update booking by 'patch'")
def test_update_booking_patch():

    # 1) Creating new booking
    # 2) Authentificating and updating booking
    # 3) Checking status code is 200
    # 4) Checking values in updated payload and response
    # 5) Validating response's JSON schema
    # 6) Deleting booking by id

    response = APIClient().create_booking(payload)
    id_booking = response.json()['bookingid']        
    part_payload = {'additionalneeds' : "pool"}
    response = APIClient().patch_booking(id_booking, part_payload, credentionals)
    APIClient().check_status(200, response)
    APIClient().check_value(payload["firstname"], response.json()["firstname"])
    APIClient().check_value(payload["lastname"], response.json()["lastname"])
    APIClient().check_value(payload["bookingdates"]["checkin"], response.json()["bookingdates"]["checkin"])
    APIClient().check_value(payload["bookingdates"]["checkout"], response.json()["bookingdates"]["checkout"])
    APIClient().check_value(part_payload["additionalneeds"], response.json()["additionalneeds"])
    APIClient().validate_json_schema(BookingPerson, response.json())
    APIClient().delete_booking(id_booking, credentionals)


@allure.epic("Update booking")
@allure.feature("Negative")
@allure.story("Update booking by 'patch' with wrong type data")
def test_update_booking_patch_wrong_data():

    # 1) Creating new booking
    # 2) Authentificating and updating booking
    # 3) Checking status code is 200
    # 4) Checking values in updated payload and response. Wrong type data in updated payload becomes None type.
    # 5) Validating response's JSON schema
    # 6) Deleting booking by id

    response = APIClient().create_booking(payload)
    id_booking = response.json()['bookingid']        
    part_payload = {'totalprice' : "ten"}
    response = APIClient().patch_booking(id_booking, part_payload, credentionals)
    APIClient().check_status(200, response)
    APIClient().check_value(payload["firstname"], response.json()["firstname"])
    APIClient().check_value(payload["lastname"], response.json()["lastname"])
    APIClient().check_value(payload["bookingdates"]["checkin"], response.json()["bookingdates"]["checkin"])
    APIClient().check_value(payload["bookingdates"]["checkout"], response.json()["bookingdates"]["checkout"])
    APIClient().check_value(None, response.json()["totalprice"])
    APIClient().validate_json_schema(BookingPerson, response.json())
    APIClient().delete_booking(id_booking, credentionals)

@allure.epic("Update booking")
@allure.feature("Negative")
@allure.story("Update booking by 'patch' without auth")
def test_update_booking_patch_without_auth():

    # 1) Creating new booking
    # 2) Authentificating with wrong credentionals and updating booking
    # 3) Checking status code is 403

    response = APIClient().create_booking(payload)
    id_booking = response.json()['bookingid']        
    part_payload = {'additionalneeds' : "pool"}
    response = APIClient().patch_booking(id_booking, part_payload, wrong_credentionals)
    APIClient().check_status(403, response)    
    APIClient().delete_booking(id_booking, credentionals)