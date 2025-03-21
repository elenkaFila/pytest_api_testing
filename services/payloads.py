from faker import Faker
from datetime import datetime, timedelta
import allure


fake = Faker()
date_today = datetime.today().strftime('%Y-%m-%d')
past_date_start = (fake.past_date()- timedelta(days=150)).strftime('%Y-%m-%d')
past_date_end = (fake.past_date()).strftime('%Y-%m-%d')
future_date_start = (fake.future_date()).strftime('%Y-%m-%d')
future_date_end = (fake.future_date() + timedelta(days=10)).strftime('%Y-%m-%d')

credentionals = {
    "username" : "admin",
    "password" : "password123",
    "timeout": 10
}

wrong_credentionals = {
    "username" : "admin",
    "password" : "mypassword123",
    "timeout": 10
}

empty_credentionals = {
    "username" : "",
    "password" : "",
    "timeout": 10
}


def generate_dates_today():
    dates = {
            "checkin" : date_today,
            "checkout" : date_today
        }
    return dates


def generate_empty_dates():
    dates = {
            "checkin" : "",
            "checkout" : ""
        }
    return dates


def generate_one_empty_date():
    dates = {
            "checkin" : "",
            "checkout" : future_date_end
        }
    return dates

def generate_dates():
    dates = {
            "checkin" : future_date_start,
            "checkout" : future_date_end
        }
    return dates


def generate_past_dates():
    dates = {
            "checkin" : past_date_start,
            "checkout" : past_date_end
        }
    return dates


def generate_wrong_dates():
    dates = {
            "checkin" : future_date_start,
            "checkout" : past_date_end
        }
    return dates


def get_data(dates):

    booking_data = { 
        "firstname" : fake.first_name(),
        "lastname" : fake.last_name(),
        "totalprice" : fake.random_int(min=100, max=999),
        "depositpaid" : fake.boolean(),
        "bookingdates" : dates,
        "additionalneeds" : "Breakfast"
        }
    return booking_data



payload_correct_dates = get_data(generate_dates())
payload_correct_today_dates = get_data(generate_dates_today())
payload_past_dates = get_data(generate_past_dates())
payload_empty_dates = get_data(generate_empty_dates())
payload_wrong_dates = get_data(generate_wrong_dates())
payload_one_empty_date = get_data(generate_one_empty_date())

payload_incorrect_without_dates = { 
        "firstname" : fake.first_name(),
        "lastname" : fake.last_name(),
        "totalprice" : fake.random_int(min=100, max=999),
        "depositpaid" : fake.boolean(),
        "additionalneeds" : "Breakfast"
}

empty_payload = { 
        "firstname" : "",
        "lastname" : "",
        "totalprice" : "",
        "depositpaid" : "",
        "bookingdates" : generate_empty_dates(),
        "additionalneeds" : ""
}
all_empty_payload = { 
     }

payload_without_additionals = { 
        "firstname" : fake.first_name(),
        "lastname" : fake.last_name(),
        "totalprice" : fake.random_int(min=100, max=999),
        "depositpaid" : fake.boolean(),
        "bookingdates" : generate_dates()
        }

payload_with_2_additionals = { 
        "firstname" : fake.first_name(),
        "lastname" : fake.last_name(),
        "totalprice" : fake.random_int(min=100, max=999),
        "depositpaid" : fake.boolean(),
        "bookingdates" : generate_dates(),
        "additionalneeds" : "breakfast, pool"
        }

payload_with_long_additionals = { 
        "firstname" : fake.first_name(),
        "lastname" : fake.last_name(),
        "totalprice" : fake.random_int(min=100, max=999),
        "depositpaid" : fake.boolean(),
        "bookingdates" : generate_dates(),
        "additionalneeds" : "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim. Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus. Phasellus viverra nulla ut metus varius laoreet. Quisque rutrum. Aenean imperdiet. Etiam ultricies nisi vel augue. Curabitur ullamcorper ultricies nisi. Nam eget dui. Etiam rhoncus. Maecenas tempus, tellus eget condimentum rhoncus, sem quam semper libero, sit amet adipiscing sem neque sed ipsum. Nam quam nunc, blandit vel, luctus pulvinar, hendrerit id, lorem. Maecenas nec odio et ante tincidunt tempus. Donec vitae sapien ut libero venenatis faucibus. Nullam quis ante. Etiam sit amet orci eget eros faucibus tincidunt. Duis leo. Sed fringilla mauris sit amet nibh. Donec sodales sagittis magna. Sed consequat, leo eget bibendum sodales, augue velit cursus nunc, quis gravida magna mi a libero. Fusce vulputate eleifend sapien. Vestibulum purus quam, scelerisque ut, mollis sed, nonummy id, metus. Nullam accumsan lorem in dui. Cras ultricies mi eu turpis hendrerit fringilla. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; In ac dui quis mi consectetuer lacinia. Nam pretium turpis et arcu. Duis arcu tortor, suscipit eget, imperdiet nec, imperdiet iaculis, ipsum. Sed aliquam ultrices mauris. Integer ante arcu, accumsan a, consectetuer eget, posuere ut, mauris. Praesent adipiscing. Phasellus ullamcorper ipsum rutrum nunc. Nunc nonummy metus. Vestibulum volutpat pretium libero. Cras id dui. Aenean ut eros et nisl sagittis vestibulum. Nullam nulla eros, ultricies sit amet, nonummy id, imperdiet feugiat, pede. Sed lectus. Donec mollis hendrerit risus. Phasellus nec sem in justo pellentesque facilisis. Etiam imperdiet imperdiet orci. Nunc nec neque. Phasellus leo dolor, tempus non, auctor et, hendrerit quis, nisi. Curabitur ligula sapien, tincidunt non, euismod vitae, posuere imperdiet, leo. Maecenas malesuada. Praesent congue erat at massa. Sed cursus turpis vitae tortor. Donec posuere vulputate arcu. Phasellus accumsan cursus velit. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Sed aliquam, nisi quis porttitor congue, elit erat euismod orci, ac placerat dolor lectus quis orci. Phasellus consectetuer vestibulum elit. Aenean tellus metus, bibendum sed, posuere ac, mattis non, nunc. Vestibulum fringilla pede sit amet augue. In turpis. Pellentesque posuere. Praesent turpis. Aenean posuere, tortor sed cursus feugiat, nunc augue blandit nunc, eu sollicitudin urna dolor sagittis lacus. Donec elit libero, sodales nec, volutpat a, suscipit non, turpis. Nullam sagittis. Suspendisse pulvinar, augue ac venenatis condimentum, sem libero volutpat nibh, nec pellentesque velit pede quis nunc. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Fusce id purus. Ut varius tincidunt libero. Phasellus dolor. Maecenas vestibulum mollis diam. Pellentesque ut neque. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. In dui magna, posuere eget, vestibulum et, tempor auctor, justo. In ac felis quis tortor malesuada pretium. Pellentesque auctor neque nec urna. Proin sapien ipsum, porta a, auctor quis, euismod ut, mi. Aenean viverra rhoncus pede. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Ut non enim eleifend felis pretium feugiat. Vivamus quis mi. Phasellus a est. Phasellus magna. In hac habitasse platea dictumst. Curabitur at lacus ac velit ornare lobortis. Curabitur a felis in nunc fringilla tristique. Morbi mattis ullamcorper velit. Phasellus gravida semper nisi. Nullam vel sem. Pellentesque libero tortor, tincidunt et, tincidunt eget, semper nec, quam. Sed hendrerit. Morbi ac felis. Nunc egestas, augue at pellentesque laoreet, felis eros vehicula leo, at malesuada velit leo quis pede. Donec interdum, metus et hendrerit aliquet, dolor diam sagittis ligula, eget egestas libero turpis vel mi. Nunc nulla. Fusce risus nisl, viverra et, tempor et, pretium in, sapien. Donec venenatis vulputate lorem. Morbi nec metus. Phasellus blandit leo ut odio. Maecenas ullamcorper, dui et placerat feugiat, eros pede varius nisi, condimentum viverra felis nunc et lorem. Sed magna purus, fermentum eu, tincidunt eu, varius ut, felis. In auctor lobortis lacus. Quisque libero metus, condimentum nec, tempor a, commodo mollis, magna. Vestibulum ullamcorper mauris at ligula. Fusce fermentum. Nullam cursus lacinia erat. Praesent blandit laoreet nibh. Fusce convallis metus id felis luctus adipiscing. Pellentesque egestas, neque sit amet convallis pulvinar, justo nulla eleifend augue, ac auctor orci leo non est. Quisque id mi. Ut tincidunt tincidunt erat. Etiam feugiat lorem non metus. Vestibulum dapibus nunc ac augue. Curabitur vestibulum aliquam leo. Praesent egestas neque eu enim. In hac habitasse platea dictumst. Fusce a quam. Etiam ut purus mattis mauris sodales aliquam. Curabitur nisi. Quisque malesuada placerat nisl. Nam ipsum risus, rutrum vitae, vestibulum eu, molestie vel, lacus. Sed augue ipsum, egestas nec, vestibulum et, malesuada adipiscing, dui. Vestibulum facilisis, purus nec pulvinar iaculis, ligula mi congue nunc, vitae euismod ligula urna in dolor. Mauris sollicitudin fermentum libero. Praesent nonummy mi in odio. Nunc interdum lacus sit amet orci. Vestibulum rutrum, mi nec elementum vehicula, eros quam gravida nisl, id fringilla neque ante vel mi. Morbi mollis tellus ac sapien. Phasellus volutpat, metus eget egestas mollis, lacus lacus blandit dui, id egestas quam mauris ut lacus. Fusce vel dui. Sed"
        }


payload_incorrect_data_types = {
        "firstname" : 23,
        "lastname" : 25,
        "totalprice" : "",
        "depositpaid" : "",
        "bookingdates" : generate_dates(),
        "additionalneeds" : ""
}


payload_without_additionalneeds = {
        "firstname" : fake.first_name(),
        "lastname" : fake.last_name(),
        "totalprice" : fake.random_int(min=100, max=999),
        "depositpaid" : fake.boolean(),
        "bookingdates" : generate_dates()
        }