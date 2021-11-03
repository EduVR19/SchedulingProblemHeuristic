#################################################################
# Nombre:       Eduardo Vicente Reyna Villela                   #                   
# Matrícula:    1868879                                         #
# Carrera:      ITS                                             #
# Materia:      Temas Selectos de Optimización                  #
# Docente:      Dra. Iris Abril Martínez Salazar                #
# Actividad:    Programar el Algoritmo de Inserción Más Barata  # 
#               para resolver el Problema TSP                   #
# Fecha:        09/10/2021                                      #
#                                                   FIME - UANL #
#################################################################

################## Inicio - Leer datos del archivo ##################
import csv
import sys

par_ordenado = [] # Inicializar la lista para cada par
coord = [] # Inicializar la matriz de coordenadas

# Descomenta solo una línea con la ruta del archivo
# Ruta del archivo
ruta = '5nodes.csv'
# ruta = '48nodes.csv'
# ruta = '101nodes.csv'

# Abrir el archivo para leerlo y asignarlo como 
with open(ruta, encoding='utf-8-sig') as archivo_csv:
    lector_csv = csv.reader(archivo_csv)
    
    
    for linea in lector_csv:
        n_nodos = linea[0]
        x_coord = linea[1]
        y_coord = linea[2]
        par_ordenado.append(x_coord)
        par_ordenado.append(y_coord)
        coord.append(par_ordenado)
        par_ordenado = []

# Eliminar los primeros pares que son de "numero, nodos" y "x, y"
coord.pop(0)    
coord.pop(0)

# Convertir de tipo texto a tipo numérico
n_nodos = int(n_nodos) # Convertir el numero de nodos str -> int
# Convertir los lementos de la matriz de coordenadas str -> int
for i in range(n_nodos):
    for j in range(2):
        coord[i][j] = int(coord[i][j])

# Imprimit número de nodos
print()
print("Numero de nodos")
print(n_nodos)
# Imprimit la matriz de coordenadas
print()
print("Coordenadas")
for i in range(n_nodos):
    print(f"{i + 1} {coord[i]}")
################## Fin - Leer datos del archivo ################## 





################## Inicio - Generar matriz de costos ##################
from math import * 
# Inicializar el costo de cada fila
costo_fila = []
# Inicializar la matriz de costos
costos = []

# Función para calcular la distancia Euclidiana
def calcularDistanciaEuclidiana(a, b, c, d):
    distanciaE = pow( a - c, 2 ) + pow( b - d, 2  )
    return sqrt(distanciaE) # devolvemos la distancia

# Ciclo para generar la matriz de costos
for j in range(n_nodos):
    for i in range(n_nodos):
        distancia = calcularDistanciaEuclidiana( coord[j][0], coord[j][1], coord[i][0], coord[i][1] )
        costo_fila.append( round(distancia) ) # Agregar cada costo en una fila
    costos.append( costo_fila ) # Agregar la fila de costo a la matriz
    costo_fila = [] # Borramos los elementos para calcular la próxima fila y volver a guardarla en la 
    # matriz

# imprimir matriz
print()
print("Matriz de costos")
for i in range(n_nodos):
    print(f"{i + 1} {costos[i]}")
################## Fin - Generar matriz de costos ################## 





################## Inicio - Generar Tour Parcial ################## 
import random

n_t = [] # Inicializar lista del tour
n_k = [] # Inicializar lista del nodos k
# Inicializar nodo arbitriario
# nodo_inicial = 5
nodo_inicial = random.randint(1, n_nodos) # 1 
n_t.append(nodo_inicial)
n_t.append(nodo_inicial)

indice_cliente = n_t[0] - 1 # Se identifica el índice del cliente inicial (arbitrario)

costo_min = max( costos[indice_cliente] ) # Se encuentra el valor máximo de la fila
for i in range(n_nodos): # Aquí se recorren todos los clientes de la fila actual
    # Se compara el costo de cada cliente para encontrar el valor mínimo y se valida también que 
    # el costo no sea 0
     if ( costos[indice_cliente][i] <= costo_min and costos[indice_cliente][i] != 0 ):

            costo_min = costos[indice_cliente][i] # Se guarda el valor del costo mínimo en la variable
            i_costo_minimo = i # Se guarda el índice del costo mínimo


n_t.insert(1, i_costo_minimo + 1) # Se inserta el nodo más cercano al nodo inicial, haciendo la forma T = i j i

# Se obtiene una lista con los nodos que faltan por agregar, los nodos k
for i in range(n_nodos):
    if ( (i + 1) in n_t ):
        continue
    else:
        n_k.append( i + 1 )

# Impresión de nodo inicial y subtour T = i j i
print()
print("Nodo Inicial")
print(nodo_inicial)
print()
print("Inserciones")
print("T =", n_t)
################## Fin - Generar Tour Parcial ################## 





################## Fin - Generar Tour TSP ################## 
import sys

# Inicializar costo mas barato con un valor muy grande
costo_mas_barato = sys.maxsize


# Función para obtener el valor de deltaF
def calcularDistanciaArco(i, j, k):
    # Convertimos de nodos a indices para consultar la matriz de costos
    i = i - 1
    j = j - 1
    k = k - 1
    # Consultamos la matriz de costos para emplear la fórmula
    distanciaA = costos[i][k] + costos[k][j] - costos[i][j]
    return distanciaA # devolvemos la distancia


# Se insertan los nodos faltantes (Se resta 2 porque ya se insertaron 2 nodos)
for nodo in range( n_nodos - 2 ):
    # Se calcula para cada nodo en T, se resta 1 ya que por ejemplo si se tiene
    # [1, 2, 1] no se podría calcular para el último elemento + 1 porque está fuera del rango
    for nodo_t in range( len( n_t ) - 1 ):

        i = n_t[nodo_t]     # 0
        j = n_t[nodo_t + 1] # 1

        # Para cada nodo k se calcula la distancia de arco y posteriormente se obtiene el costo más barato
        for nodo_k in range( len( n_k ) ):
            # Se llama a la función para calcular deltaF
            deltaF = calcularDistanciaArco(i, j, n_k[nodo_k])
            # Se compara cada costo para obtener el costo mas barato
            if ( deltaF < costo_mas_barato ):
                costo_mas_barato = deltaF # Se guarda el valor de deltaF para seguir buscando el minimo
                k_nodo = n_k[nodo_k] # Se guarda el nodo k en una variable
                nodo_j = j # Se guarda el índice del nodo j para luego hacer la inserción

    # Se identifica el indice del nodo j
    indice_nodo_j = n_t.index( nodo_j, 1 )
    # Se remueve el nodo de la lista de los nodos k
    n_k.remove(k_nodo)
    # Se hace la inserción del nodo k en el Tour, justo detrás del nodo j
    n_t.insert(indice_nodo_j, k_nodo)

    # Reiniciar valor del costo mas barato
    costo_mas_barato = sys.maxsize

    # Imprimir inserciones
    print("T =", n_t)
################## Fin - Generar Tour TSP ################## 



################## Inicio - Calcular Costo Total ################## 
# Inicializar variable para el costo total
costo_total = 0
# Para cada nodo se encuentra su costo con el nodo siguiente
for nodo in range(n_nodos):
    # Se consulta la matriz de costos para obtener el costo total del 
    # Tour TSP Final
    costo_total = costo_total + costos[ n_t[nodo] - 1 ][ n_t[nodo + 1] - 1 ]
################## Inicio - Calcular Costo Total ################## 




################## Inicio - Impresion de resultados ################## 
print()
print("Tour Final")
print(n_t)
print()
print("Costo Total")
print(costo_total)
print()
################## Fin - Impresion de resultados ################## 
