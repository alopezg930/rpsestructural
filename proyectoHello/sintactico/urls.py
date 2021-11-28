from django.urls import path
from .views import principal

app_name = 'sintactico'

urlpatterns = [
    path("estructuralRP/", principal, name="patrones")
]