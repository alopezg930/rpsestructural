# from django.http.response import HttpResponse
from django.shortcuts import render
from .models import tessiu
from .forms import registraDistancias

import numpy as np

# Create your views here.
def myhome(request):
    
    list = tessiu.objects.get_queryset()
    indiceA = 0
    r1 = []
    r2 = []
    distancias = []
    # distancias = [[],[],[]]
    
    for a in list:
        indiceA+=1
        indiceB = 0
        for b in list:
            indiceB+=1
            if(indiceA<=indiceB):
                distancia = round(np.sqrt(((a.temperature-b.temperature)**2)+((a.color-b.color)**2)+((a.inflammation-b.inflammation)**2)),2)
                r1.append(indiceA)
                r2.append(indiceB)
                distancias.append(distancia)
                # distancias[0].append(indiceA)
                # distancias[1].append(indiceB)
                # distancias[2].append(distancia)
                
            
    template_name = 'home/home.html'
    return render(request, template_name, {'lista':list, 'distancias':distancias, 'r1':r1, 'r2':r2})
    