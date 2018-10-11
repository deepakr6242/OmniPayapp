from django.conf.urls import url,include
from . import views
from django.contrib.auth.views import login,logout

urlpatterns=[

  
   url(r'^$',views.hello, name='hello'),]