from django.conf.urls import include, url
import views

urlpatterns = [
    url(r'^$',views.home),
    url(r'^room/(?P<room>\w+)/?$',views.talk_page),
    url(r'^ajax/?$',views.ajax_port,name='talk_ajax'),
    ]