from pydantic import BaseModel
from datetime import date


class BadCredentionalsResponse(BaseModel):
    reason: str

class AuthOkResponse(BaseModel):
    token : str

class DatesCheck(BaseModel):
    checkin : date | str
    checkout: date | str

class BookingPerson(BaseModel):
    firstname : str
    lastname : str
    totalprice : int | None
    depositpaid : bool
    bookingdates : DatesCheck
    additionalneeds: str | None=None

class BookingCreate(BaseModel):
    bookingid : int
    booking: BookingPerson
