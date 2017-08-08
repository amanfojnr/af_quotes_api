from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^quotes/list/$',
        views.quote_list,
        name='quotes'),
    url(r'^quotes/list/(?P<limit>\d+)',
        views.quote_list,
        name='quotes-limit'),
    url(r'^quotes/random/$',
        views.random_quote_detail,
        name='random_quote'),
]
