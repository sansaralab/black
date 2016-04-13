from django.conf.urls import url
from .views import main, concrete, search

urlpatterns = [
    url(r'^$', main),
    url(r'^concrete', concrete),
    url(r'^search', search)
]
