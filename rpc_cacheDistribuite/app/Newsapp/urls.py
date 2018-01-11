from django.conf.urls import include, url
from app.Newsapp.views import index

urlpatterns = [
    url(r'^$', index),
]
