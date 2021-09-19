from django.test import TestCase
from .models import Quote
from rest_framework.test import APIClient


class QuoteModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Quote.objects.create(quote="Haha", tag="trash")

    def test(self):
        quote = Quote.objects.get(id=1)
        self.assertURLEqual(quote.quote, 'Haha')
        self.assertEqual(quote.tag, 'trash')

    def test_api(self):
        api = APIClient()
        success_code = api.get('/quotes').status_code
        success_code_code_1 = api.get('/quotes/trash').status_code
        error_code = api.get('/quotes/no-trash').status_code
        self.assertEqual(success_code, 200)
        self.assertEqual(success_code_code_1, 200)
        self.assertEqual(error_code, 404)