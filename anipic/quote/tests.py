from django.test import TestCase
from .models import Quote


class QuoteModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Quote.objects.create(quote="Haha", tag="trash")

    def test(self):
        quote = Quote.objects.get(id=1)
        self.assertURLEqual(quote.quote, 'Haha')
        self.assertEqual(quote.tag, 'trash')

    def test_api(self):
        pass