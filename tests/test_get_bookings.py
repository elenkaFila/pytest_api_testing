from services.api import *
from services.payloads import payload_correct_dates as payload, credentionals
from services.json_schema import *
import pytest
import allure

@allure.epic('Getting booking')
@allure.feature('Positive')
@allure.story("Get booking by id")
def test_get_booking():
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
@allure.story("Get booking by id")
def test_get_booking():
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
    list_bookings = []
    for i in range(5):
        response = APIClient().create_booking(payload)
        id_booking = response.json()['bookingid']
        list_bookings.append(id_booking)
    print(list_bookings)
    firstname = response.json()["booking"]["firstname"]
    lastname = response.json()["booking"]["lastname"]
    params = {
        "firstname": firstname,
        "lastname": lastname
    }
    response = APIClient().get_booking_ids(params)
    response_json = response.json()
    print(response_json)
    APIClient().not_empty_json(response_json)
    APIClient().check_status(200, response)
    for id in list_bookings:
        APIClient().exist_value_in_json('bookingid', id, response_json)
        APIClient().delete_booking(id, credentionals)

@allure.epic('Getting booking')
@allure.feature('Positive')
@allure.story("Get bookings by date")
def test_get_bookings_with_filter_dates():
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