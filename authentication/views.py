from django.http import Http404
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm

class SignupPageView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


# LOGIN VIEW ENDPOINT

def login(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')


