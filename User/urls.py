from django.conf.urls import url
from User import views


urlpatterns = [

    url('/login', views.UserLogin.as_view(), name='login'),
    url('/getList', views.Users.as_view(), name='userList'),
    url('/(?P<id>[0-9]+)$', views.UserDetails.as_view(), name='userDetail'),
    url('', views.User.as_view(), name='user'),

]
