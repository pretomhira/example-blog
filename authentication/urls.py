from django.urls import path
from authentication.views import SignupPageView, RegisterView, LoginView

urlpatterns = [
    
    path('signup/', SignupPageView.as_view(), name='signup'),
    path('register',RegisterView.as_view(), name='register_view'),
    path('login', LoginView.as_view()),
]
