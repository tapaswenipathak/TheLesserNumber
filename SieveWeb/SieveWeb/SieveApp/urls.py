from django.conf.urls import url
from django.shortcuts import render
from .views import contact_page

app_name = "SieveApp"
urlpatterns = [
    url(r'^$', contact_page, name='contact'),
]
