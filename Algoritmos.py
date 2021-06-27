
#Se elige como victima la pagina que lleva mas tiempo en memoria
def FLU():

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
FLU()