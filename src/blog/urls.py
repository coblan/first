from django.conf.urls import include, url
import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^index/(\w+)/$',views.index,name='blog_content'),
    url(r'^article/(\w+)/$',views.article),
    url(r'^tag/(\w+)/$',views.tag_view),
    url(r'^upload/(\w+)',views.upload_file),
]




