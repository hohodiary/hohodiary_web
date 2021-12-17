from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User

# Create your views here.
def blogin(request):
    return render(request, 'accountapp/blogin.html')

class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:blogin')
    template_name = 'accountapp/create.html'
