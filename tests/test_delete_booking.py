from services.api import *
from services.payloads import *
from services.json_schema import *
import pytest
import allure


@allure.epic('Delete booking')
@allure.feature('Positive')
@allure.story('Delete existing booking by id')
def test_delete_booking():

    # 1) Creating new booking
    # 2) Creating new auth token for getting access to DELETE method.
    # 3) Deleting booking by id. Asserting status code is 201
    # 4) Geting booking by id. Asserting that chosen booking was deleted status code is 404
    
    response = APIClient().create_booking(payload_correct_dates)
    APIClient().check_status(200, response)
    id_booking = response.json()['bookingid']
    resp = APIClient().delete_booking(id_booking, credentionals)
    APIClient().check_status(201, resp)
    resp2 = APIClient().get_booking_by_id(id_booking)
    APIClient().check_status(404, resp2)


@allure.epic('Delete booking')
@allure.feature('Negative')
@allure.story('Delete deleted booking')
def test_delete_deleted_booking():
    
    # 1) Creating new booking
    # 2) Creating new auth token for getting access to DELETE method.
    # 3) Deleting booking by id. Asserting status code is 201
    # 4) Geting booking by id. Asserting that chosen booking was deleted status code is 404
    # 5) Deleting booking by id. Asserting status code is 405

    response = APIClient().create_booking(payload_correct_dates)
    id_booking = response.json()['bookingid']
    resp = APIClient().delete_booking(id_booking, credentionals)
    APIClient().check_status(201, resp)
    resp2 = APIClient().get_booking_by_id(id_booking)
    APIClient().check_status(404, resp2)
    resp3 = APIClient().delete_booking(id_booking, credentionals)
    APIClient().check_status(405, resp3)