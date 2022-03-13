from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import City, Country, Countrylanguage
from rest_framework.response import Response
from restapi.serializers import CountrySerializer
# Create your views here.
@api_view(['GET'])
def get_country_details(request, country_name):
    country = Country.objects.get(name=country_name)
    result = {"country": country}
    
    return render(request, "country.html", result)
    # country_serializer = CountrySerializer(result, many=True)
    # return JsonResponse(country_serializer.data, safe=False)
