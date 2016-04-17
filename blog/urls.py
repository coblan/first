from django.conf.urls import include, url
import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^index/(\w+)',views.index),
    url(r'^art/(\w+)',views.art),
    url(r'^upload/(\w+)',views.upload_file),
]




