from django.urls import path
from .views import QuoteList


urlpatterns = [
        path('quotes', QuoteList.as_view(), name='quote', kwargs={'tag': None}),
        path('quotes/<str:tag>', QuoteList.as_view(), name="quote by tag"),
]