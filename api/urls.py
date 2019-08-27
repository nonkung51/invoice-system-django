from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import UserProfileView
from .auth_views import create_user


urlpatterns = [
    path("register/", create_user),
    path("profile/", UserProfileView.as_view()),
    path("login/", obtain_auth_token),
]
