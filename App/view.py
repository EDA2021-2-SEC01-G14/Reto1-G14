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
    print("2- Listar cronológicamente los artistas")
    print("3- Listar cronológicamente las adquisiciones ")
    print("4- Clasificar las obras de un artista por técnica")
    print("5- Clasificar las obras por la nacionalidad de sus creadores")
    print("6- Costostransportar obras de un departamento")
    print("7- Proponer una nueva exposición en el museo")

catalog = None


def print_3(gd):
    tamaño=lt.size(gd)
    print("Número total de obras: " + str(tamaño))
    purchase= controller.purchase(gd)
    print("Obras compradas: " + str(purchase))
    print("Primeras 3 obras: ")
    print("ObjectID: " + str(gd["elements"][0]["ObjectID"]) + ", Título: " + str(gd["elements"][0]['Title'])
    + ", Fecha: " + str(gd["elements"][0]['DateAcquired'])
    + ", Medio: " +str(gd["elements"][0]['Medium']) + ", Dimensiones: " + str(gd["elements"][0]['Dimensions']))

    print("\nObjectID: " + str(gd["elements"][1]["ObjectID"]) + ", Título: " + str(gd["elements"][1]['Title'])
    + ", Fecha: " + str(gd["elements"][1]['DateAcquired'])
    + ", Medio: " +str(gd["elements"][1]['Medium']) + ", Dimensiones: " + str(gd["elements"][1]['Dimensions']))

    print("\nObjectID: " + str(gd["elements"][2]["ObjectID"]) + ", Título: " + str(gd["elements"][2]['Title'])
    + ", Fecha: " + str(gd["elements"][2]['DateAcquired'])
    + ", Medio: " +str(gd["elements"][2]['Medium']) + ", Dimensiones: " + str(gd["elements"][2]['Dimensions']))

    print("\nÚltimas 3 obras: ")

    print("\nObjectID: " + str(gd["elements"][tamaño-3]["ObjectID"]) + ", Título: " + str(gd["elements"][tamaño-3]['Title'])
    + ", Fecha: " + str(gd["elements"][tamaño-3]['DateAcquired'])
    + ", Medio: " +str(gd["elements"][tamaño-3]['Medium']) + ", Dimensiones: " + str(gd["elements"][tamaño-3]['Dimensions']))

    print("\nObjectID: " + str(gd["elements"][tamaño-2]["ObjectID"]) + ", Título: " + str(gd["elements"][tamaño-2]['Title'])
    + ", Fecha: " + str(gd["elements"][tamaño-2]['DateAcquired'])
    + ", Medio: " +str(gd["elements"][tamaño-2]['Medium']) + ", Dimensiones: " + str(gd["elements"][tamaño-2]['Dimensions']))

    print("\nObjectID: " + str(gd["elements"][tamaño-1]["ObjectID"]) + ", Título: " + str(gd["elements"][tamaño-1]['Title'])
    + ", Fecha: " + str(gd["elements"][tamaño-1]['DateAcquired'])
    + ", Medio: " +str(gd["elements"][tamaño-1]['Medium']) + ", Dimensiones: " + str(gd["elements"][tamaño-1]['Dimensions']))

    


    

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
       
        print("Cargando información de los archivos ....")

        catalog = controller.initCatalog()
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

        print("Digite el rango de fechas en el que desea realizar la búsqueda (AAAA-MM-DD)")
        min = int(input("Fecha Inicial: ").replace("-",""))
        max = int(input("Fecha Final: ").replace("-",""))

        gd = controller.getArtworksbyDate(catalog, min, max)

        print_3(gd)

        

    elif int(inputs[0]) == 4:
        print("Digite el rango de fechas que desea realizar la busqueda (AAAA-MM-DD)")
        min = input("Año Inicial: ")
        max = input("Año Final: ")
        
        result= controller.getYear(catalog, min, max)

    

    elif int(inputs[0]) == 0:
        pass

    elif int(inputs[0]) == 5:
        pass

    elif int(inputs[0]) == 6:
        pass

    elif int(inputs[0]) == 7:
        pass

    elif int(inputs[0]) == 3:
        pass

    elif int(inputs[0]) == 4:
        pass

    elif int(inputs[0]) == 5:
        pass

    elif int(inputs[0]) == 6:
        pass

    elif int(inputs[0]) == 7:
        pass

    else:
        sys.exit(0)

sys.exit(0)
