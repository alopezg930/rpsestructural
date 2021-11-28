from .models import tessiu
# from .models import tessiu
from django.contrib.auth.forms import UserCreationForm

class registraDistancias(UserCreationForm):
    class Meta:
        moder = tessiu
        fields = [
                'r1',
                'r2',
                'distancia',
        ]
        labels = {
            'r1': 'patron 1',
            'r2': 'patron 2',
            'distancia': 'distancia',
        }