################## Inicio - Lectura de Datos ################## 
from os import O_APPEND
import pandas as pd
import numpy as np
import os.path
import logging

# Descomenta una línea con la instancia deseada para correr el programa
# ruta = "Instancia1_10.txt"
# ruta = "Instancia1_20.txt"
# ruta = "Instancia1_50a.txt"
ruta = "Instancia1_50b.txt"

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
producto = 0
tiempo_periodo_temp = 0
productos = []
# Listas necesarias para contener datos finales y de control


print()
print("Datos")
n_productos = (values_array[0][1] + 1)
print( "No. de productos:", (values_array[0][1]) )
# Muestra la cantidad de nodos

M = (values_array[1][1])
print( "Tiempo de Mantenimiento M:", values_array[1][1])
# Muestra el valor de M

T = (values_array[2][1])
print("Tiempo de Periodo T:", values_array[2][1])
# Muestra el valor de T

C = T - M
print("Capacidad maxima C:", C)
# Capacidad de cada ciclo

# imprimir pruductos
print()
for x in range(len(productos_array)):
    productos.append(productos_array[x][1])
productos.insert(0, M)

print("Tiempo de Preparacion por Producto")
pd.set_option("max_columns", 10)
pd.set_option("max_rows", 10)
print_products = pd.DataFrame(productos)
print( print_products )
# for i in range( len( productos ) ):
#     print(f"{i + 1} {productos[i]}")

# Agrega a la lista de productos el arreglo respectivo
# e inserta al principio el valor de M

matrizTiempoPreparacion = arreglo_array
print()
print("Matriz de Tiempos de Preparacion")
pd.set_option("max_columns", 9)
pd.set_option("max_rows", 9)
print_matriz = pd.DataFrame(matrizTiempoPreparacion)
print(print_matriz)
# for i in range( len( matrizTiempoPreparacion[0] ) ):
#     print(f"{i} {matrizTiempoPreparacion[i]}")
# Simplemente muestra la matriz de tiempos
################## Fin - Lectura de Datos ################## 




################## Inicio - Generar Secuenciación de productos ################## 
lista_final         = []
lista_temp          = [0]
producto            = 0
tiempo_periodo_temp = 0

# Función para verificar si ya se agregaron todos los productos
def verifyProducts():
    count = 0                    
    for i in range( len(lista_temp) ):
        if ( i in lista_temp):
            count = count + 1
    if(count == n_productos):
            return False
    else:
        return True    

while( verifyProducts() ): # El ciclo dura hasta que todos los productos se haya agregado a la secuencia
    tiempo_min = max( matrizTiempoPreparacion[producto] ) # Se encuentra el valor máximo de la fila
    for i in range(n_productos): # Aquí se recorren todos los productos de la fila actual
        # Se compara el tiempo de cada producto para encontrar el valor mínimo
        if ( matrizTiempoPreparacion[producto][i] < tiempo_min):
            # Se verifica que el producto no se encuentre ya en la lista del tour
            # Se verifica el caso cuando i = j (diagonal de 0s) 
            # Si se encuentra se continua fuera del if-else, excluyéndolo
            if ( ( i in lista_temp ) or ( i == producto) ):
                continue
            # Si no se encuentra se considera para poder encontrar el valor mínimo
            else:
                tiempo_min = matrizTiempoPreparacion[producto][i] # Se guarda el valor del tiempo mínimo en la variable
                i_tiempo_minimo = i 

    # Se hace una suma de tiempo para verificar que no se pase del tiempo límite
                # Tiempo de preparación del producto actual al producto a agregar 
    sumaTiempos = matrizTiempoPreparacion[producto][i_tiempo_minimo] 
                # Tiempo de preparación del producto a agregar 
    sumaTiempos += productos[i_tiempo_minimo] 
                # Tiempo de preparación del producto a agregar al Mantenimiento (0)
    sumaTiempos += matrizTiempoPreparacion[i_tiempo_minimo][0]

    # Verificar que no pase del tiempo límite, sumando el tiempo del periodo actual
    # + el tiempo generado si se agrega el nuevo producto
    if( ( tiempo_periodo_temp + sumaTiempos ) < C):
        lista_temp.append(i_tiempo_minimo) # Y ya se agrega el producto con el menor tiempo a la secuencia
                            # Tiempo del periodo actual
        tiempo_periodo_temp = tiempo_periodo_temp
                            # Tiempo de preparación del producto actual al producto a agregar  
        tiempo_periodo_temp += matrizTiempoPreparacion[producto][i_tiempo_minimo] 
        tiempo_periodo_temp += productos[i_tiempo_minimo]
        producto = i_tiempo_minimo # Se guarda el índice del último producto que se ha añadido para 
        # encontrar el nuevo producto
        
    else:
        lista_temp.append(0) # Se agrega el producto 0 (Mantenimiento) debido a que ya no caben más productos
        producto = 0 # Se guarda el índice con 0 (Mantenimiento)
        tiempo_periodo_temp = 0 # Se reinicia el tiempo del periodo
# Fin del for para todos los productos

# Se quita el mantenimiento (0) al inicio de la lista
lista_temp.pop(0)
lista_temp.append(0)
################## Fin - Generar Secuenciación de productos ################## 





################## Inicio - Calcular Tiempo Total ################## 
# Inicializar variable para el tiempo total
tiempo_total = 0
tiempo_total = tiempo_total + matrizTiempoPreparacion[ 0 ][ lista_temp[0] ]
# Para cada producto se encuentra su tiempo con el producto siguiente
for producto in range( len(lista_temp) ):
    if (producto == len(lista_temp) - 1): #Si es igual al último índice se sale del loop
        break
    # Se consulta la matriz de tiempos para obtener el tiempo total del 
    # Tour TSP Final
    tiempo_total = tiempo_total + matrizTiempoPreparacion[ lista_temp[producto] ][ lista_temp[producto + 1] ]


# Calcular cuántos mantenimientos hay en la lista
countM = 0
for producto in range( len(lista_temp) ):
    if( lista_temp[producto] == 0 ):
        countM = countM + 1
tiempo_total = tiempo_total + (M * countM)

# Agregar el tiempo de los productos
tiempo_total = tiempo_total + sum(productos) - M
################## Fin - Calcular Tiempo Total ################## 



################## Inicio - Impresion de resultados ################## 
print()
print("Resultados")
print("Secuencia de productos")
print(lista_temp)
print("Tiempo total")
print(tiempo_total)
print()
print("Cantidad de periodos T")
print(lista_temp.count(0))
print()
################## Fin - Impresion de resultados ################## 
