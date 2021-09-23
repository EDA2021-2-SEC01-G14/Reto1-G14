"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """

import config as cf
import time
import sys
import copy
default_limit=1000
sys.setrecursionlimit(default_limit*10)
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as it
from DISClib.Algorithms.Sorting import mergesort as mg
from DISClib.Algorithms.Sorting import quicksort as qs
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newCatalog(option):
    """
    Inicializa el catálogo de libros. Crea una lista vacia para guardar
    todos los libros, adicionalmente, crea una lista vacia para los autores,
    una lista vacia para los generos y una lista vacia para la asociación
    generos y libros. Retorna el catalogo inicializado.
    """
    catalog = {'Artists': None,
               'Artworks': None}

    if option == 1:
        catalog['Artists'] = lt.newList('ARRAY_LIST')
        catalog['Artworks'] = lt.newList('ARRAY_LIST')
        catalog["BeginDate"] = lt.newList("ARRAY_LIST")
        catalog["EndDate"] = lt.newList("ARRAY_LIST")
    
    elif option == 2:
        catalog['Artists'] = lt.newList()
        catalog['Artworks'] = lt.newList()
        catalog["BeginDate"] = lt.newList()
        catalog["EndDate"] = lt.newList()
   
    return catalog

# Funciones para agregar informacion al catalogo

def addArtist(catalog, artist):
    lt.addLast(catalog["Artists"], artist)
    BeginDate=artist["BeginDate"]
    lt.addLast(catalog["BeginDate"],BeginDate)
    EndDate = artist["EndDate"]
    lt.addLast(catalog["EndDate"], EndDate)

def addArtwork(catalog, artwork):
    lt.addLast(catalog["Artworks"], artwork)

# Funciones para creacion de datos

    

# Funciones de consulta

def getArtworksbyDate(catalog, min, max, tamaño, op, option):

    start = time.process_time_ns()
    
    list2 = lt.subList(catalog["Artworks"], 1 , tamaño)
    list2 = list2.copy()
    b=lt.newList("ARRAY_LIST")

    if option == 1:
    
        for byDate in list2["elements"]:

            if byDate["DateAcquired"] != "":
            
                date = int(byDate["DateAcquired"].replace("-",""))

                if date >= min and date <= max:
                    lt.addLast(b, byDate)

    else:

        for i in range(1,(lt.size(list2))+1):

            art=(lt.getElement(list2,i))
            date=art["DateAcquired"]

            if date != "":
                
                    date = int(date.replace('-',''))

                    if date >= min and date <= max:
                        lt.addLast(b, art)
        
        '''print(list2)
        for byDate in list2:

            if byDate not in 'size type key cmpfunction':
                print(byDate)
                print(list2[byDate]['info']["DateAcquired"])
                date=(list2[byDate]['info']["DateAcquired"])

                if date != "":
                
                    date = int(date.replace('-',''))

                    if date >= min and date <= max:
                        lt.addLast(b, date)'''
        

    
    if op == 1:
        it.sort(b, cmpArtworkByDateAcquired)
    elif op == 2:
        sa.sort(b, cmpArtworkByDateAcquired)
    elif op == 3:
        mg.sort(b, cmpArtworkByDateAcquired)
    elif op == 4:
        qs.sort(b, cmpArtworkByDateAcquired)

    stop = time.process_time_ns()

    sgs = (stop-start)/1000000

    
    return b, sgs

#REQU 1

def getArtistBeginDate(catalog, min, max,):

    start = time.process_time_ns()

    list= catalog['Artists'].copy()
    a=lt.newList("ARRAY_LIST")
    
    for artist in list['elements']:
        
        date= int(artist['BeginDate'].replace('-',''))
        
        if date >= min and date <= max:
            lt.addLast(a,artist)

    mg.sort(a, cmpArtistBegindate)


    a1= lt.getElement(a,1)
    a1= 'Nombre: '+ a1['DisplayName'] ,'Año de Nacimiento: '+ a1['BeginDate'],'Genero: '+ a1['Gender'], 'Nacionalidad: '+ a1['Nationality']
    a2= lt.getElement(a,2)
    a2= 'Nombre: '+ a2['DisplayName'], 'Año de Nacimiento: '+a2['BeginDate'],'Genero: '+ a2['Gender'], 'Nacionalidad: '+ a2['Nationality']
    a3= lt.getElement(a,3)
    a3= 'Nombre: '+a3['DisplayName'], 'Año de Nacimiento: '+a3['BeginDate'],'Genero: '+ a3['Gender'], 'Nacionalidad: '+a3['Nationality']
    a4= lt.getElement(a,(lt.size(a) - 2))
    a4= 'Nombre: '+a4['DisplayName'], 'Año de Nacimiento: '+a4['BeginDate'],'Genero: '+ a4['Gender'], 'Nacionalidad: '+ a4['Nationality']
    a5= lt.getElement(a,(lt.size(a) - 1))
    a5= 'Nombre: '+a5['DisplayName'], 'Año de Nacimiento: '+a5['BeginDate'],'Genero: '+ a5['Gender'], 'Nacionalidad: '+ a5['Nationality']
    a6= lt.getElement(a,lt.size(a))
    a6= 'Nombre: '+a6['DisplayName'], 'Año de Nacimiento: '+a6['BeginDate'],'Genero: '+ a6['Gender'], 'Nacionalidad: '+ a6['Nationality']

    stop = time.process_time_ns()

    sgs = (stop-start)/1000000000
    print(sgs)
    return [a,a1,a2,a3,a4,a5,a6]

#REQU 3

def ArtworksbyArtist(catalog,ArtistName):

    start = time.process_time_ns()

    listA = catalog['Artists'].copy()
    ArtistID=''
    x=True
    pos=1
    while x: 

        artist= lt.getElement(listA,pos)
        if ArtistName in artist['DisplayName']:
            ArtistID= artist["ConstituentID"]
            x=False

        pos+=1

    

    listW = catalog['Artworks'].copy()
    a=lt.newList("ARRAY_LIST")
    
    for artworks in listW['elements']:
        
        if ArtistID in artworks['ConstituentID']:
            lt.addLast(a,artworks)


    mg.sort(a,cmpArtworkMedium)

    n_artworks = lt.size(a)


    if n_artworks ==0: 

        stop = time.process_time_ns()

        sgs = (stop-start)/1000000000
        print(sgs)
        return 0

        
    else:
        

        rta=[n_artworks] + ArtwroksMedium(a)

        stop = time.process_time_ns()

        sgs = (stop-start)/1000000000
        print(sgs)  

        return rta



def ArtwroksMedium(list):
    

    Mediums=[lt.getElement(list,1)['Medium']]
    biggest=0
    big_M =lt.getElement(list,1)['Medium']
    count=0

    for artwork in list['elements']:

        if artwork['Medium'] in Mediums: 
            count+=1

        else: 
            Mediums.append(artwork['Medium'])

            if biggest > count:
                biggest = count
                big_M = artwork['Medium']

    return [Mediums, big_M , Artwork_big_M(list,big_M)]

def Artwork_big_M(list,big_M):

    a=lt.newList("ARRAY_LIST")

    for artwork in list['elements']:
        if artwork['Medium'] == big_M:

            lt.addLast(a,artwork)

    return a



#REQU 5



def TransportCos(catalog,depa):
    start = time.process_time_ns()

    listD = ArtbyDepartment(catalog,depa)
    
    Cost=0
    Weight=0
    
    for artwork in listD['elements']:
        costA=48
        Costs=[]
        
        if artwork['Weight (kg)'] != '':
            costW = float(artwork['Weight (kg)']) * 35
            Weight += float(artwork['Weight (kg)'])
        else:
            costW=0
        Costs.append(costW)

        if artwork['Height (cm)'] != '' and artwork['Width (cm)'] != '':
            costm_2 = float(artwork['Height (cm)']) * float(artwork['Width (cm)']) * 35
        else:
            costm_2=0
        Costs.append(costm_2)

        if artwork['Height (cm)'] != '' and artwork['Width (cm)'] != '' and artwork['Depth (cm)'] != '':
            costm_3 = float(artwork['Height (cm)'])/100 * float(artwork['Width (cm)'])/100 * float(artwork['Depth (cm)'] )/100 *35
        else:
            costm_3=0
        Costs.append(costm_3)

        if max(Costs) != 0:
         
            Cost += max(Costs)
            artwork['Cost']=str(round(max(Costs),2)) +' USD'
        else:
            Cost += costA
            artwork['Cost']=str(round(costA,2)) + ' USD'

    #Artworks_Artist(listD,catalog['Artists'])    

    mg.sort(listD,cmpArtworkDate)
    expensive = copy.deepcopy(listD)
    mg.sort(expensive,cmpArtworkCost)

    stop = time.process_time_ns()

    sgs = (stop-start)/1000000000
    print(sgs) 

    return [listD ,Cost , Weight, expensive]

def ArtbyDepartment(catalog,depa):


    listA = catalog['Artworks']
    a=lt.newList("ARRAY_LIST")

    for artwork in listA['elements']:
        if artwork['Department'] == depa:

            lt.addLast(a,artwork)

    return a


def Artworks_Artist(listW,listA):

    for artwork in listW['elements']:
        artwork['Artist']=''

        for artist in listA['elements']:
            if artist['ConstituentID'] in artwork['ConstituentID']:
                artwork['Artist']= artist['DisplayName']

    
        
###############
def getYear(catalog, min, max):

    a=lt.newList()
    b=lt.newList()

    for dateMin in catalog["BeginDate"]:
        if dateMin >= min:
            lt.addLast(a, dateMin)
    
    for dateMax in a:
        if dateMax <= max:
            lt.addLast(b,dateMax)
        

    return b

# Funciones utilizadas para comparar elementos dentro de una lista
def cmpArtworkByDateAcquired(artwork1, artwork2):

    if (artwork1["DateAcquired"]) < (artwork2["DateAcquired"]):
        return True
    else:
        return False

def cmpArtistBegindate(artist1, artist2):

    if (artist1["BeginDate"]) < (artist2["BeginDate"]):
        return True
    else:
        return False

def cmpArtworkMedium(artwork1, artwork2):
    if (artwork1["Medium"]) < (artwork2["Medium"]):
        return True
    else:
        return False

def cmpArtworkDate(artwork1, artwork2):

    if artwork1["Date"] == '':
        artwork1["Date"]='No se sabe'
    if artwork2["Date"] == '':
        artwork2["Date"]='No se sabe'

    if (artwork1["Date"]) < (artwork2["Date"]):
        return True
    else:
        return False

def cmpArtworkCost(artwork1, artwork2):
    if (artwork1["Cost"]) > (artwork2["Cost"]):
        return True
    else:
        return False





# Funciones de ordenamiento

def ordering(op,catalog):

    if op == 1:
        it.sort(catalog["Artworks"], cmpArtworkByDateAcquired)
    elif op == 2:
        sa.sort(catalog["Artworks"], cmpArtworkByDateAcquired)
    elif op == 3:
        mg.sort(catalog["Artworks"], cmpArtworkByDateAcquired)
    elif op == 4:
        qs.sort(catalog["Artworks"], cmpArtworkByDateAcquired)
