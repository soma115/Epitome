from django.conf.urls import url
from Propylaea import views

urlpatterns = [
    #~ url(r'^$', views.UserIndex, name='index'),
    url(r'^signup', views.sign_up_v, name='signup'),
    url(r'^login', views.log_in, name='login')
]
