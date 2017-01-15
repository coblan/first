"""first URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from pagebuilder import views
from hello import views as hello_view

#import index

urlpatterns = [
    
    url(r'^accounts/',include('authuser.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^share/',include('share.urls')),
    url(r'^blog/',include('blog.urls')),
    #url(r'hello/','hello.views.hello'),
    url(r'^$','hello.views.hello'),
    url(r'^talk/','hello.views.talk'),
    
    url(r'^build/','pagebuilder.views.build'),
    url(r'^pagebuilder/','pagebuilder.views.pagebuild'),
    url(r'^mbpage/$',views.mobile_page),
    url(r'^mbpage/(?P<step>.*)/$',views.mobile_page,name='mbpage'),
    url(r'^upload_image_demo/$','hello.views.upload_image_demo'),
    url(r'ajax_error',hello_view.test_ajax_error),
    url(r'norm_try/?$',hello_view.normal_try),
    url(r'chat/',include('talk.urls')),
]


from django.conf import settings
from django.conf.urls.static import static

if getattr(settings,'ROUT_MEDIA',None):
    urlpatterns = urlpatterns+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)