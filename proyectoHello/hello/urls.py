from django.urls .conf import path
from .views import myhome, comparaDatos

app_name = 'inicio'

urlpatterns = [
    path('',myhome, name='home'),
    path("compara/", comparaDatos, name="compara")
]
