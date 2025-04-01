from services.api import *
from services.payloads import payload_correct_dates as payload, credentionals
from services.json_schema import *
import pytest
import allure

@allure.epic('Getting booking')
@allure.feature('Positive')
@allure.story("Get booking by id")
def test_get_booking_by_id():

    # 1) Creating booking with correct payload
    # 2) Asserting status code is 200
    # 3) Checking values in payloads and response
    # 4) Validating response's JSON schema
    # 5) Getting booking by id
    # 6) Checking values in payloads and response
    # 7) Validating response's JSON schema
    # 8) Deleting booking by id

    response = APIClient().create_booking(payload)
    APIClient().check_status(200, response)
    if response.status_code != 500:
        APIClient().check_value(payload["firstname"], response.json()["booking"]["firstname"])
        APIClient().check_value(payload["lastname"], response.json()["booking"]["lastname"])
        APIClient().check_value(payload["bookingdates"]["checkin"], response.json()["booking"]["bookingdates"]["checkin"])
        APIClient().check_value(payload["bookingdates"]["checkout"], response.json()["booking"]["bookingdates"]["checkout"])
        
        APIClient().validate_json_schema(BookingCreate, response.json())

        id_booking = response.json()['bookingid']
        response = APIClient().get_booking_by_id(id_booking)
        APIClient().check_value(payload["firstname"], response.json()["firstname"])
        APIClient().check_value(payload["lastname"], response.json()["lastname"])
        APIClient().check_value(payload["bookingdates"]["checkin"], response.json()["bookingdates"]["checkin"])
        APIClient().check_value(payload["bookingdates"]["checkout"], response.json()["bookingdates"]["checkout"])
        APIClient().validate_json_schema(BookingPerson, response.json())
        APIClient().delete_booking(id_booking, credentionals)

@allure.epic('Getting booking')
@allure.feature('Negative')
@allure.story("Get deleted booking by id")
def test_get_booking():
    
    # 1) Creating booking with correct payload
    # 2) Asserting status code is 200
    # 3) Deleting booking by id
    # 4) Getting booking by id
    # 5) Asserting status code is 404


    response = APIClient().create_booking(payload)
    APIClient().check_status(200, response)
    id_booking = response.json()['bookingid']
    APIClient().delete_booking(id_booking, credentionals)
    resp2 = APIClient().get_booking_by_id(id_booking)
    APIClient().check_status(404, resp2)

@allure.epic('Getting booking')
@allure.feature('Positive')
@allure.story("Get all bookings")
def test_get_bookings_all_ids():
    response = APIClient().create_booking(payload)
    id_booking = response.json()['bookingid']
    response = APIClient().get_booking_ids()
    response_json = response.json()
    APIClient().exist_value_in_json('bookingid', id_booking, response_json)
    APIClient().not_empty_json(response_json)
    APIClient().check_status(200, response)
    APIClient().delete_booking(id_booking, credentionals)
        

@allure.epic('Getting booking')
@allure.feature('Positive')
@allure.story("Get bookings by name")
def test_get_bookings_with_filter_name():
    
    # 1) Creating 5 bookings with correct payload
    # 2) Getting parametres from booking for search
    # 3) Getting booking by parametres
    # 4) Asserting json is not empty
    # 5) Asserting status code is 200
    # 6) Asserting values in json
    # 7) Deleting bookings by id
    
    list_bookings = []
    for i in range(5):
        response = APIClient().create_booking(payload)
        id_booking = response.json()['bookingid']
        list_bookings.append(id_booking)
    #print(list_bookings)
    firstname = response.json()["booking"]["firstname"]
    lastname = response.json()["booking"]["lastname"]
    params = {
        "firstname": firstname,
        "lastname": lastname
    }
    response = APIClient().get_booking_ids(params)
    response_json = response.json()
    #print(response_json)
    APIClient().not_empty_json(response_json)
    APIClient().check_status(200, response)
    for id in list_bookings:
        APIClient().exist_value_in_json('bookingid', id, response_json)
        APIClient().delete_booking(id, credentionals)

@allure.epic('Getting booking')
@allure.feature('Positive')
@allure.story("Get bookings by date")
def test_get_bookings_with_filter_dates():
        
    # 1) Creating 5 bookings with correct payload
    # 2) Getting parametres from booking for search
    # 3) Getting booking by parametres
    # 4) Asserting json is not empty
    # 5) Asserting status code is 200
    # 6) Asserting values in json
    # 7) Deleting bookings by id
    
    with allure.step("Create 5 bookings [{list_bookings}]"):
        list_bookings = []
        for i in range(5):
            response = APIClient().create_booking(payload)
            id_booking = response.json()['bookingid']
            list_bookings.append(id_booking)
            checkin = response.json()['booking']['bookingdates']['checkin']
            checkout = response.json()['booking']['bookingdates']['checkout']
    response = APIClient().get_booking_ids(params=f'?checkin={checkin}&checkout={checkout}')
    response_json = response.json()
    APIClient().not_empty_json(response_json)
    APIClient().check_status(200, response)
    for id in list_bookings:
        APIClient().exist_value_in_json('bookingid', id, response_json)
        APIClient().delete_booking(id, credentionals)