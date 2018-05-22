# -*- coding: utf-8 -*-
"""
Created on Tue May 15 19:37:36 2018

@author: Unalmed
"""


from netCDF4 import Dataset
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.basemap import Basemap
import datetime
import scipy.stats
import xlsxwriter as xlsxwl # Crear archivos de Excel
import pandas as pd
import scipy.stats as scp
from windrose import WindroseAxes
from datetime import datetime 
import xlrd #para arir archvos de excel


Name= 'C:/Users/Unalmed/Documents/CampoResultados/Perfiles.xlsx'


#------------------------
#se nombran as estaciones
#------------------------

#Se abre el archivo

MisDatos=xlrd.open_workbook(Name)
#for hoja in range(1,4):
    
HojaActual= MisDatos.sheet_by_index(0)
    
    
    #Se extraelacolumna 2  para encontrar indicadores de Enero
X= []
Y= []



   
i=1
while True:
    try:
        X.append(HojaActual.cell(i,1).value)
        Y.append(HojaActual.cell(i,2).value)
        
        i+=1
    except IndexError:
        break
        
X=np.array(X)  
Y=np.array(Y)    

Xmetros=[]
for i in X:
    Xmetros.append(float(i))

Ymetros=[]
for i in Y:
    Ymetros.append(float(i))
    
Xmetros=np.array(Xmetros)  
Ymetros=np.array(Ymetros)     


####PERFILES DE PLAYA#####

#resto nivel de referencia

altura=Ymetros-1.41

plt.plot(Xmetros, altura)
axes = plt.gca()
#axes.set_xlim([1,12])
axes.set_ylim([-5,5])

    