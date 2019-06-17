from django.conf.urls import url
from . import views

urlpatterns = [
    # localhost:8000 => views.index
    url(r'^$', views.index)
]