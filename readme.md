Allure report with history on https://elenkafila.github.io/pytest_api_testing/

API tests for http://restful-booker.herokuapp.com/
Apidoc can be found at https://restful-booker.herokuapp.com/apidoc/index.html
This repository contains sets of API smoke tests realized by OOP method.

The following tests have been implemented:
- Validating status codes of basic CRUD http methods
- Validating of specified json data/schemas validation
- Generating of authentication token
- Getting ids of available bookings upon various filters data provided (specified id, firstname & lastname, checkin & checkout)
- Creating new booking
- Updating specified bookings fully and partially
- Deleting specified booking

pytest, requests, faker, pydantic, allure reports, docker, github pages
