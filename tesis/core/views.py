import pandas as pd

import numpy as np
from django.shortcuts import render

# Create your views here.

def inicio(request):
    return render(request, 'modulos/inicio.html')

def tabla(request):
    documento=pd.read_table('core/20200925_Directorio_Oficial_EE_2020_20200430_WEB.csv', sep=';')
    coquimbo=documento[documento['COD_REG_RBD']==4]

    variable=documento.replace(' ', np.nan)
    variable=variable.dropna()

    latitud=variable['LATITUD']
    longitud=variable['LONGITUD']

    mylist = zip(latitud.to_list(), longitud.to_list())

    context={ 'cord': mylist}


    return render(request, 'prueba.html', context)

def tabla_dos(request):
    
    coquimbo=pd.read_table('core/coquimbo.csv', sep=',',decimal=",")

    exceso_oferta=pd.read_table('core/EXC_OFERTA.csv', sep=';', decimal=".")
 
    total=exceso_oferta[exceso_oferta['EXC_OFERTA']=='100%']


    coquimbo['check']=coquimbo.RBD.isin(exceso_oferta.rbd)
    procesados=coquimbo[coquimbo['check']]

    latitud=procesados['LATITUD']
    longitud=procesados['LONGITUD']
    
    mylist = zip(latitud.to_list(), longitud.to_list())

    context={ 'cord': mylist}

    return render(request, 'modulos/prueba_dos.html',context )