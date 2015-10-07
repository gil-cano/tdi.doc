from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.talk_template_list),
    # url(r'(?P<pk>\d+)/$', views.talk_details),
    url(r'(?P<pk>\d+)/$', views.track_details),
]
