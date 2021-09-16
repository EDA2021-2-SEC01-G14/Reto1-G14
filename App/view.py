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
    print("7- Costostransportar obras de un departamento")
    print("8- Proponer una nueva exposición en el museo")

catalog = None


def printOP3(gd, min, max, tamaño):

    print("Las obras encontradas entre " + str(min) + " hasta " + str(max) + " con una muestra de " + str(tamaño) + " son:")
    a = gd[0]
    print("Número total de obras: " + str(len(a["elements"])))

    print("Tiempo: "+ str( gd[1]))

    

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

        gd = controller.getArtworksbyDate(catalog, min, max, tamaño,op)

        printOP3(gd, min, max, tamaño)

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
