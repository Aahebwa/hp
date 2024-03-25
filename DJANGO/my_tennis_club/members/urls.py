from django.urls import path
from . import views

app_name = "cyclone"

urlpatterns = [
    path('', views.main, name="main"),
    path('members/', views.members, name="members"),
    path('testing/' ,views.testing, name="testing"),
    path('signup/', views.signupView, name="signup"),
    path('login/', views.loginView, name="login"),
    path('members/details/<int:id>', views.details, name="details"),
]