from django.shortcuts import render
from rest_framework.renderers import JSONRenderer
from .serializers import QuoteSerializer
from .models import Quote
from random import randrange
from django.http import HttpResponse

# Create your views here.


class QuoteListView(generics.ListAPIView):
    """
    API endpoint that generate quotes all quotes
    """
    queryset = Quote.objects.order_by('pk')
    serializer_class = QuoteSerializer


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
