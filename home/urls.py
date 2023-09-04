from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('profile', myprofile, name="myprofile"),
    path('/transactions/', transactions, name='transactions'),
    path('/running/', running, name='running'),
    path('/notifications/', notifs, name='notifications'),
    path('/edit/', edit, name='edit')
]
