from django.urls .conf import path
from .views import myhome

urlpatterns = [
    path('',myhome, name='home')
]
