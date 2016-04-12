from django.conf.urls import url, include
from .views import main

urlpatterns = [
    url(r'^$', main)
]
