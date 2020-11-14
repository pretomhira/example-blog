from django.urls import path
from authentication.views import login, register,SignupPageView

urlpatterns = [
    path('login/', login),
    path('register/', register),
    path('signup/', SignupPageView.as_view(), name='signup'),
]
