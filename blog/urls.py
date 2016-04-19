from django.conf.urls import include, url
import views

urlpatterns = [
    url(r'^$', views.content),
    url(r'^content/(\w+)/(\w*)',views.content,name='blog_content'),
    url(r'^upload/(\w+)',views.upload_file),
]




