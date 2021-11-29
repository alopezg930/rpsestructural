# from django.http.response import HttpResponse
from django.shortcuts import render
from .models import distancia, tessiu
# from .forms import registraDistancias

import numpy as np

# Create your views here.
def myhome(request):
    
    list = tessiu.objects.get_queryset()                
            
    template_name = 'home/home.html'
    diccionario = {'lista':list}
    return render(request, template_name, diccionario)
    
def comparaDatos(request):
    umbral = int(request.POST['txtUmbral'])

    list = tessiu.objects.get_queryset()
    datos, dat= obtenDistancias(list, umbral)
    
    template_name = 'home/reporte.html'
    diccionario = {'dist':datos, "umbral":umbral, 'distancias':dat}
    return render(request, template_name, diccionario)

def obtenDistancias(list, umbral):
    indiceA = 0
    distanciass = [[],[],[],[]]
    distancias = []
    
    for a in list:
        
        indiceA+=1
        indiceB = 0
        for b in list:
            datos = []
            indiceB+=1
            if(indiceA<=indiceB):
                distancia = round(np.sqrt(((a.temperature-b.temperature)**2)+((a.color-b.color)**2)+((a.inflammation-b.inflammation)**2)),2)
                
                distanciass[0].append(indiceA)
                distanciass[1].append(indiceB)
                distanciass[2].append(distancia)
                datos.append(indiceA)
                datos.append(indiceB)
                datos.append(distancia)
                
                if(distancia<=umbral):
                    distanciass[3].append("si")
                    datos.append("si")
                else:
                    distanciass[3].append("no")
                    datos.append("no")
                    
            distancias.append(datos)
                
    return distanciass, distancias