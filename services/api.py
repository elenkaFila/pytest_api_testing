import requests
from services.config import configurations
from services.endpoints import *
import allure
import json
from allure_commons.types import AttachmentType
import pytest

class APIClient:
    def __init__(self, environment='development'):
        self.config = configurations.get(environment, configurations['development'])
        self.base_url = self.config. BASE_URL
        self.timeout = self.config.TIMEOUT
        self.session = requests.Session()

    
    @allure.step("Check status code is 200")
    def check_status_is_200(self, response):
        assert response.status_code == 200, f"Expected status 200 but got {response.status_code}"
        print("Checking expected status code 200")

    @allure.step("Check status code is 201")
    def check_status_is_201(self, response):
        assert response.status_code == 201, f"Expected status 201 but got {response.status_code}"
        print("Checking expected status code 201")

    @allure.step("Check expected status code: {status}")
    def check_status(self, status, response):
        assert status == response.status_code, f"Expected status : {status} but got {response.status_code}"
        print(f"Checking expected status code {status}")

    @allure.step("Check expected value:{payload_value} exist in json response: {json_response}")
    def check_value(self, payload_value, json_response):
        assert payload_value == json_response, f"Expected '{payload_value}' not equal {json_response}"
        print(f"Checking expected value: {payload_value} exist in json response: {json_response}")

    @allure.step("Check expected key: {key} exist in json")
    def exist_key_in_json(self, key):
        assert key, f"Expected '{key}' not exist in json"
        print(f"Checking expected key exist in json")

    @allure.step("Check expected key value: {value} exist in json")
    def exist_value_in_json(self, key, value, response_json):
        assert any(param[key] == value for param in response_json), f"Expected '{value}' not exist in json"
        print(f"Checking expected key value {value} exist in json")

    @allure.step("Check json is not empty")
    def not_empty_json(self, response_json):
        assert len(response_json) > 0, f'{response_json} is empty'
        print(f"Checking json is not empty")    
    
    @allure.step("Check expected json schema")
    def validate_json_schema(self, model,response):
        model(**response)
        print("Checking expected json schema")

    def attach_response_json(self, response):
        response = json.dumps(response, indent=4)
        allure.attach(body=response, name="API Response", attachment_type=AttachmentType.JSON)

    def attach_response(self, response):
        allure.attach(response, name="response content", attachment_type=AttachmentType.JSON)


    def ping(self):
         
        """A simple health check endpoint to confirm whether the API is up and running."""
        
        response = self.session.get(f"{self.base_url}{PING_ENDPOINT}")
        response.raise_for_status()
        self.check_status_is_201(response)

    def authenticate(self, credentionals):

        """Creates a new auth token to use for access to the PUT and DELETE /booking."""
        with allure.step('Send post request with credentionals'):
            response = self.session.post(f"{self.base_url}{AUTH_ENDPOINT}",
                                     json=credentionals,
                                     timeout=self.timeout)
        self.attach_response_json(response.json())
        response.raise_for_status()
        token = response.json().get("token")
        if token != None:
            with allure.step("Update token in cookies"):
                self.session.headers.update({'Cookie': f'token = {token}'})
        return response


    def create_booking(self, booking_data):
        
        """Creates a new booking in the API / Verifies that new booking has been created."""
        with allure.step('Create a new booking in the API'):
            response = self.session.post(f"{self.base_url}{BOOKING_ENDPOINT}",
                                     json=booking_data)
            if response.status_code != 500:
                self.attach_response_json(response.json())
        return response

    def get_booking_ids(self, params=None):

        """Returns the ids of all the bookings that exist within the API."""
        with allure.step('Get all ids of all the bookings'):
            response = self.session.get(f"{self.base_url}{BOOKING_ENDPOINT}", 
                                    params=params)
            response.raise_for_status()
        
        return response

    def get_booking_by_id(self, booking_id):

        """Returns a specific booking based upon the booking id provided / Validates response's json schema."""
        with allure.step('Get booking with id'):
            response = self.session.get(f"{self.base_url}{BOOKING_ENDPOINT}/{booking_id}")
            if response.status_code < 400:
                self.attach_response_json(response.json())       
        return response

    def update_booking(self, booking_id, updated_data, credentionals):

        """Updates a current booking / Verifies the booking has been updated."""



        with allure.step('Update booking with id'):
            response = self.session.put(f"{self.base_url}{BOOKING_ENDPOINT}/{booking_id}", 
                                    json=updated_data, 
                                    headers=self.authenticate(credentionals).json())
            if response.status_code < 400:
                self.attach_response_json(response.json())
        return response

    def patch_booking(self, booking_id, part_of_updated_data, credentionals):

        """Updates a current booking with a partial payload / Verifies the booking has been partially updated."""

        with allure.step('Update booking with partial payload'):
            response = self.session.patch(f"{self.base_url}{BOOKING_ENDPOINT}/{booking_id}", 
                                      json=part_of_updated_data, 
                                      headers=self.authenticate(credentionals).json())
            if response.status_code < 400:
                self.attach_response_json(response.json())
        return response

    def delete_booking(self, booking_id, credentionals):

        """Deletes a specific booking based upon the booking id provided / Verifies booking has been deleted."""
        
        with allure.step('Delete booking with id'):
            response = self.session.delete(f"{self.base_url}{BOOKING_ENDPOINT}/{booking_id}", 
                                       headers=self.authenticate(credentionals).json())
        return response


