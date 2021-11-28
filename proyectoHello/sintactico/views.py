from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

def principal(request):
    template_name = 'sintactico/sintactico.html'
    
    return render(request, template_name, {})