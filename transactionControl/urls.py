from django.urls import path
from .views import *

urlpatterns = [
    path('admin', adminView, name='admin'),
    path('pair', pairing, name='pair'),
    path('resetPairs', clearPairs, name='resetPairs')
]
