from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.root),
    url(r'^user$', views.index),
    # url(r'^user/create$', views.create_user),
    url(r'^user/(?P<user_id>\d+)$', views.show_user),
    url(r'^user/(?P<user_id>\d+)/update$', views.update_user),
    url(r'^user/(?P<user_id>\d+)/delete$', views.delete_user),
    url(r'^user/(?P<user_id>\d+)/favorite$', views.favorite),
]
