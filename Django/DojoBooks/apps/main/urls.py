from django.conf.urls import url
from . import views
urlpatterns = [
    # localhost:8000/book/ ??? VVVV
    url(r'^$', views.index),
    # url(r'^book/create$', views.create_book),
    url(r'^(?P<book_id>\d+)$', views.show_book),
    url(r'^(?P<book_id>\d+)/update$', views.update_book),
    url(r'^(?P<book_id>\d+)/delete$', views.delete_book),
]
