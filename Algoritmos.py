



#Se elige como victima la pagina que lleva mas tiempo en memoria
def LRU():

    lista_result = []
    parametros_entrada = [1,2,3,4,1,2,5,1,2,3,4,5]
    parametro_largo = 4
    
    contador1 = 0
    contador2 = 0
    contador3 = 0
    
    lista_contadora_roja = []

    es_diferente = False

    #Recorre el arreglo de numeros
    for n in parametros_entrada:

        #Caso segundo, cuando entra un numero igual
        contador1 = 0
        es_diferente = True

        #Recorro la lista de resultado
        for m in lista_result:

            #Es el parametro a insertar es igual al dato de la lista
            if n == m:
                lista_contadora_roja[contador1] = 1
                es_diferente = False
            else:
                #Se suma uno a los demas numeros
                lista_contadora_roja[contador1] += 1

            contador1 += 1
            
        #Caso tercero, cuando entra un numero diferente
        if es_diferente == True and contador2 >= parametro_largo:

            contador3 = 0
            mas_grande = 0
            indice_encontrado = 0

            #Fijarse en que lleva mas tiempo
            for y in lista_contadora_roja:

                #Es mayor, se sustitulle
                if mas_grande < y:
                    mas_grande = y
                    indice_encontrado = contador3

                contador3 += 1

            #Sustituyo el numero que a estado mas tiempo
            lista_result[indice_encontrado] = n   
            lista_contadora_roja[indice_encontrado] = 1

        #Caso primero, cuando se llena la memoria
        if  es_diferente == True and contador2 < parametro_largo:
            lista_result.append(n)
            lista_contadora_roja.append(1)
            contador2 += 1
            
        #Imprimo corrida
        print("\nLista de resultado: ")
        print(lista_result)

        print("Lista de contadores: ")
        print(lista_contadora_roja)

#Compilo
#LRU()

#
def FIFO():
    lista_resultado = []
    parametros_entrada = [7,0,1,2,0,3,0,4,2,3,0,3,2,1,2]
    parametro_largo = 3

    contador_global = 0


    #Caso primero, se llena la lista de resultado
    for n in parametros_entrada:
        
        es_igual = False
    
        #Si el numero a insertar es igual entonces no se hace nada
        for m in lista_resultado:
            
            if m == n:
                es_igual = True

        #Caso en el que el numero es diferente.
        if es_igual == False:

            #Esta vacia alguna casilla?
            if len(lista_resultado) < parametro_largo:
                lista_resultado.append(n)
            else:
                lista_resultado[contador_global] = n

            print("\nIndice")
            print(contador_global)

            #Coloco el indice global en el campo correspondiente
            if contador_global < parametro_largo-1:
                contador_global += 1
            else:
                contador_global = 0
        else:
            print("\nIndice")
            print(contador_global)

        #Imprimo resultado
        print("Lista de resultado:")
        print(lista_resultado)

#Compilo
#FIFO()

#Algoritmo de remplazo de la frecuencia menos usada
def LFU():
    lista_resultado = []
    parametro_largo = 3
    lista_frecuencias = []
    lista_senales = []
    parametros_entrada = [7,0,1,2,0,3,0,4,2,3,0,3,2,1,2]
    contador = 0

    #Inicializo la lista de frecuencias en cero
    for i in range(0, parametro_largo):
        lista_frecuencias.append(0)

    #Inicializo lista de senales
    for o in range(0, len(parametros_entrada)):
        lista_senales.append(0)

    #Recorro paramtros de entrada
    for n in parametros_entrada:

        es_vacia = False

        #Caso base, cuando la lista es vacia
        if lista_resultado == []:
            lista_resultado.append(n)
            lista_frecuencias[contador] = 1
            es_vacia = True

        es_igual = False
        contador3 = 0

        #Caso si el numero es igual
        for m in lista_resultado:

            if m == n and es_vacia == False:
                es_igual = True
                lista_frecuencias[contador3] += 1

            contador3 += 1 

        #Caso cuando no es igual el numero y hay casillas vacias
        if es_igual == False and \
            es_vacia == False and \
            len(lista_resultado) < parametro_largo:

            lista_resultado.append(n)
            lista_frecuencias[contador] = 1

        contador += 1
        lista_frecuencias_bajas = []
        numero_seleccionado = -1

        #Caso cuando la lista esta llena
        if es_igual == False and \
            es_vacia == False and \
            contador > parametro_largo:
        
            lista_frecuencias_bajas_temp = []
            lista_frecuencias_bajas_numeros = []
            contador4 = 0

            #Saco la frecuencia mas baja, en caso que hayan dos o mas iguales, salen.
            for k in lista_frecuencias:

                vacia_es = False

                #Caso cuando es vacia la lista
                if lista_frecuencias_bajas == []:
                    lista_frecuencias_bajas.append(k)
                    lista_frecuencias_bajas_numeros.append(lista_resultado[contador4])
                    vacia_es = True
                
                bandera_temp = False

                #Recorro la lista de frecuencias bajas, a ver si son iguales o menores
                for u in lista_frecuencias_bajas:
                    
                    #Encuentra una frecuencia con la misma resonancia
                    if u == k and vacia_es == False:
                        lista_frecuencias_bajas_temp.append(k)
                        lista_frecuencias_bajas_numeros.append(lista_resultado[contador4])


                    #Caso cuando encuentra una mas baja
                    if k < u:
                        lista_frecuencias_bajas_temp = []
                        lista_frecuencias_bajas_temp.append(k)
                        lista_frecuencias_bajas_numeros = []
                        lista_frecuencias_bajas_numeros.append(lista_resultado[contador4])
                        bandera_temp = True

                if bandera_temp == True:
                    lista_frecuencias_bajas = lista_frecuencias_bajas_temp
                    
                contador4 += 1
                                
            contador1 = 0
            bandera_encontro = False

            #Recorro de izquierda a derecha la lista de parametros
            #hasta llegar al primero que consida con la frecuencia baja
            #no ddebe estar marcado en la lista de senales
            for h in parametros_entrada:
                
                if bandera_encontro == False:
                    #Recorro la frecuencias bajas hasta que sea una de ellas
                    for j in lista_frecuencias_bajas_numeros:

                        #Encontro concidencia
                        if j == h and \
                            lista_senales[contador1] == 0 and \
                            bandera_encontro == False:
                            
                            #hace senal de que ya uso este
                            lista_senales[contador1] = 1
                            numero_seleccionado = j

                            bandera_encontro = True

                contador1 += 1

            contador2 = 0

            lista_resultado_temp = lista_resultado
                
            #Hago el debido remplazo
            for g in lista_resultado:

                #Encuentre el numero a remplazar
                if g == numero_seleccionado:
                    lista_resultado_temp[contador2] = n
                    lista_frecuencias[contador2] = 1

                contador2 += 1
            
            lista_resultado = lista_resultado_temp

        print("\nNumero seleccionado a remplazar")
        print(numero_seleccionado)
                
        print("Lista de resultados:")
        print(lista_resultado)

        print("Lista de frecuencias:")
        print(lista_frecuencias)


#Compilo
#LFU()

#
def MRU():
    lista_resultado = []
    parametro_largo = 3
    parametros_entrada = [7,0,1,2,0,3,0,4,2,3,0,3,2,1,2]

    for n in parametros_entrada:
        print(n)

#Compilo
MRU()