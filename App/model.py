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
        catalog['Artists'] = lt.newList()
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

def getArtworksbyDate(catalog, min, max, tamaño, op):

    start = time.process_time_ns()
    
    list2 = lt.subList(catalog["Artworks"], 1 , tamaño)
    list2 = list2.copy()
    b=lt.newList("ARRAY_LIST")
    
    for byDate in list2["elements"]:

        if byDate["DateAcquired"] != "":
        
            date = int(byDate["DateAcquired"].replace("-",""))

            if date >= min and date <= max:
                lt.addLast(b, byDate)

    
    if op == 1:
        it.sort(b, cmpArtworkByDateAcquired)
    elif op == 2:
        sa.sort(b, cmpArtworkByDateAcquired)
    elif op == 3:
        mg.sort(b, cmpArtworkByDateAcquired)
    elif op == 4:
        qs.sort(b, cmpArtworkByDateAcquired)

    stop = time.process_time_ns()

    sgs = (stop-start)/1000000000

    return b, sgs

    

        

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





