n_nodos = 11
M = 50
T = 300
C = T - 50

productos = [50, 86, 78, 64, 22, 98, 82, 87, 52, 100, 99]

matrizTiempos = [
    [0,	8,	15,	7,	16,	15,	9,	14,	20,	14,	9],
    [7,	0,	14,	17,	19,	17,	14,	14,	14,	18,	8],
    [9,	11,	0,	16,	6,	14,	15,	5,	10,	11,	18],
    [13, 18, 6,	0,	14,	18,	7,	19,	12,	10,	14],
    [20, 19, 6,	17,	0,	11,	12,	6,	11,	14,	7],
    [13, 15, 7,	16,	16,	0,	13,	5,	11,	18,	14],
    [20, 11, 16, 6,	15,	10,	0,	12,	9,	14,	13],
    [5,	15,	12,	5,	5,	18,	17,	0,	12,	7,	15],
    [5,	11,	8,	13,	19,	17,	19,	20,	0,	18,	15],
    [7,	6,	14,	14,	19,	9,	9,	7,	16,	0,	7],
    [6,	11,	9,	18,	17,	20,	9,	15,	18,	20,	0] ]


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
