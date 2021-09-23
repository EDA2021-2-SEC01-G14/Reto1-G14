"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
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
 """

from os import stat_result
import config as cf
import sys
default_limit=1000
sys.setrecursionlimit(default_limit*10)
import controller
from DISClib.ADT import list as lt
assert cf

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():

    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Algoritmos de Ordenamiento")
    print("3- Listar cronológicamente las adquisiciones ")
    print("4- Listar cronológicamente los artistas")
    print("5- Clasificar las obras de un artista por técnica")
    print("6- Clasificar las obras por la nacionalidad de sus creadores")
    print("7- Costos transportar obras de un departamento")
    print("8- Proponer una nueva exposición en el museo")

catalog = None

def printOP3(gd, min, max, tamaño):

    print("Las obras encontradas entre " + str(min) + " hasta " + str(max) + " con una muestra de " + str(tamaño) + " son:")
    a = gd[0]
    print("Número total de obras: " + str(len(a["elements"])))

    print("Tiempo: "+ str( gd[1]))

def printArtistBegindate(list):
    
    print('El numero total de artistas en aquel rango es de: ', lt.size(list[0]))

    for i in range(1,len(list)):
        print(list[i])
    
def printArtworsMediums(list): 

    if list == 0:
        print('\nNo tiene obras')
    else:
        print('\nEl artista tiene',list[0], 'obras') 

        print('Se usan', len(list[1]), 'técnicas en total')
        print('La técnica mas utilizad es: ', list[2])

        for a in list[3]['elements']:
            print('\nTitulo: '+a['Title'], 'Fecha de la obra: '+a['Date'], 'Tecnica o Medio: '+a['Medium'],
            'Diemensiones: '+ a['Dimensions'] )

 
def printArtDepa(list):

    print('\nEl departamento tiene un total de ',lt.size(list[0]), 'obras')

    print('El costo por el servicio de transporte es de ',round(list[1]), 'USD')

    print('Todas las obras tienen un peso estimado de' , round(list[2]), 'kg')
    print('\n5 obras mas antiguas a transportar:')
    for i in range(1,6):
#'|Artista: '+a['Artist'],
        a=lt.getElement(list[0],i)
        print('\nTitulo: '+ a['Title'],  '|Clasificacion: '+ a['Classification'], '|Fecha: '+ a['Date'],
         '|Medio: '+ a['Medium'], '|Dimensiones: '+ a['Dimensions'], '|Costo Transporte: '+ a['Cost'])
    print('\n5 obras mas costosas a transportar:')
    for i in range(1,6):
#'|Artista: '+b['Artist'],
        b=lt.getElement(list[3],i)
        print('\nTitulo: '+ b['Title'],  '|Clasificacion: '+ b['Classification'], '|Fecha: '+ b['Date'],
         '|Medio: '+ b['Medium'], '|Dimensiones: '+ b['Dimensions'], '|Costo Transporte: '+ b['Cost'])
    
    

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("1. ARRAY lIST")
        print("2. LINKED LIST")
        option = int(input("Digite el número de la opción en que desea cargar los datos: "))
        print("Cargando información de los archivos ....")

        catalog = controller.initCatalog(option)
        controller.loadData(catalog)
        
        print("\nArtistas cargadas: " + str(lt.size(catalog["Artists"])))
        print("\nObras cargadas: " + str(lt.size(catalog["Artworks"])))
    

    elif int(inputs[0]) == 2:

        print("Seleccione el tipo de ordenamiento interactivo que desea realizar:\n")
        print("1. Insertion\n")
        print("2. Shell\n")
        print("3. Merge\n")
        print("4. Quick Sorts\n")

        op = int(input("\n"))
        

    elif int(inputs[0]) == 3:

        tamaño = int(input("Digite el tamaño de la muestra: "))
        print("Digite el rango de fechas en el que desea realizar la búsqueda (AAAA-MM-DD)")
        min = int(input("Fecha Inicial: ").replace("-",""))
        max = int(input("Fecha Final: ").replace("-",""))

        gd = controller.getArtworksbyDate(catalog, min, max, tamaño,op,option)

        printOP3(gd, min, max, tamaño)

    elif int(inputs[0]) == 4:
        print("Digite el rango de fechas en el que desea realizar la búsqueda (AAAA)")
        min = int(input("Fecha Inicial: "))
        max = int(input("Fecha Final: "))
         
        list=controller.getArtistBeginDate(catalog,min,max)
        printArtistBegindate(list)
    

    elif int(inputs[0]) == 5:
        Name=input("El nombre del artista que desea buscar: ")
        
        list=controller.ArtworksbyArtist(catalog,Name)
        printArtworsMediums(list)


    elif int(inputs[0]) == 6:
    
        depa=input('Digite el nombre del departamento que desea costear: ')
        list=controller.TransportCos(catalog,depa)
        printArtDepa(list)


    elif int(inputs[0]) == 7:
        pass

    else:
        sys.exit(0)

sys.exit(0)
