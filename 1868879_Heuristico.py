################## Inicio - Lectura de Datos ################## 
from os import O_APPEND
import pandas as pd
import numpy as np
import os.path
import logging

# Descomenta una línea con la instancia deseada para correr el programa
ruta = "Instancia1_10.txt"
# ruta = "Instancia1_20.txt"
# ruta = "Instancia1_50a.txt"
# ruta = "Instancia1_50b.txt"

# Pregunta el nombre de archivo junto con extensión
askname_File = ruta
file_exists = os.path.exists(askname_File)

# Si el archivo existe, entonces lo toma como el
# que usará para generar los datos
if file_exists is True:
    current_Filename = askname_File
else:
    print("File not exists!")
    exit()


# Genera los archivos adecuados para el archivo (Instancia1_10.txt)
if ( current_Filename == 'Instancia1_10.txt'):
    newTxtGeneral = "Instancia1_10new.txt"
    valuesNew = "values1_10.txt"
    productosNew = "productos1_10.txt"
    arrregloNew = "arreglo1_10.txt"
    pass
# Genera los archivos adecuados para el archivo (Instancia1_20.txt)
elif ( current_Filename == 'Instancia1_20.txt'):
    newTxtGeneral = "Instancia1_20new.txt"
    valuesNew = "values1_20.txt"
    productosNew = "productos1_20.txt"
    arrregloNew = "arreglo1_20.txt"
    pass
# Genera los archivos adecuados para el archivo (Instancia1_50a.txt)
elif ( current_Filename == 'Instancia1_50a.txt'):
    newTxtGeneral = "Instancia1_50anew.txt"
    valuesNew = "values1_50a.txt"
    productosNew = "productos1_50a.txt"
    arrregloNew = "arreglo1_50a.txt"
    pass
# Genera los archivos adecuados para el archivo (Instancia1_50b.txt)
elif ( current_Filename == 'Instancia1_50b.txt'):
    newTxtGeneral = "Instancia1_50bnew.txt"
    valuesNew = "values1_50b.txt"
    productosNew = "productos1_50b.txt"
    arrregloNew = "arreglo1_50b.txt"
    pass
else:
    print("File not supported") # En caso de que no sea alguno de los anteriores
    exit()                      # entonces termina


# Muestra el nombre del archivo con el que trabaja
print()
print("Trabajando con: ", current_Filename)

# Abre el archivo actual y genera los nuevos archivos necesarios
with open(current_Filename) as fin, open(newTxtGeneral, 'w') as fout:
    for line in fin:
        fout.write(line.replace('\t', ','))

# Abre tres archivos para guardar cada seccion del txt
out1 = open(valuesNew, 'w')
# Archivo para guardar los valores de variables
out2 = open(productosNew, 'w')
# Archivo para guardar los productos y sus tiempos
# de procesamiento
out3 = open(arrregloNew, 'w')
# Archivo para guardar la matriz de tiempos de preparación
with open(newTxtGeneral, 'r') as f:
    for line in f:
        if 'Values' in line:
            for line in f:
                #print(line)
                out1.writelines(line)
                # Genera el archivo 'values.txt y guarda
                # los valores
                if not line.strip():
                    for line in f:
                        if 'Productos' in line:
                            for line in f:
                                out2.writelines(line)
                                # Genera el archivo 'productos.txt y guarda
                                # los valores
                                if not line.strip():
                                    for line in f:
                                        if 'Arreglo' in line:
                                            for line in f:
                                                out3.writelines(line)
                                                # Genera el archivo 'arreglo'.txt y guarda
                                                # los valores
                                                if not line.strip():
                                                    break
out1.close()
out2.close()
out3.close()
# Cierra todos los archivos IMPORTANTE

dataframe1 = pd.read_csv(valuesNew, index_col=None, header=None)
dataframe1.to_csv('goatValues.csv', index=None)
# Genera un csv del txt actual con los valores de n, M y T

dataframe2 = pd.read_csv(productosNew, index_col=None, header=None)
dataframe2.to_csv('goatProducts.csv', index=None)
# Genera un csv del txt actual con los valores de n, M y T    

dataframe3 = pd.read_csv(arrregloNew, index_col=None, header=None)
dataframe3.to_csv('goatArreglo.csv', index=None)
# Genera un csv del txt actual con los valores de n, M y T

values_array = dataframe1.to_numpy()
productos_array = dataframe2.to_numpy()
arreglo_array = dataframe3.to_numpy()
# Transforma cada uno de los dataframes en arreglos


lista_final = []
lista_temp = [0]
indice_cliente = 0
tiempo_periodo_temp = 0
productos = []
# Listas necesarias para contener datos finales y de control


print()
print("Datos")
n_nodos = (values_array[0][1] + 1)
print( "No. de productos: ", (values_array[0][1]) )
# Muestra la cantidad de nodos

M = (values_array[1][1])
print( "Tiempo de Mantenimiento M: ", values_array[1][1])
# Muestra el valor de M

T = (values_array[2][1])
print("Tiempo de Periodo T: ", values_array[2][1])
# Muestra el valor de T

C = T - M
print("Capacidad maxima C: ", C)
# Capacidad de cada ciclo

# imprimir pruductos
for x in range(len(productos_array)):
    productos.append(productos_array[x][1])
print("Tiempo por producto")
for i in range( len( productos ) ):
    print(f"{i + 1} {productos[i]}")
productos.insert(0, M)
# Agrega a la lista de productos el arreglo respectivo
# e inserta al principio el valor de M

matrizTiempos = arreglo_array
print()
print("Matriz de Tiempos")
for i in range( len(productos ) ):
    print(f"{i} {matrizTiempos[i]}")
# Simplemente muestra la matriz de tiempos
################## Fin - Lectura de Datos ################## 



lista_final = []
lista_temp = [0]
indice_cliente = 0
tiempo_periodo_temp = 0

# Función para verificar si ya se agregaron todos los productos
def verifyProducts():
    count = 0                    
    for i in range( len(lista_temp) ):
        if ( i in lista_temp):
            count = count + 1
        
    if(count == n_nodos):
            return True
    else:
        return False    

flag = False

################## Fin - Generar Tour TSP ################## 
while( not flag ): # El ciclo dura n_nodos - 1 para así reservar el último puesto para el 
    # cliente inicial
    costo_min = max( matrizTiempos[indice_cliente] ) # Se encuentra el valor máximo de la fila
    for i in range(n_nodos): # Aquí se recorren todos los clientes de la fila actual
        # Se compara el costo de cada cliente para encontrar el valor mínimo y se valida también que 
        # el costo no sea 0
        if ( matrizTiempos[indice_cliente][i] < costo_min):
            # Se verifica que el cliente no se encuentre ya en la lista del tour
            # Si se encuentra se continua fuera del if-else o si i = j (diagonal de 0s) se excluye
            if ( ( i in lista_temp ) or ( i == indice_cliente) ):
                continue
            # Si no se encuentra se considera para poder encontrar el valor mínimo
            else:
                costo_min = matrizTiempos[indice_cliente][i] # Se guarda el valor del costo mínimo en la variable
                i_costo_minimo = i 


    sumaTiempos = matrizTiempos[indice_cliente][i_costo_minimo] + productos[i_costo_minimo] + matrizTiempos[0][i_costo_minimo]

    if( ( tiempo_periodo_temp + sumaTiempos ) < C):
        # El número del cliente sería igual a su índice (matriz)
        lista_temp.append(i_costo_minimo) # Y ya se agrega el cliente con el menor costo a la lista del 
        # tour después de las validaciones
        tiempo_periodo_temp = tiempo_periodo_temp + ( matrizTiempos[indice_cliente][i_costo_minimo] + productos[i_costo_minimo] )
        indice_cliente = i_costo_minimo # Se guarda el índice del último cliente que se ha añadido para 
        # encontrar el nuevo cliente
        
    else:
        lista_temp.append(0) # Se agrega el nodo 0 (Mantenimiento) debido a que ya no caben más productos
        indice_cliente = 0 # Se guarda el índice con 0 (Mantenimiento)
        tiempo_periodo_temp = 0 # Se reinicia el tiempo del periodo

    flag = verifyProducts()
# Fin del for para todos los nodos

       

################## Fin - Generar Tour TSP ################## 


lista_temp.pop(0)
lista_temp.append(0)


################## Inicio - Calcular Costo Total ################## 
# Inicializar variable para el costo total
costo_total = 0
costo_total = costo_total + matrizTiempos[ 0 ][ lista_temp[0] ]
# Para cada nodo se encuentra su costo con el nodo siguiente
for nodo in range( len(lista_temp) ):
    if (nodo == len(lista_temp) - 1): #Si es igual al último índice se sale del loop
        break
    # Se consulta la matriz de tiempos para obtener el costo total del 
    # Tour TSP Final
    costo_total = costo_total + matrizTiempos[ lista_temp[nodo] ][ lista_temp[nodo + 1] ]


# Calcular cuántos mantenimientos hay en la lista
countM = 0
for nodo in range( len(lista_temp) ):
    if( lista_temp[nodo] == 0 ):
        countM = countM + 1

costo_total = costo_total + (M * countM)

costo_total = costo_total + sum(productos) - M

print(lista_temp)
#print(countM)
print(costo_total)
################## Inicio - Calcular Costo Total ################## 



################## Inicio - Impresion de resultados ################## 

################## Fin - Impresion de resultados ################## 
