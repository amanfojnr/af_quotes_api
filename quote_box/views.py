from django.shortcuts import render
from rest_framework import generics
from rest_framework.renderers import JSONRenderer
from .serializers import QuoteSerializer
from .models import Quote
from random import randrange
from django.http import HttpResponse

# Create your views here.


def quote_list(request, limit=263):
    """
    API endpoint that lists all quotes or a specific number of
    quotes

    limit --  the number of quotes to be returned
    """
    quotes = Quote.objects.all()[:int(limit)]
    serializer = QuoteSerializer(quotes, many=True)
    response = HttpResponse(JSONRenderer().render(serializer.data),
                            content_type='application/json')
    response["Access-Control-Allow-Origin"] = "*"
    return response


def random_quote_detail(request):
    """
    API endpoint that generates a random quote
    """
    quote = Quote.objects.get(id=randrange(1, 264))
    serializer = QuoteSerializer(quote)
    response = HttpResponse(JSONRenderer().render(serializer.data),
                            content_type='application/json')
    response["Access-Control-Allow-Origin"] = "*"
    return response


def index(request):
    return render(request,
                  "quote_box/index.html")
