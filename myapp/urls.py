from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.home, name="home"),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
]
