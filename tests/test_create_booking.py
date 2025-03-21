from services.api import *
from services.payloads import *
from services.json_schema import *
import pytest
import allure


@allure.epic("Create booking")
@allure.feature('Positive')
@allure.story('Test correct dates')
@pytest.mark.parametrize(
    "payload, model, status",
    [
        (payload_correct_dates, BookingCreate, 200),
        (payload_correct_today_dates, BookingCreate, 200),
    ], ids= ["Correct dates",
             "Correct dates on today"]
)
def test_correct_dates_create_booking(payload, model, status):
    
    # 1) Creating booking with correct payload
    # 2) Asserting status code is 200
    # 3) Checking values in payloads and response
    # 4) Validating response's JSON schema
    # 5) Deleting booking by id
    

    response = APIClient().create_booking(payload)
    APIClient().check_status(status, response)
    if response.status_code != 500:
        response_json = response.json()
        APIClient().check_value(payload["firstname"], response.json()["booking"]["firstname"])
        APIClient().check_value(payload["lastname"], response.json()["booking"]["lastname"])
        APIClient().check_value(payload["bookingdates"]["checkin"], response.json()["booking"]["bookingdates"]["checkin"])
        APIClient().check_value(payload["bookingdates"]["checkout"], response.json()["booking"]["bookingdates"]["checkout"])
        
        APIClient().validate_json_schema(model, response.json())

        id_booking = response_json['bookingid']
        APIClient().delete_booking(id_booking, credentionals)


@allure.epic("Create booking")
@allure.feature('Negative')
@allure.story('Test incorrect dates')
@pytest.mark.parametrize(
    "payload, model, status",
    [   (payload_past_dates, BookingCreate, 200),
        (payload_empty_dates, BookingCreate, 200),
        (payload_one_empty_date, BookingCreate, 200),
        (payload_wrong_dates, BookingCreate, 200),
        (payload_incorrect_without_dates, BookingCreate, 500),
    ], ids= ["Past dates",
             "Empty dates",
             "Empty one day",
             "Wrong dates 'checkin>checkout'",
             "Payload without dates"]
)
def test_incorrect_dates_create_booking(payload, model, status):

    # 1) Creating booking with incorrect payload
    # 2) Asserting status codes
    # 3) Checking values in payloads and response. If payloads dates empty, response dates are "0NaN-aN-aN"
    # 4) Validating response's JSON schema
    # 5) Deleting booking by id


    response = APIClient().create_booking(payload)
    APIClient().check_status(status, response)
    if response.status_code != 500:
        response_json = response.json()
        APIClient().check_value(payload["firstname"], response.json()["booking"]["firstname"])
        APIClient().check_value(payload["lastname"], response.json()["booking"]["lastname"])
        if payload["bookingdates"]["checkin"] == '':
            print("1")
            APIClient().check_value("0NaN-aN-aN", response.json()["booking"]["bookingdates"]["checkin"])
            if payload["bookingdates"]["checkout"]=='':
                APIClient().check_value("0NaN-aN-aN", response.json()["booking"]["bookingdates"]["checkout"])
            else:
                print("1")
                APIClient().check_value(payload["bookingdates"]["checkout"], response.json()["booking"]["bookingdates"]["checkout"])
        elif payload["bookingdates"]["checkout"]=='' :
            print("2")
            APIClient().check_value("0NaN-aN-aN", response.json()["booking"]["bookingdates"]["checkout"])
            if payload["bookingdates"]["checkin"]=='':
                APIClient().check_value("0NaN-aN-aN", response.json()["booking"]["bookingdates"]["checkin"])
            else:
                print("2")
                APIClient().check_value(payload["bookingdates"]["checkin"], response.json()["booking"]["bookingdates"]["checkin"]) 
        else:           
            print("3")  
            APIClient().check_value(payload["bookingdates"]["checkin"], response.json()["booking"]["bookingdates"]["checkin"])
            APIClient().check_value(payload["bookingdates"]["checkout"], response.json()["booking"]["bookingdates"]["checkout"])
        
        APIClient().validate_json_schema(model, response.json())

        id_booking = response_json['bookingid']
        APIClient().delete_booking(id_booking, credentionals)



@allure.epic("Create booking")
@allure.feature('Negative')
@allure.story('Test incorrect payloads')
@pytest.mark.parametrize(
    "payload, model, status",
    [
        (empty_payload, BookingCreate, 200),
        (all_empty_payload, BookingCreate, 500),
        (payload_incorrect_data_types, BookingCreate, 500)
    ], ids= ["Empty payload",
             "Without payload",
             "Payload incorrect data types"]
)
def test_incorrect_payloads_create_booking(payload, model, status):
    
    # 1) Creating booking with incorrect payload
    # 2) Asserting status codes
    # 3) Checking values in payloads and response. If payloads dates empty, response dates are "0NaN-aN-aN"
    # 4) Validating response's JSON schema
    # 5) Deleting booking by id
    
    response = APIClient().create_booking(payload)
    APIClient().check_status(status, response)
    if response.status_code != 500:
        response_json = response.json()
        APIClient().check_value(payload["firstname"], response.json()["booking"]["firstname"])
        APIClient().check_value(payload["lastname"], response.json()["booking"]["lastname"])
        # check existing field 'additionalneeds' in sending payload 
        if "additionalneeds" in payload:
                APIClient().check_value(payload["additionalneeds"], response.json()["booking"]["additionalneeds"])   
                     
        APIClient().validate_json_schema(model, response.json())

        id_booking = response_json['bookingid']
        APIClient().delete_booking(id_booking, credentionals)

@allure.epic("Create booking")
@allure.feature('Positive')
@allure.story('Test additionalneeds in payloads')
@pytest.mark.parametrize(
    "payload, model, status",
    [
        (payload_without_additionals, BookingCreate, 200),
        (payload_with_2_additionals, BookingCreate, 200),
        (payload_with_long_additionals, BookingCreate, 200)
    ], ids= ["Payload without additionals",
             "Payload with 2 additionals",
             "Payload with long additionals"]
)
def test_payloads_additional_create_booking(payload, model, status):
    
    # 1) Creating booking with correct payload
    # 2) Asserting status codes
    # 3) Checking values in additionalneeds.
    # 4) Validating response's JSON schema
    # 5) Deleting booking by id
 
    response = APIClient().create_booking(payload)
    APIClient().check_status(status, response)
    if response.status_code != 500:
        response_json = response.json()
        APIClient().check_value(payload["firstname"], response.json()["booking"]["firstname"])
        APIClient().check_value(payload["lastname"], response.json()["booking"]["lastname"])
        # check existing field 'additionalneeds' in sending payload 
        if "additionalneeds" in payload:
                APIClient().check_value(payload["additionalneeds"], response.json()["booking"]["additionalneeds"])                
        APIClient().validate_json_schema(model, response.json())

        id_booking = response_json['bookingid']
        APIClient().delete_booking(id_booking, credentionals)