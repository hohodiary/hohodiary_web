from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from accountapp.views import blogin, AccountCreateView,main,about

app_name = 'accountapp'

urlpatterns = [
    path('login/', LoginView.as_view(template_name='accountapp/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('blogin/', blogin, name='blogin'),
    path('create/', AccountCreateView.as_view(), name='create'),
    path('main/', main, name='main'),
    path('about/', about, name='about')
]