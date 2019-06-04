import json
import requests

from django.conf import settings


def post_property_data(property_data):
    request_data = {
        'email': property_data.email,
        'property_address': property_data.property_address,
        'zip_code': property_data.zip_code,
        'number_bedrooms': property_data.number_bedrooms,
        'number_bathrooms': property_data.number_bathrooms,
        'square_footage': property_data.square_footage
    }
    response = requests.post(settings.QUOTE_API_URL+"submit",
                             data=json.dumps(request_data),
                             headers={'content-type': 'application/json'})
    response.raise_for_status()
    return response.json()['estimate']

