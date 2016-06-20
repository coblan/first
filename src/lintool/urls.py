from django.conf.urls import include, url
import views,login
import myadmin
urlpatterns = [
    url(r'^login/$', login.login_view,name='login'),
    url(r'^registe/$',login.regist_user,name='registe'),
    url(r'^admin/$',myadmin.admin),
    url(r'^test/',views.test),
    url(r'^testloop',views.test_loopwork),
]