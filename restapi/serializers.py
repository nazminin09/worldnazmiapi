from rest_framework import serializers 
from restapi.models import Country
 
 
class CountrySerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Country
        fields = ('lifeexpectancy',
                  'name',
                  'continent',
                  'region')