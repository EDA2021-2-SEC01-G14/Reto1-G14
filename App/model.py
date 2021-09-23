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

from DISClib.DataStructures.arraylist import newList
import config as cf
import time
import sys
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

def newCatalog():
    """
    Inicializa el catálogo de libros. Crea una lista vacia para guardar
    todos los libros, adicionalmente, crea una lista vacia para los autores,
    una lista vacia para los generos y una lista vacia para la asociación
    generos y libros. Retorna el catalogo inicializado.
    """
    catalog = {'Artists': None,
               'Artworks': None}

    
    catalog['Artists'] = lt.newList('ARRAY_LIST')
    catalog['Artworks'] = lt.newList('ARRAY_LIST')
   
    return catalog


# Funciones para agregar informacion al catalogo

def addArtist(catalog, artist):
    lt.addLast(catalog["Artists"], artist)

def addArtwork(catalog, artwork):
    lt.addLast(catalog["Artworks"], artwork)

# Funciones para creacion de datos


    

# Funciones de consulta

def getArtworksbyDate(catalog, min, max):

    a= catalog["Artworks"]
    resultArtwoks = lt.newList('ARRAY_LIST')

    for byDate in a["elements"]:
        if byDate["DateAcquired"]!= "":
            date = int(byDate["DateAcquired"].replace("-",""))
            
            if date >= min and date<= max:
                lt.addLast(resultArtwoks, byDate)

    mg.sort(resultArtwoks,cmpArtworkByDateAcquired)
    
    return resultArtwoks

def purchase(gd):

    count=0
    a=gd["elements"]

    for purch in a:
        
        b= purch["CreditLine"]
    
        if "purchase" in b.lower():
            count += 1

    return count
    
def top10byNacionality(catalog):

    mg.sort(catalog["Artists"],cmpIDObject)
    mg.sort(catalog["Artworks"],cmpIDObject)
    i=0
    tamaño1=lt.size(catalog["Artworks"])
    tamaño2=lt.size(catalog["Artists"])
    if tamaño1>tamaño2:
        tamaño=tamaño2
    else: 
        tamaño=tamaño1
    
    top10=lt.newList("ARRAY_LIST")

    while i < tamaño:
        b=[]
        b.append(catalog["Artists"]["elements"][i])
        b.append(catalog["Artworks"]["elements"][i])
        lt.addLast(top10,b)
        i+=1

    a=0
    dicc={}
    while a < tamaño:
        
        if top10["elements"][a][0]['Nationality'] != "":
            if top10["elements"][a][0]['Nationality'] in dicc.keys():
                x= dicc[top10["elements"][a][0]['Nationality']]
                x+=1
                dicc[top10["elements"][a][0]['Nationality']]=x
            else:
                dicc[top10["elements"][a][0]['Nationality']]=1
        a+=1
    count=0
    mayor=""
    for y in dicc.keys():
        if dicc[y]> count:
            mayor= y
            count=dicc[y]
    
    o=lt.newList("ARRAY_LIST")
    lt.addLast(o,dicc)
    mg.sort(o,cmpO)
    

    return mayor,o,top10

def newExposition(catalog, min, max, area):
    
    cat=catalog["Artworks"]["elements"]
    sum=0
    i=0
    catalogDate=lt.newList("ARRAY_LIST")
    for x in cat:
        if x["Date"]>=(min) and x["Date"]<=(max):
            lt.addLast(catalogDate, x)

    catDate=catalogDate["elements"]
    catalogArea=lt.newList("ARRAY_LIST")

    while sum<(area*10000):
        obr=0
    
        if catDate[i]['Height (cm)']!="" and catDate[i]['Width (cm)'] !="":

            obr=float(catDate[i]['Height (cm)'])*float(catDate[i]['Width (cm)'])
            
            sum=sum+obr
            lt.addLast(catalogArea,catDate[i])
        i+=1
        
    return catalogArea,sum
    
    

# Funciones utilizadas para comparar elementos dentro de una lista
def cmpArtworkByDateAcquired(artwork1, artwork2):

    if (artwork1["DateAcquired"]) < (artwork2["DateAcquired"]):
        return True
    else:
        return False

def cmpO(a,b):
    print(a)
    if a.values() < b.values():
        return True
    else:
        return False

def cmpIDObject(a,b):

    if a["ConstituentID"]<b["ConstituentID"]:
        return True
    else:
        return False
# Funciones de ordenamiento




                     


