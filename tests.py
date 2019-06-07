from django.test import SimpleTestCase, TestCase
from django.http import HttpRequest
from django.urls import reverse
from quotium import views

from model_mommy import mommy
from quotium.models import PropertyData
from quotium.utils import post_property_data


class QuoteListViewTests(SimpleTestCase):
    def test_quotelist_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('quote_list'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('quote_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'quotium/quoterecord_list.html')

class CreateSubmissionViewTests(SimpleTestCase):
    def test_create_submission_page_status_Code(self):
        response = self.client.get('/post/new')
        self.assertEqual(response.status_code, 301)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('post_new'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('post_new'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('quotium/propertydata_form.html')

    def test_view_contains(self):
        response = self.client.get(reverse('post_new'))
        self.assertContains(response, '<h1>Property Information</h1>')



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

