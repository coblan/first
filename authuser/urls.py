from django.conf.urls import include, url
import views
urlpatterns = [
    url(r'^login/',views.login),
    url(r'regist/',views.regist_user,name='regist')
    
]