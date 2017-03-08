from django.conf.urls import include, url
import views

urlpatterns = [
    url(r'^$', views.hello),
    url(r'^jsonpost/$',views.jsonpost)
]