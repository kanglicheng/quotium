from django.test import TestCase


from model_mommy import mommy
from blog.models import PropertyData
from blog.utils import post_property_data


class APITestCase(TestCase):
    def test_call_api_with_data(self):
        test_property_data = mommy.prepare(
            PropertyData,
            email='tester@email.com',
            property_address='155 test drive',
            zip_code='03784',
            number_bedrooms=5,
            number_bathrooms=3,
            square_footage=1000
        )
        estimate = post_property_data(test_property_data)
        self.assertEqual(estimate, 5973)

