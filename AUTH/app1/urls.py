from django.urls import path
from .views import signupView,loginView,homeView,logutView




urlpatterns=[

    path('signup/', signupView, name='signupview'),
    path('login/', loginView, name='loginview'),
    path('home/', homeView, name='homeview'),
    path('logout/', logutView, name='logoutview')



]