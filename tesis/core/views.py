import pandas as pd

from django.shortcuts import render

# Create your views here.

def inicio(request):
    return render(request, 'modulos/inicio.html')

def tabla(request):
    documento=pd.read_table('core/20200925_Directorio_Oficial_EE_2020_20200430_WEB.csv', sep=';')
    coquimbo=documento[documento['COD_REG_RBD']==4]
    latitud=coquimbo['LATITUD']
    longitud=coquimbo['LONGITUD']

    return render(request, 'prueba.html', context={'lat':latitud.to_list(), 'lon':longitud.to_list()})

def tabla_dos(request):
    documento=pd.read_table('core/20200925_Directorio_Oficial_EE_2020_20200430_WEB.csv', sep=';')
    coquimbo=documento[documento['COD_REG_RBD']==4]
    latitud=coquimbo['LATITUD'].dropna()
    longitud=coquimbo['LONGITUD'].dropna()
    lat=pd.to_numeric(lat,owncast='float')
    
    return render(request, 'prueba_dos.html', context={ 'cord': {'lat':lat.to_list(), 'lon':longitud.to_list()}})