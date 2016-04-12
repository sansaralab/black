from django.conf.urls import url, include
from .views import main, concrete

urlpatterns = [
    url(r'^$', main),
    url(r'^concrete', concrete)
]
