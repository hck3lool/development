from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'(?P<id_request_json>\d+)/$', views.compare_rest, name='compare_rest'),
    url(r'(?P<id_request_json>\d+)/(?P<side>right|left)/$', views.json_rest, name='json_rest'),
]
