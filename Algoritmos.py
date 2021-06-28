

####################################################################################################################

#                                         Principios de sistemas operativos

####################################################################################################################

#
def MRU(parametros_entrada, parametro_largo):
    lista_resultado = []
    indice_global = 0
    esta_llena = False
    pf = 0
    ph = 0

    #Recorro paramentros de entrada
    for n in parametros_entrada:

        print("\nPagina:")
        print(n)

        es_vacia = False

        #Caso cuando la lista esta vacia
        if lista_resultado == []:
            lista_resultado.append(n)
            es_vacia = True
            pf += 1

        #Caso cuando el numero ya esta
        if es_vacia == False:

            es_igual = False
            contador1 = 0

            #Recorro lista_resultado para saber si esta el numero
            for m in lista_resultado:
                
                if m == n:
                    es_igual = True
                    indice_global = contador1
                    print("X")
                    ph += 1

                contador1 += 1

        #Caso cuando esta llena la lista
        #Se sustituye donde se encuentre el indice
        if esta_llena == True:
            lista_resultado[indice_global] = n
            if es_igual == False:
                pf += 1

        #Caso cuando hay casillas disponibles
        #El numero no esta en la lista
        if es_vacia == False and \
            es_igual == False and \
            len(lista_resultado) < parametro_largo:

            lista_resultado.append(n) 
            indice_global += 1
            pf += 1

        #Si esta llena la lista se prende la bandera   
        if len(lista_resultado) == parametro_largo:
            esta_llena = True
        
        #Resultados

        print("Indice global:")
        print(indice_global)
        
        print("Lista de resultado:")
        print(lista_resultado)

        print("Total page fault:")
        print(pf)

        print("Total page hit:")
        print(ph)

##################################################################################################################

#Se elige como victima la pagina que lleva mas tiempo en memoria
def LRU(parametros_entrada, parametro_largo):

    lista_result = []
    
    contador1 = 0
    contador2 = 0
    contador3 = 0
    pf = 0
    ph = 0
    
    lista_contadora_roja = []

    es_diferente = False


    #Recorre el arreglo de numeros
    for n in parametros_entrada:

        print("\nPagina:")
        print(n)

        #Caso segundo, cuando entra un numero igual
        contador1 = 0
        es_diferente = True

        #Recorro la lista de resultado
        for m in lista_result:

            #Es el parametro a insertar es igual al dato de la lista
            if n == m:
                lista_contadora_roja[contador1] = 1
                es_diferente = False
                print("X")
                ph += 1
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

            pf += 1

        #Caso primero, cuando se llena la memoria
        if  es_diferente == True and contador2 < parametro_largo:
            lista_result.append(n)
            lista_contadora_roja.append(1)
            contador2 += 1
            pf += 1
            
        #Imprimo corrida

        print("Lista de contadores: ")
        print(lista_contadora_roja)

        print("Lista de resultado: ")
        print(lista_result)

        print("Total page fault:")
        print(pf)

        print("Total page hit:")
        print(ph)

#################################################################################################################

#
def FIFO(parametros_entrada, parametro_largo):
    lista_resultado = []

    contador_global = 0
    lista_contadores = []
    pf = 0
    ph = 0

    #Caso primero, se llena la lista de resultado
    for n in parametros_entrada:
        
        print("\nPagina:")
        print(n)

        es_igual = False
        es_vacia = False

        #Caso cuando es vacia la lista
        if lista_resultado == []:
            lista_resultado.append(n)
            es_vacia = True
            lista_contadores.append(0)
            pf += 1

        #Si el numero a insertar es igual entonces no se hace nada
        if es_vacia == False:
            for m in lista_resultado:
                
                if m == n:
                    es_igual = True
                    print("X")
                    ph += 1

        #Caso en el que el numero es diferente.
        if es_igual == False and \
            es_vacia == False:

            largo_lista = len(lista_resultado)

            #Esta vacia alguna casilla?
            if largo_lista < parametro_largo:
                lista_resultado.append(n)
                lista_contadores.append(0)
                pf += 1
            else:

                el_mas_viejo = 0
                contador2 = 0
                
                #Revisa cual es la pagina mas vieja
                for k in lista_contadores:

                    #Caso cuando estan en el indice cero
                    if contador2 == 0:
                        el_mas_viejo = k
                        contador_global = contador2
                    else:
                        #Compara para sacar el mas viejo
                        if el_mas_viejo < k:
                            el_mas_viejo = k
                            contador_global = contador2

                    contador2 += 1

                lista_resultado[contador_global] = n
                lista_contadores[contador_global] = 0
                pf += 1


            #Coloco el indice global en el campo correspondiente
            if contador_global < parametro_largo-1:
                contador_global += 1
            else:
                contador_global = 0

        largo_lista_contadores = len(lista_contadores)

        #Aumenta contadores en general
        for j in range(0,largo_lista_contadores):
            numero = lista_contadores[j]
            lista_contadores[j] = numero + 1

        #Imprimo resultado
        print("Lista contadores:")
        print(lista_contadores)

        print("Lista de resultado:")
        print(lista_resultado)

        print("Total page fault:")
        print(pf)

        print("Total page hit:")
        print(ph)

##########################################################################################################

#
def SecondChance(parametros_entrada, parametro_largo):
    lista_resultado = []

    contador_global = 0
    lista_contadores = []
    lista_second_chance = []
    pf = 0
    ph = 0

    #Caso primero, se llena la lista de resultado
    for n in parametros_entrada:
        
        print("\nPagina:")
        print(n)

        es_igual = False
        es_vacia = False

        #Caso cuando es vacia la lista
        if lista_resultado == []:
            lista_resultado.append(n)
            es_vacia = True
            lista_contadores.append(0)
            lista_second_chance.append(0)
            pf += 1

        #Si el numero a insertar es igual entonces no se hace nada
        if es_vacia == False:

            contador3 = 0

            for m in lista_resultado:
                
                if m == n:
                    es_igual = True
                    print("X")
                    print("Hubo un second chance. Se actualiza a uno.")
                    lista_second_chance[contador3] = 1
                    ph += 1

                contador3 += 1

        #Caso en el que el numero es diferente.
        if es_igual == False and \
            es_vacia == False:

            largo_lista = len(lista_resultado)

            #Esta vacia alguna casilla?
            if largo_lista < parametro_largo:
                lista_resultado.append(n)
                lista_contadores.append(0)
                lista_second_chance.append(0)
                pf += 1

            else:

                el_mas_viejo = 0
                contador2 = 0
                
                #Revisa cual es la pagina mas vieja
                for k in lista_contadores:

                    #Caso cuando estan en el indice cero
                    if contador2 == 0 and \
                        lista_second_chance[contador2] == 0:
                        el_mas_viejo = k
                        contador_global = contador2
                    else:
                        #Compara para sacar el mas viejo
                        #Para los que tengan second chance, los omite
                        if el_mas_viejo < k and \
                            lista_second_chance[contador2] == 0:
                            el_mas_viejo = k
                            contador_global = contador2
                        
                        #Actualiza el second chance
                        if el_mas_viejo < k and \
                            lista_second_chance[contador2] == 1:
                            print("Se salvo el que tiene second chance. Se actualiza a cero.")
                            lista_second_chance[contador2] = 0

                    contador2 += 1

                lista_resultado[contador_global] = n
                lista_contadores[contador_global] = 0
                pf += 1


            #Coloco el indice global en el campo correspondiente
            if contador_global < parametro_largo-1:
                contador_global += 1
            else:
                contador_global = 0

        largo_lista_contadores = len(lista_contadores)

        #Aumenta contadores en general
        for j in range(0,largo_lista_contadores):
            numero = lista_contadores[j]
            lista_contadores[j] = numero + 1


        #Imprimo resultado
        print("Lista second chance:")
        print(lista_second_chance)

        print("Lista contadores:")
        print(lista_contadores)

        print("Lista de resultado:")
        print(lista_resultado)

        print("Total page fault:")
        print(pf)

        print("Total page hit:")
        print(ph)

##############################################################################################################

#Algoritmo de remplazo de la frecuencia menos usada
def LFU(parametros_entrada, parametro_largo):
    lista_resultado = []
    lista_frecuencias = []
    lista_senales = []
    contador = 0
    pf = 0
    ph = 0

    #Inicializo la lista de frecuencias en cero
    for i in range(0, parametro_largo):
        lista_frecuencias.append(0)

    #Inicializo lista de senales
    for o in range(0, len(parametros_entrada)):
        lista_senales.append(0)

    #Recorro paramtros de entrada
    for n in parametros_entrada:

        print("\nPagina:")
        print(n)

        es_vacia = False

        #Caso base, cuando la lista es vacia
        if lista_resultado == []:
            lista_resultado.append(n)
            lista_frecuencias[contador] = 1
            es_vacia = True
            pf += 1

        es_igual = False
        contador3 = 0

        #Caso si el numero es igual
        for m in lista_resultado:

            if m == n and es_vacia == False:
                es_igual = True
                lista_frecuencias[contador3] += 1
                print("X")
                ph += 1

            contador3 += 1 

        #Caso cuando no es igual el numero y hay casillas vacias
        if es_igual == False and \
            es_vacia == False and \
            len(lista_resultado) < parametro_largo:

            lista_resultado.append(n)
            lista_frecuencias[contador] = 1
            pf += 1

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
                    pf += 1

                contador2 += 1
            
            lista_resultado = lista_resultado_temp

        #Resultados
        
        print("Numero seleccionado a remplazar")
        print(numero_seleccionado)
                
        print("Lista de frecuencias:")
        print(lista_frecuencias)

        print("Lista de resultados:")
        print(lista_resultado)

        print("Total page fault:")
        print(pf)

        print("Total page hit:")
        print(ph)

###############################################################################################################

#                                           Pruebas

###############################################################################################################


############################################## MRU ############################################################
#Ejemplo1
#MRU([7,0,1,2,0,3,0,4,2,3,0,3,1,2,0,7,0,1], 3)
#Ejemplo2
#MRU([1,2,3,4,5,6,1,2,3,4,5,6,1,2,3,4,5,6,1,2,3,4,5,6], 4)

############################################# LRU #############################################################
#Ejemplo1
#LRU([1,2,3,4,1,2,5,1,2,3,4,5], 4)
#Ejemplo2 
#LRU([7,0,1,2,0,3,0,4,2,3,0,3,2,1,2,0,1,7,0,1], 3)

############################################# FIFO ############################################################
#Ejemplo1
#FIFO([3,2,1,3,4,1,6,2,4,3,4,2,1,4,5,2,1,3,4], 3)
#Ejemplo2
#FIFO([7,0,1,2,0,3,0,4,2,3,0,3,2,1,2,0,1,7,0,1], 3)

######################################## Second chance ########################################################
#Ejemplo1
#SecondChance([2,3,2,1,5,2,4,5,3,2,5,2], 3)
#Ejemplo2
#SecondChance([4,5,5,5,6,7,8,6,7,8,6,7,8,4,1,5,2,4,4,1], 4)

############################################ LFU ##############################################################
#Ejemplo1
#LFU([7,0,1,2,0,3,0,4,2,3,0,3,2,1,2], 3)
#Ejemplo2
#LFU([3,5,6,6,1,1,4,2,3,4], 3)

###############################################################################################################

#                                 Principios de sistemas operativos

###############################################################################################################