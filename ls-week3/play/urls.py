from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('signup',views.signup,name="signup"),
    path('login_',views.login_,name="login_"),
    path('logout_',views.logout_,name="logout_")
]