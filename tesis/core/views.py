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
    coquimbo=pd.read_table('core/coquimbo.csv', sep=',',decimal=",")
 
    latitud=coquimbo['LATITUD']
    longitud=coquimbo['LONGITUD']

    mylist = zip(latitud.to_list(), longitud.to_list())

    context={ 'cord': mylist}

    return render(request, 'prueba_dos.html',context )