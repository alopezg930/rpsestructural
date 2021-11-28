from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def about(request):
    # return HttpResponse("<h1>hola about</h1>")
    
    template_name = 'about/about.html'
    
    return render(request, template_name, {"nombreUsuario":miFuncion(request), "edad":24})
    
def miFuncion(args):
    # return 'osvaldo'
    return "osvaldo lg"