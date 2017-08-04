from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^quotes/$',
        views.QuoteListView.as_view(),
        name='quotes'),
    url(r'^quotes/random/$',
        views.random_quote_detail,
        name='random_quote'),
]
