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
import datetime as DT
import time

from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import mergesort as mer
from DISClib.Algorithms.Sorting import quicksort as qui
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
    
    elif option == 2:
        catalog['Artists'] = lt.newList()
        catalog['Artworks'] = lt.newList()
   
    return catalog

# Funciones para agregar informacion al catalogo

def addArtist(catalog, artist):
    lt.addLast(catalog["Artists"], artist)

def addArtwork(catalog, artwork):
    lt.addLast(catalog["Artworks"], artwork)

# Funciones para creacion de datos

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

def cmpArtworkByDateAcquired(artwork1, artwork2):

    a1=artwork1['DateAcquired'].split('-')
    date1=DT.data(int(a1[0]),int(a1[1]),int(a1[2]))

    a2=artwork1['DateAcquired'].split('-')
    date2=DT.data(int(a2[0]),int(a2[1]),int(a2[2]))
    
    rta=False
    if date1 < date2:
        return True

    return rta 
    '''
    artwork2_date=artwork2['DateAcquired']
    date2=DT.datetime.strptime(artwork2_date, '%Y-%m-%d').date
    
    
    Devuelve verdadero (True) si el 'DateAcquired' de artwork1 es menores que el de artwork2
    Args:
    artwork1: informacion de la primera obra que incluye su valor 'DateAcquired'
    artwork2: informacion de la segunda obra que incluye su valor 'DateAcquired'
    '''


# Funciones de ordenamiento

def sortartworks(catalog, size):

    if len(catalog["Artworks"]) < size:
        return 'La muestra es mas grande que los datos cargados'
    
    else:

        sub_list = lt.subList(catalog["Artworks"], 1, size)
        sub_list = sub_list.copy()
        start_time = time.process_time()
        sorted_list = sa.sort(sub_list, cmpArtworkByDateAcquired)
        stop_time = time.process_time()





