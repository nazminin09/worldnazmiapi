from django.urls import path, re_path
from . import views

urlpatterns = [
    # path('', views.get_country_details),
    # path('country/', views.get_country_details),
    re_path(r'country/(?P<country_name>[\w|\W]+)$', views.get_country_details, name="country_page"),
    
]