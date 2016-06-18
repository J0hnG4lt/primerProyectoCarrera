from tkinter import *
from random import choice
from time import sleep

# Estudiantes: Georvic Tur    --- Carnet: 12-11402
#              Ronald Becerra --- Carnet: 12-10706

#Nota: no usabamos git cuando hicimos este proyecto.
#      Lo encontramos guardado y decidimos subirlo.

#############################################################################
###################### Variables y estructuras ##############################
#############################################################################


class varGlobales :

    """Esta clase guarda valores que son usados por varias subrutinas
    y cuyos cambios deben ser vistos por cada una de ellas. Por esta razon,
    una vez que se haya creado un objeto de tipo "varGlobales", se consideraran
    estas variables como globales
    """
    
    ventana = Tk() #Ventana donde se plasma la interfaz grafica
    
    #Plano en donde se dibujan las lineas, puntitos y cuadrados
    canvas = Canvas(ventana, bg = "white", width = 528, height = 528)
    nombreJugador = "" #Nombre del jugador principal
    nombreOponente = "" #nombre del oponente (tambien si es la maquina)
    numeroPuntosX = 0 #Numero de puntitos horizontales en "canvas"
    numeroPuntosY = 0 #Numero de puntitos verticales en "canvas"
    puntuacionJugador = 0 #Puntuacion del jugador
    puntuacionOponente = 0 #Puntuacion del oponente
    colorJugador = "" #Color elegido por el jugador
    colorOponente = "" #Color elegido para el oponente
    matrizLineasHorizontales = [] #lista que almacenara un 1 si la linea 
                                  #correspondiente
                                  #a su indice ha sido marcada. De lo contrario, 
                                  #guarda 0
    matrizLineasVerticales = [] #lista que almacenara un 1 si la linea 
                                #correspondiente
                                #a su indice ha sido marcada. De lo contrario, 
                                #guarda 0
    matrizCuadrados = [] #Matriz que contendra 1 en la posicion i,j si el 
                         #cuadrado i,j
                         #hasido completado por el jugador; 2, si ha sido 
                         #completado por
                         #por el oponente; y 0, si aun no ha sido completado
    listaLineasX = [] #lista que almacena los identificadores de las lineas 
                      #horizontales
    listaLineasY = [] #lista que almacena los identificadores de las lineas 
                      #verticales
    juegaOponente = False #Variable booleana que identifica al jugador a quien le
                          #corresponde jugar
    turnoActual = 0 #variable que lleva el numero de turnos jugados

    numeroJugadores = 2 #Variable que determina si se juega con la maquina
                        # o con otro jugador
    
    
    

misVarGlobales = varGlobales() #Objeto de tipo varGlobales que almacena las
                               # variables globales usadas en el programa

                               

#############################################################################
###################### Declaracion de  Subrutinas ###########################
#############################################################################



def instrucciones()-> 'void' :
    #Pre : True
    #Post : True

    #Variables usadas
    # instrucciones : str //guarda las instrucciones que seran mostradas

    print("               BIENVENIDO AL JUEGO DE LOS PUNTITOS")
    print("")
    
    print("    Para ganar este juego, usted ha de rellenar más cuadritos que")
    print("su oponente. Para rellenar un cuadrito, usted ha de marcar las cua-")
    print("tro líneas del mismo, dándoles un click con el botón izquierdo de ")
    print("su ratón. En caso de que su oponente no sea la máquina, entonces su")
    print("oponente ha de darle click a la línea que haya elegido.")
    print("")
    print(">>> Presione ENTER para continuar.")

    
    input()


def juegoNuevoSalvado()-> 'void' :
    #Pre : True
    #Post : True

    #Variables locales usadas :
    # contestado : bool //indica si se han contestado bien las preguntas
    # archivo : file //archivo que guarda la partida que el usuario quiere
    #               //continuar
    
    contestado = False
    #Invariante
    assert(contestado == False)
    while(not contestado) :

        #Invariante
        assert(contestado == False)

        print("")
        print("Escriba (N) si quiere empezar un juego nuevo.")
        print("Escriba (G) si quiere cargar un juego guardado.")
        print("")
        respuesta = input("Respuesta: ")

        if respuesta == "N" :
            contestado = True
            pedirDatos()
            
        elif respuesta == "G" :
            contestado = True
            while(True) :
                try :
                    
                    nombreArchivo = input("Ingrese el nombre del archivo: ")
                    archivo = open(nombreArchivo, "r")
                    archivo.close()
                    assert(archivo.closed)
                    break
                except :
                    print(">>> El archivo no existe")
                
            juegoCargado(nombreArchivo)
        else :
            print(">>> Ingrese una de las opciones pedidas.")

def juegoCargado(nombre : str, misVarGlobales = misVarGlobales) -> 'void' :
    #Pre : True
    #Post : True

    #Variables globales usadas:
    # misVarGlobales.nombreJugador : str //nombre del jugador
    # misVarGlobales.nombreOponente : str //nombre del oponente
    # misVarGlobales.numeroPuntosX : int //numero de puntos horizontales
    # misVarGlobales.numeroPuntosY : int //numero de puntos verticales
    # misVarGlobales.numeroJugadores : int //1 si juega la maquina. 2 si
    #                                    //juegan dos personas
    # misVarGlobales.colorJugador : str //color escogido por el jugador
    # misVarGlobales.colorOponente : str //color escogido para el oponente
    # misVarGlobales.puntuacionOponente : int //puntos del oponente
    # misVarGlobales.puntuacionJugador : int //puntos del jugador
    # misVarGlobales.matrizLineasHorizontales : array of int
    #                                        //identifica lineas marcadas
    # misVarGlobales.matrizLineasVerticales : array of int //identifica
    #                                                   //lineas marcadas
    # misVarGlobales.matrizCuadrados : array of array of int //identifica
    #                                 //quien ha completado un cuadrado
    # misVarGlobales.listaLineasX : list //guarda identificadores de lineas
    #                                   //horizontales
    # misVarGlobales.listaLineasY : list //guarda identificadores de lineas
    #                                    //verticales
    # misVarGlobales.turnoActual : int //lleva el numero de turnos completados
    # misVarGlobales.juegaOponente : bool // True si le toca jugar al oponente

    #Variables locales usadas :
    # entrada : file //archivo que guarda un partido
    # lineas : array of str //lista que guarda las lineas de entrada
    # numeroPuntosX : str //numero de puntos horizontales
    # numeroPuntosY : str //numero de puntos verticales
    # numeroJugadores : str //numero de jugadores
    # quienJuaga : str //1 si le toca al jugador; 2, si le toca al oponente
    # nombreJugador : str //nombre del jugador
    # nombreOponente : str //nombre del oponente
    # matrizLineasHorizontalesN : array of str // filas del archivo que
    #                       // guardan la matriz de lineas horizontales
    # matrizLineasVerticalesN : array of str // filas del archivo que
    #                       // guardan la matriz de lineas verticales
    # matrizCuadradosN : array of str // filas del archivo que
    #                   //guardan la matriz de cuadrados
    # matrizLineasHorizontalesC : array of str // filas del archivo que
    #                       // guardan la matriz de lineas horizontales
    # matrizLineasVerticalesC : array of str // filas del archivo que
    #                       // guardan la matriz de lineas verticales
    # matrizCuadradosC : array of str // filas del archivo que
    #                   //guardan la matriz de cuadrados
    # jugadorEsMaquina : bool //True si el jugador es maquina
    # oponenteEsMaquina : bool //True si el oponente es maquina
    


    

    
    with open(nombre, "r") as entrada :

        lineas = entrada.readlines()
        numeroPuntosX = lineas[0]
        numeroPuntosY = lineas[1]
        numeroJugadores = lineas[2]
        quienJuega = lineas[3]
        nombreJugador = lineas[4]
        nombreOponente = lineas[5]


        numeroPuntosX = int(numeroPuntosX)
        numeroPuntosY = int(numeroPuntosY)

        matrizLineasHorizontalesN = lineas[7 : 7+numeroPuntosY]

        matrizLineasVerticalesN = lineas[numeroPuntosY+7+1 : numeroPuntosY+7\
+numeroPuntosY]

        matrizCuadradosN = lineas[numeroPuntosY+7+numeroPuntosY+1 \
: numeroPuntosY+7+1+2*numeroPuntosY+1]

    entrada.closed

    numeroJugadores = int(numeroJugadores)
    quienJuega = int(quienJuega)
    nombreJugador = nombreJugador.partition("\n")[0]
    nombreOponente = nombreOponente.partition("\n")[0]
    

    matrizLineasHorizontalesC = [j.split(sep = " ") \
for j in matrizLineasHorizontalesN]
    matrizLineasVerticalesC = [i.split(sep = " ") \
for i in matrizLineasVerticalesN]

    matrizCuadradosC = [k.split(sep = " ") for k in matrizCuadradosN]

    matrizLineasHorizontales = []
    matrizLineasVerticales = []
    

    for i in matrizLineasHorizontalesC :

        for j in i :
            
            matrizLineasHorizontales.append(int(j.partition("\n")[0]))
            

    for i in matrizLineasVerticalesC :

        for j in i :

            matrizLineasVerticales.append(int(j.partition("\n")[0]))

    jugadorEsMaquina = False
    oponenteEsMaquina = False
    if '(' in nombreJugador :
        nombreJugador = list(nombreJugador)[1:len(list(nombreJugador))-1]
        concatenacion = ""
        for i in nombreJugador :
            concatenacion = concatenacion + i
        nombreJugador = concatenacion
        jugadorEsMaquina = True

    if '(' in nombreOponente :
        nombreOponente = list(nombreOponente)[1:len(list(nombreOponente))-1]
        concatenacion = ""
        for i in nombreOponente :
            concatenacion = concatenacion + i
        nombreOponente = concatenacion
        oponenteEsMaquina = True
        
            
            

    matrizCuadrados = [[int(matrizCuadradosC[i][j]) \
for i in range(len(matrizCuadradosC))]\
                       for j in range(len(matrizCuadradosC[0]))]

    misVarGlobales.nombreJugador = nombreJugador
    misVarGlobales.nombreOponente = nombreOponente
    misVarGlobales.matrizLineasVerticales = matrizLineasVerticales
    misVarGlobales.matrizLineasHorizontales = matrizLineasHorizontales
    misVarGlobales.matrizCuadrados = matrizCuadrados

    if jugadorEsMaquina and oponenteEsMaquina :
        misVarGlobales.numeroJugadores = 0
    elif not(jugadorEsMaquina) and oponenteEsMaquina :
        misVarGlobales.numeroJugadores = 1
    elif (not jugadorEsMaquina) and (not oponenteEsMaquina) :
        misVarGlobales.numeroJugadores = 2
    elif (jugadorEsMaquina) and (not oponenteEsMaquina) :
        misVarGlobales.numeroJugadores = 1
        
        

    if quienJuega == 1 :
        misVarGlobales.juegaOponente = False
    elif quienJuega == 2 :
        misVarGlobales.juegaOponente = True

    misVarGlobales.numeroPuntosX = numeroPuntosX
    misVarGlobales.numeroPuntosY = numeroPuntosY

    misVarGlobales.colorJugador = "blue"
    misVarGlobales.colorOponente = "orange"
    
    for i in misVarGlobales.matrizCuadrados :
        for j in i :

            if j == 1 :
                misVarGlobales.puntuacionJugador += 1
            elif j == 2 :
                misVarGlobales.puntuacionOponente += 1

    for i in misVarGlobales.matrizLineasHorizontales :

        if i == 1 :

            misVarGlobales.turnoActual += 1

    for i in misVarGlobales.matrizLineasVerticales :

        if i == 1 :

            misVarGlobales.turnoActual += 1
            

    inicializarCuadrados()
                
    inicializar(True)





def salvarPartida(nombre = "juegoGuardado0.txt", objeto = misVarGlobales) -> 'void' :
    #Pre : True
    #Post : True

    #Variables globales usadas:
    # misVarGlobales.puntuacionOponente : int //puntuacion del oponente
    # misVarGlobales.puntuacionJugador : int //puntuacion del jugador
    # misVarGlobales.matrizCuadrados : array of array of int //identifica quien
                                                             #gano algun cuadrado
    # misVarGlobales.matrizLineasHorizontales : array of int //identifica lineas
    #                                                       //marcadas
    # misVarGlobales.matrizLineasVerticales : array of int //identifica lineas
    #                                                       //marcadas
    # misVarGlobales.turnoActual : int //numero de turnos completados
    # misVarGlobales.nombreJugador : str //nombre del jugador
    # misVarGlobales.nombreOponente : str //nombre del oponente
    # misVarGlobales.juegaOponente : bool // True si le toca jugar al oponente
    # misVarGlobales.numeroJugadores : int //1 si juega la maquina. 2 si juegan
    #                                        //dos personas

    #Variables locales usadas:
    # salida : file //archivo en el que se guardan los datos de la partida
    # fila : array of int // seccion de objeto.matrizLineasHorizontales
    #                     // o de objeto.matrizLineasVerticales
    #                    // o objeto.matrizCuadrados
    # filaStr : str // seccion de de objeto.matrizLineasHorizontales
    #               // o de objeto.matrizLineasVerticales
    #               //o objeto.matrizCuadrados

    while(True) :

        mp = 0
        while(True) :
            primerDigito = nombre[mp]
            if nombre[mp].isdigit() :
                break
            mp += 1
        mt = len(nombre)-1
        while(True) :
            ultimoDigito = nombre[mt]
            if nombre[mt].isdigit() :
                break
            mt -= 1


        try :
            f = open(nombre)
            nombre = "juegoGuardado"+str(int(nombre[mp:mt+1])+1)+".txt"
            f.close()
        except :
            break



    with open(nombre, "w") as salida :

        salida.write(str(objeto.numeroPuntosX) + "\n")
        salida.write(str(objeto.numeroPuntosY)+"\n")
        salida.write(str(2)+"\n")
        if objeto.juegaOponente == True :
            salida.write(str(2)+"\n")
        else :
            salida.write(str(1)+"\n")

        if objeto.numeroJugadores == 0 :
            salida.write("("+objeto.nombreJugador+")\n")
            salida.write("("+objeto.nombreOponente+")\n")
        elif objeto.numeroJugadores == 1 :
            salida.write(objeto.nombreJugador+"\n")
            salida.write("("+objeto.nombreOponente+")\n")
        elif objeto.numeroJugadores == 2 :
            salida.write(objeto.nombreJugador+"\n")
            salida.write(objeto.nombreOponente+"\n")

        salida.write("\n")

        for i in range(objeto.numeroPuntosY) :

            fila = objeto.matrizLineasHorizontales\
[i*(objeto.numeroPuntosX-1):i*(objeto.numeroPuntosX-1)+objeto.numeroPuntosX-1]

            filaStr = ""

            for j in range(len(fila)-1) :

                 filaStr = filaStr + str(fila[j]) + " "

            filaStr = filaStr+str(fila[len(fila)-1]) + "\n"

            salida.write(filaStr)

        salida.write("\n")


        for i in range(objeto.numeroPuntosY-1) :

            fila = objeto.matrizLineasVerticales\
[i*(objeto.numeroPuntosX):i*(objeto.numeroPuntosX)+objeto.numeroPuntosX]

            filaStr = ""

            for j in range(len(fila)-1) :

                 filaStr = filaStr + str(fila[j]) + " "

            filaStr = filaStr +str(fila[len(fila)-1])+ "\n"

            salida.write(filaStr)

        salida.write("\n")

        for i in range(objeto.numeroPuntosY-1) :

            filaStr = ""

            for j in range(objeto.numeroPuntosX-2) :

                filaStr = filaStr + str(objeto.matrizCuadrados[j][i]) + " "
                ultimoIndice = j

            filaStr = filaStr + str(objeto.matrizCuadrados[ultimoIndice+1][i])+"\n"

            salida.write(filaStr)

    salida.closed


def pedirDatos(misVarGlobales = misVarGlobales) -> 'void' :
    #Pre : True
    #Post : (len(misVarGlobales.nombreJugador) > 2)
    #   and (len(misVarGlobales.nombreOponente) > 2)
    #   and (misVarGlobales.nombreJugador != misVarGlobales.nombreOponente)
    #   and (misVarGlobales.colorJugador in ["blue","black","orange","red"])
    #   and (misVarGlobales.colorOponente in ["blue","black","orange","red"])
    #   and (misVarGlobales.colorJugador != misVarGlobales.colorOponente)
    #   and (20>misVarGlobales.numeroPuntosX > 2)
    #   and (20>misVarGlobales.numeroPuntosY > 2)
    #   and (misVarGlobales.numeroJugadores in [0, 1, 2] == True)
     

    #Variables globales usadas:
    # misVarGlobales.nombreJugador : str //nombre del jugador
    # misVarGlobales.nombreOponente : str //nombre del oponente
    # misVarGlobales.numeroPuntosX : int //numero de puntos horizontales
    # misVarGlobales.numeroPuntosY : int //numero de puntos verticales
    # misVarGlobales.numeroJugadores : int //1 si juega la maquina. 2 si juegan
    #                                     //dos personas
    # misVarGlobales.colorJugador : str //color escogido por el jugador
    # misVarGlobales.colorOponente : str //color escogido para el oponente

    print("")
    
    while(True) :

        try :
            misVarGlobales.nombreJugador = input("1) Ingrese su nombre: ")
            assert(len(misVarGlobales.nombreJugador) > 2)
            
        except :
            print(">>> Su nombre debe tener mas de dos caracteres")
            continue

        break

    while(True) :

        try :
            misVarGlobales.nombreOponente = input("2) Ingrese el nombre de su oponente: ")
            assert(len(misVarGlobales.nombreOponente) > 2)
            assert(misVarGlobales.nombreOponente != misVarGlobales.nombreJugador)
        except :
            print(">>> El nombre del oponente debe tener mas de dos caracteres")
            print(">>> Los nombres han de ser distintos")
            continue

        break

    while(True) :
        
        coloresDisponibles = ["azul","rojo","negro","naranja"]
        print(" - Estos son los colores: azul, rojo, negro, naranja")

        try :
            colorJugador = input("3) Ingrese su color: ")
            assert(colorJugador in coloresDisponibles)
            
        except :
            print(">>> Debe elegir uno de los colores disponibles")
            continue

        break

    while(True) :

        try :
            colorOponente = input("4) Ingrese el color de su oponente: ")
            assert(colorJugador in coloresDisponibles)
            assert(colorOponente != colorJugador)
        except :
            print(">>> Debe elegir uno de los colores disponibles")
            print(">>> Los colores elegidos han de ser distintos")
            continue


        break

    while(True):

        try :
            misVarGlobales.numeroPuntosX = int(input("5) Número de puntos por fila: "))
            assert(2<misVarGlobales.numeroPuntosX<20)
        except :
            print(">>> El número de puntitos en X ha de cumplir 2 < X < 20 ")
            continue

        break

    while(True) :

        try :
            misVarGlobales.numeroPuntosY = int(input("6) Número de puntos por columna: "))
            assert(2<misVarGlobales.numeroPuntosY<20)
        except :
            print(">>> El número de puntitos en Y, ha de cumplir 2 < X < 20 ")
            continue

        break

    while(True) :

        try :
            misVarGlobales.numeroJugadores = int(input("7) Número de jugadores vivos: "))
            assert(misVarGlobales.numeroJugadores in [0,1,2])
        except :
            print(">>> El número de jugadores vivos debe ser 0, 1 o 2")
            continue

        break

            
    coloresSistema = ["blue", "red", "black", "orange"]
    

        

    misVarGlobales.colorJugador = \
                        coloresSistema[coloresDisponibles.index(colorJugador)]
    misVarGlobales.colorOponente = \
                        coloresSistema[coloresDisponibles.index(colorOponente)]
        
        
    primerJugador()
    inicializar(False)
 
    
        
        

def primerJugador(misVarGlobales = misVarGlobales) :
    #Pre : (misVarGlobales.nombreJugador != misVarGlobales.nombreOponente)
    #Post : (misVarGlobales.juegaOponente == True) or
    #                               (misVarGlobales.juegaOponente == False)

    #Variables globales usadas:
    # misVarGlobales.nombreJugador : str //nombre del jugador
    # misVarGlobales.nombreOponente : str //nombre del oponente
    

    #Variables usadas:
    # eleccion : bool //1 si el jugador empieza el juego. De lo contrario, 2


    eleccion = choice((1,2))
    if misVarGlobales.numeroJugadores != 1 :
        
        if eleccion == 1 :
            misVarGlobales.juegaOponente = False
            print(misVarGlobales.nombreJugador+" juega primero")
        elif eleccion == 2 :
            misVarGlobales.juegaOponente = True
            print(misVarGlobales.nombreOponente+" juega primero")
        
        

        


def inicializar(juegoSalvado : bool, misVarGlobales = misVarGlobales)-> 'void' :
    #Pre : (misVarGlobales.numeroPuntosX > 2) and (misVarGlobales.numeroPuntosY > 2)
    #     and (misVarGlobales.colorJugador != misVarGlobales.colorOponente)
    #Post : all(misVarGlobales.matrizLineasHorizontales[i]==0 for i in 
    # range((misVarGlobales.numeroPuntosX-1)*(misVarGlobales.numeroPuntosY)))and
    #  all(misVarGlobales.matrizLineasVerticales[i]==0 for i in 
    # range(misVarGlobales.numeroPuntos(Y-1)*(misVarGlobales.numeroPuntosX)))and
    #  all(misVarGlobales.matrizCuadrados[i][j]==0 for i in 
    #  range(misVarGlobales.numeroPuntosX-1) for j in 
    #  range(misVarGlobales.numeroLineasY-1)) and
    #  (len(misVarGlobales.listaLineasX) == (misVarGlobales.numeroPuntosX-1)
    #                                            *(misVarGlobales.numeroPuntosY))
    # and (len(misVarGlobales.listaLineasX) == (misVarGlobales.numeroPuntosX-1)
    #                                            *(misVarGlobales.numeroPuntosY))
    #  

    #Variables globales usadas:
    # misVarGlobales.listaLineasX : list //guarda identificadores de lineas 
    #                                    //horizontales
    # misVarGlobales.listaLineasY : list //guarda identificadores de lineas 
    #                                   //verticales
    # misVarGlobales.matrizLineasHorizontales : array of int //identifica lineas
    #                                                       // marcadas
    # misVarGlobales.matrizLineasVerticales : array of int //identifica lineas 
    #                                                      //marcadas
    # misVarGlobales.matrizCuadrados : array of array of int //identifica quien
                                                             #gano algun cuadrado
    # misVarGlobales.numeroPuntosX : int //numero de puntos horizontales
    # misVarGlobales.numeroPuntosY : int //numero de puntos verticales
    # misVarGlobales.canvas : Canvas //plano en el que se dibujan las lineas

    #Variables locales usadas

    # numeroLineasX : int //numero de lineas horizontales 
    # numeroLineasY : int //numero de lineas verticales
    # longitudLineaX : int //longitud de las lineas horizontales
    # longitudLineaY : int //longitud de las lineas verticales
    # linea : int //ayuda a inicializar las partida guardadas
    # puntosEnCanvas : array of int //identificadores de puntos dibujados en
    #                               //la cuadricula


    misVarGlobales.canvas.pack(expand = TRUE, fill = BOTH)

    guardar = Button(misVarGlobales.ventana, text = "Guardar", command = salvarPartida)

    guardar.pack(side = BOTTOM, fill = BOTH)

    numeroLineasX = misVarGlobales.numeroPuntosX -1
    numeroLineasY = misVarGlobales.numeroPuntosY -1

    longitudLineaX = int(500/numeroLineasX)
    longitudLineaY = int(500/numeroLineasY)


        

    

    misVarGlobales.listaLineasX = [misVarGlobales.canvas.\
                                   create_line(i, j, i+longitudLineaX,\
                                                   j, width = 4, \
                                                   fill = "white")\
                  for j in range(10, 500+14, longitudLineaY)\
                  for i in range(10, 500-longitudLineaX+14,\
                                 longitudLineaX)]


    misVarGlobales.listaLineasY = [misVarGlobales.canvas.\
                                     create_line(i, j, i, j+longitudLineaY,\
                                                   width = 4,\
                                                   fill = "white")\
                  for j in range(10, 500-longitudLineaY+14,\
                                 longitudLineaY) \
                  for i in range(10, 500+14, longitudLineaX) ]

    puntosEnCanvas = [misVarGlobales.canvas.\
                                   create_line(i, j, i+4,\
                                                   j, width = 4, \
                                                   fill = "brown")\
                  for j in range(10, 500+14, longitudLineaY)\
                  for i in range(10, 500+14,\
                                 longitudLineaX)]
    

    if juegoSalvado == False :

        misVarGlobales.matrizLineasHorizontales = [0 for i in range(numeroLineasY+1)\
                                      for j in range(numeroLineasX) ]
        
        misVarGlobales.matrizLineasVerticales = [0 for i in range(numeroLineasY) \
                                    for j in range(numeroLineasX+1) ]
        
        misVarGlobales.matrizCuadrados = [[0 for i in range(numeroLineasY)] \
                             for j in range(numeroLineasX) ]

        

    elif juegoSalvado == True :

        for i in range(len(misVarGlobales.matrizLineasHorizontales)) :

            if misVarGlobales.matrizLineasHorizontales[i] == 1 :

                linea = misVarGlobales.listaLineasX[i]

                misVarGlobales.canvas.itemconfig(linea, fill = "gray")

        for i in range(len(misVarGlobales.matrizLineasVerticales)) :

            if misVarGlobales.matrizLineasVerticales[i] == 1 :

                linea = misVarGlobales.listaLineasY[i]

                misVarGlobales.canvas.itemconfig(linea, fill = "gray")

        

                

    misVarGlobales.canvas.bind("<ButtonPress-1>", colorearLinea)

    if misVarGlobales.juegaOponente == True :
        juegaMaquina()

    misVarGlobales.ventana.mainloop()



def comprobarLinea(event, misVarGlobales = misVarGlobales) -> 'void' :
    #Pre : True
    #Post : ((estaEnX == True) <= lineaActual in misVarGlobales.listaLineasX
    #    and indiceEnMatriz == misVarGlobales.listaLineasX.index(lineaActual)
    #    and (estaMarcada == (misVarGlobales.matrizLineasHorizontales[indiceEnMatriz]
    #    == 1)))
    #    and ((estaEnX == False) <= lineaActual in misVarGlobales.listaLineasY
    #    and indiceEnMatriz == misVarGlobales.listaLineasY.index(lineaActual)
    #    and (estaMarcada == (misVarGlobales.matrizLineasVerticales[indiceEnMatriz
    #    == 1])))

    
    #Variables globales usadas: 
    # misVarGlobales.canvas : Canvas //plano en el que se dibujan las lineas
    # misVarGlobales.listaLineasX : list //guarda identificadores de lineas 
    #                                    //horizontales
    # misVarGlobales.listaLineasY : list //guarda identificadores de lineas
    #                                    //verticales
    # misVarGlobales.matrizLineasHorizontales : array of int //identifica lineas 
    #                                                       //marcadas
    # misVarGlobales.matrizLineasVerticales : array of int //identifica lineas 
    #                                                     //marcadas



    #Variables locales usadas
    # puntuacionOponenteAnterior : int //puntuacion anterior del oponente
    # puntuacionJugadorAnterior : int //puntuacion anterior del jugador
    # matrizLineasHorizontalesAnterior : list //guarda el valor anterior de 
    #                                  //misVarGlobales.matrizLineasHorizontales
    # matrizLineasVerticalesAnterior : list  //guarda el valor anterior de 
    #                                   //misVarGlobales.matrizLineasVerticales
    # turnoAnterior : int//almacena el numero anterior de turnos
    # lineaActual : int //identificador de la linea sobre la cual se ha dado un 
    #                  //click
    # estaEnY : bool //es True si "lineaActual" es vertical
    # estaEnX : bool //es True si "lineaActual" es horizontal
    # estaMarcada : bool //es True si "lineaActual" ya ha sido marcada
    # indiceEnMatriz : int //indice de "lineaActual" en la lista de
    #                      //identificadores correspondiente

    
 

    lineaActual = misVarGlobales.canvas.find_closest(event.x, event.y)[0]

    if lineaActual in misVarGlobales.listaLineasY \
       or lineaActual in misVarGlobales.listaLineasX :

        estaEnY = (lineaActual in misVarGlobales.listaLineasY)
        estaEnX = (lineaActual in misVarGlobales.listaLineasX)


        if estaEnY :
            indiceEnMatriz = misVarGlobales.listaLineasY.index(lineaActual)

            estaMarcada = (misVarGlobales.matrizLineasVerticales\
                           [indiceEnMatriz] != 0)

            if estaMarcada :
                print("")
                print(">>> Debe seleccionar una línea no marcada")
            
        elif estaEnX :
            indiceEnMatriz = misVarGlobales.listaLineasX.index(lineaActual)

            estaMarcada = (misVarGlobales.matrizLineasHorizontales\
                           [indiceEnMatriz] != 0)

        
        
        if estaMarcada :
            print("")
            print(">>> Debe seleccionar una línea no marcada")

        return estaMarcada, indiceEnMatriz, estaEnX, lineaActual

    else :
        print("")
        print(">>> Seleccione una línea")





def colorearLinea(event, misVarGlobales = misVarGlobales)-> 'void' :
    #Pre : 0 <= misVarGlobales.turnoActual < (2*(misVarGlobales.numeroPuntosX)*
    #                                      (misVarGlobales.numeroPuntosY)
    #       - misVarGlobales.numeroPuntosX - misVarGlobales.numeroPuntosY)
    #Post : (misVarGlobales.turnoActual == turnoAnterior + 1) and 
    #   (any(misVarGlobales.matrizLineasHorizontales[i] != 
    #   matrizLineasHorizontalesAnterior[i] for i in 
    #   range(len(misVarGlobales.matrizLineasHorizontales))) or 
    #   any(misVarGlobales.matrizLineasVerticales[i] != 
    #   matrizLineasVerticalesAnterior[i] for i in 
    #   range(len(misVarGlobales.matrizLineasVerticales)))) and
    #   ((cuadradoCompleto(lineaActual, indiceEnMatriz, estaEnX) == False) and
    #   (misVarGlobales.juegaOponente == False )<= 
    #   (misVarGlobales.juegaOponente == True))   and
    #   ((cuadradoCompleto(lineaActual, indiceEnMatriz, estaEnX) == False) and
    #   (misVarGlobales.juegaOponente == True )
    #                and  (misVarGlobales.numeroJugadores == 2)<= 
    #   (misVarGlobales.juegaOponente == False)) and
    #   ((cuadradoCompleto(lineaActual, indiceEnMatriz, estaEnX)==True) and
    #   (juegaOponente == False) <= misVarGlobales.puntuacionJugador 
    #   == puntuacionJugadorAnterior +1 ) and
    #   ((cuadradoCompleto(lineaActual, indiceEnMatriz, estaEnX)==True) and
    #   (juegaOponente == True) and (misVarGlobales.numeroJugadores == 2) 
    #      <=misVarGlobales.puntuacionJugador 
    #    == puntuacionOponenteAnterior +1 )


    #Variables globales usadas :
    # misVarGlobales.numeroJugadores : int //1 si se juega con la maquina
    #                                     //2 si se juega con otra persona
    # misVarGlobales.nombreJugador : str //nombre del jugador
    # misVarGlobales.nombreOponente : str //nombre del oponente
    # misVarGlobales.listaLineasX : list //guarda identificadores de lineas 
    #                                    //horizontales
    # misVarGlobales.listaLineasY : list //guarda identificadores de lineas
    #                                    //verticales
    # misVarGlobales.matrizLineasHorizontales : array of int //identifica lineas 
    #                                                       //marcadas
    # misVarGlobales.matrizLineasVerticales : array of int //identifica lineas 
    #                                                     //marcadas
    # misVarGlobales.canvas : Canvas //plano en el que se dibujan las lineas
    # misVarGlobales.turnoActual : int //lleva el numero de turnos completados
    # misVarGlobales.juegaOponente : bool // True si le toca jugar al oponente


    #Variables locales usadas
    # puntuacionOponenteAnterior : int //puntuacion anterior del oponente
    # puntuacionJugadorAnterior : int //puntuacion anterior del jugador
    # matrizLineasHorizontalesAnterior : list //guarda el valor anterior de 
    #                                  //misVarGlobales.matrizLineasHorizontales
    # matrizLineasVerticalesAnterior : list  //guarda el valor anterior de 
    #                                   //misVarGlobales.matrizLineasVerticales
    # turnoAnterior : int//almacena el numero anterior de turnos
    # lineaActual : int //identificador de la linea sobre la cual se ha dado un 
    #                  //click
    # estaEnY : bool //es True si "lineaActual" es vertical
    # estaEnX : bool //es True si "lineaActual" es horizontal
    # estaMarcada : bool //es True si "lineaActual" ya ha sido marcada
    # indiceEnMatriz : int //indice de "lineaActual" en la lista de
    #                      //identificadores correspondiente
  
    lineaActual = misVarGlobales.canvas.find_closest(event.x, event.y)[0]

    if (lineaActual in misVarGlobales.listaLineasY \
       or lineaActual in misVarGlobales.listaLineasX) :
        

        if misVarGlobales.numeroJugadores != 0 :
            (estaMarcada, indiceEnMatriz, estaEnX, lineaActual) = comprobarLinea(event)

            
                
            if not(estaMarcada) :

                if misVarGlobales.juegaOponente == False :
                    print("")
                    print(misVarGlobales.nombreJugador + " ha jugado")
                    color = misVarGlobales.colorJugador
                else :
                    print("")
                    print(misVarGlobales.nombreOponente + " ha jugado")
                    color = misVarGlobales.colorOponente
                    
                    

                misVarGlobales.canvas.itemconfig(lineaActual, \
                                                     fill = color)

                if not estaEnX :

                    misVarGlobales.matrizLineasVerticales[indiceEnMatriz] = 1

                else :

                    misVarGlobales.matrizLineasHorizontales[indiceEnMatriz] = 1


                misVarGlobales.turnoActual += 1
                print("")
                print("Turno actual: "+str(misVarGlobales.turnoActual))
                

                if cuadradoCompleto(lineaActual, indiceEnMatriz, estaEnX) == True :

                    #colorearCuadrado(lineaActual, indiceEnMatriz, estaEnX, event)
                    
                    
                    if misVarGlobales.juegaOponente == False :
                        print("")
                        print(misVarGlobales.nombreJugador + " tiene otro turno")
                    else :
                        print("")
                        print(misVarGlobales.nombreOponente + " tiene otro turno")

                else :


                    if misVarGlobales.juegaOponente == True :

                        misVarGlobales.juegaOponente = False

                    else :

                        misVarGlobales.juegaOponente = True

                        juegaMaquina()

                    if misVarGlobales.juegaOponente == False :
                        print("")
                        print("--> Le toca a "+misVarGlobales.nombreJugador)
                    else :
                        print("")
                        print("--> Le toca a "+misVarGlobales.nombreOponente)

                        

                terminaJuego()

        elif  misVarGlobales.numeroJugadores == 0 :
            #misVarGlobales.juegaOponente = False
            
            
            juegaMaquina()
            #misVarGlobales.turnoActual += 1
            terminaJuego()

    else :

        if misVarGlobales.numeroJugadores != 0 :
            print(">>> Seleccione una línea")

        elif misVarGlobales.numeroJugadores == 0 :
            #misVarGlobales.juegaOponente = False
            juegaMaquina()
            #misVarGlobales.turnoActual += 1
            terminaJuego()

            
        


def terminaJuego(misVarGlobales = misVarGlobales)-> bool :
    #Pre : 0 < misVarGlobales.turnoActual
    #Post : haTerminado == (misVarGlobales.turnoActual ==
    #                                   (2*(misVarGlobales.numeroPuntosX)*
    #                                      (misVarGlobales.numeroPuntosY)
    #       - misVarGlobales.numeroPuntosX - misVarGlobales.numeroPuntosY))

    #Variables globales usadas :
    # misVarGlobales.numeroPuntosX : int //numero de puntos horizontales
    # misVarGlobales.numeroPuntosY : int //numero de puntos verticales
    # misVarGlobales.turnoActual : int //lleva el numero de turnos completados

    #Variables locales usadas:
    # numeroLineasX : int //numero de lineas horizontales 
    # numeroLineasY : int //numero de lineas verticales
    # numeroJugadasPosibles : int //numero de jugadas posibles
    # haTerminado : bool // es True si misVarGlobales.turnoActual es igual a
                            # numeroJugadasPosibles


    numeroLineasX = misVarGlobales.numeroPuntosX -1
    numeroLineasY = misVarGlobales.numeroPuntosY -1

    numeroJugadasPosibles = (2*numeroLineasX*numeroLineasY \
                                   + numeroLineasX + numeroLineasY)


    haTerminado = (misVarGlobales.turnoActual >= numeroJugadasPosibles)

    if haTerminado :

        determinarGanador()
        #misVarGlobales.canvas.destroy()
        if misVarGlobales.numeroJugadores == 1 :
            misVarGlobales.juegaOponente = False

        if misVarGlobales.numeroJugadores == 0 :

            return haTerminado
        


def determinarGanador(misVarGlobales = misVarGlobales)-> 'void' :
    #Pre : misVarGlobales.turnoActual == (2*(misVarGlobales.numeroPuntosX)*
    #                                      (misVarGlobales.numeroPuntosY)
    #       - misVarGlobales.numeroPuntosX - misVarGlobales.numeroPuntosY)
    #Post : oponenteGana or (not oponenteGana) or hayEmpate

    #Variables globales usadas:
    # misVarGlobales.nombreJugador : str //nombre del jugador
    # misVarGlobales.nombreOponente : str //nombre del oponente

    #Variables locales usadas:
    # oponenteGana : bool // True si la puntuacion del jugador es mayor a la del
    #                    // oponente
    # hayEmpate : bool //True si las puntuaciones son iguales



    oponenteGana = (misVarGlobales.puntuacionJugador < \
                    misVarGlobales.puntuacionOponente)

    hayEmpate = (misVarGlobales.puntuacionJugador == \
                    misVarGlobales.puntuacionOponente)

    if oponenteGana == True :        
        print("")
        print(misVarGlobales.nombreOponente + " ha ganado.")
        if misVarGlobales.numeroJugadores == 2:
            print("")
            print("Felicitaciones para "+misVarGlobales.nombreOponente)
        else:
            print("Lo sentimos.... Siga intentando.")
        

    elif hayEmpate == True :
        print("")
        print("Ha ocurrido un empate")

    else :
        print(misVarGlobales.nombreJugador + " ha ganado.")
        if misVarGlobales.numeroJugadores != 0:
            print("")
            print("Felicitaciones para "+misVarGlobales.nombreJugador)


def actualizarMatrizCuadrados(indiceEnMatriz : int, \
misVarGlobales = misVarGlobales)-> 'void' :
    #Pre : ((indiceEnMatriz < len(misVarGlobales.listaLineasX))
    #    or (indiceEnMatriz < len(misVarGlobales.listaLineasY))
    #Post : any(misVarGlobales.matrizCuadrados[i][j] != valorAnteriorMatrizCuadrados
    #       for i in range(len(misVarGlobales.matrizCuadrados))
    #       for j in range(len(misVarGlobales.matrizCuadrados[0])))

    #Variables Globales usadas:
    # misVarGlobales.matrizCuadrados : array of array of int //identifica quien
                                                             #gano algun cuadrado

    #Variables locales usadas:
    # valorAnteriorMatrizCuadrados: array of array of int //Guarda el valor
    # fila : int //numero de fila de la matriz de cuadrados
    # columna : int //numero de columna de la matriz de cuadrados

    


    columna = indiceEnMatriz % (misVarGlobales.numeroPuntosX-1)

    fila = max(j for j in range(misVarGlobales.numeroPuntosY) if indiceEnMatriz >= j*(misVarGlobales.numeroPuntosX-1) )

    if misVarGlobales.juegaOponente == True :

        misVarGlobales.matrizCuadrados[columna][fila] = 2

    elif misVarGlobales.juegaOponente == False :

        misVarGlobales.matrizCuadrados[columna][fila] = 1



    



def cuadradoCompleto(lineaActual : int, indiceEnMatriz : int, \
estaEnX : bool, misVarGlobales = misVarGlobales) -> 'void' :
    #Pre : ((lineaActual in misVarGlobales.listaLineasY) or
    #      (lineaActual in misVarGlobales.listaLineasX)) and
    #      ((misVarGlobales.listaLineasY.index(lineaActual) == indiceEnMatriz)
    #        or (misVarGlobales.listaLineasX.index(lineaActual) == indiceEnMatriz))
    #       and (lineaActual in misVarGlobales.listaLineasX == estaEnX)
    #Post :
    #(estaEnX == True) <=
    #   ((indiceEnMatriz < numeroLineasX) <=
    #               ((misVarGlobales.matrizLineasHorizontales[indiceEnMatriz \
    #                                               + numeroLineasX] == 1)\
    #               and (misVarGlobales.matrizLineasVerticales\
    #                    [indiceEnMatriz+indiceAuxiliar1-1] == 1) \
    #                and (misVarGlobales.matrizLineasVerticales\
    #  [indiceEnMatriz+indiceAuxiliar1] == 1)  <= (esCuadradoCompleto == True)))
    #
    #   and
    #
    #       numeroLineasX <= indiceEnMatriz < numeroLineasX*numeroLineasY) <=
    #               ((misVarGlobales.matrizLineasHorizontales[indiceEnMatriz \
    #                                               + numeroLineasX] == 1)\
    #               and (misVarGlobales.matrizLineasVerticales\
    #                    [indiceEnMatriz+indiceAuxiliar1-1] == 1) \
    #                and (misVarGlobales.matrizLineasVerticales\
    #    [indiceEnMatriz+indiceAuxiliar1] == 1)) <= (esCuadradoCompleto == True))
    #
    #
    #                               and
    #
    #        ((misVarGlobales.matrizLineasHorizontales[indiceEnMatriz \
    #                                               - numeroLineasX] == 1)\
    #           and (misVarGlobales.matrizLineasVerticales[indiceEnMatriz \
    #                                                       - numeroLineasX \
    #                                                    +indiceAuxiliar1-2]\
    #                             == 1) \
    #            and (misVarGlobales.matrizLineasVerticales[indiceEnMatriz \
    #                                                        - numeroLineasX \
    #                                                    +indiceAuxiliar1-1]\
    #                           == 1) <= (esCuadradoCompleto == True))
    #
    #       and
    #
    #       (numeroLineasX*numeroLineasY <= indiceEnMatriz ) <= 
    #
    #               ((misVarGlobales.matrizLineasHorizontales[indiceEnMatriz \
    #                                                - numeroLineasX] == 1)\
    #                and (misVarGlobales.matrizLineasVerticales[indiceEnMatriz \
    #                                                    - numeroLineasX \
    #                                                    +indiceAuxiliar1-2]\
    #                     == 1) \
    #           and (misVarGlobales.matrizLineasVerticales[indiceEnMatriz \
    #                                                        - numeroLineasX \
    #                                                       +indiceAuxiliar1-1]\
    #                   == 1) <= (esCuadradoCompleto == True))
    #
    #
    #
    #
    #   and
    #
    #   (estaEnX == False) <= 
    #
    #               (((indiceEnMatriz +1) % (numeroLineasX+1) != 0) \
    #           and (indiceEnMatriz % (numeroLineasX +1) != 0)    <=
    #
    #
    #               ((misVarGlobales.matrizLineasHorizontales[indiceEnMatriz \
    #                                               - indiceAuxiliar2] == 1)\
    #               and (misVarGlobales.matrizLineasHorizontales[indiceEnMatriz \
    #                                - indiceAuxiliar2 + numeroLineasX] == 1)\
    #         and (misVarGlobales.matrizLineasVerticales[indiceEnMatriz +1] == 1)
    #                                            <=(esCuadradoCompleto == True)))
    #
    #
    #               and
    #
    #
    #               (misVarGlobales.matrizLineasHorizontales[indiceEnMatriz \
    #                                             - indiceAuxiliar2-1] == 1)\
    #               and (misVarGlobales.matrizLineasHorizontales[indiceEnMatriz \
    #                           - indiceAuxiliar2-1 + numeroLineasX] == 1)\
    #          and (misVarGlobales.matrizLineasVerticales[indiceEnMatriz-1] == 1)
    #
    #                                          <= ((esCuadradoCompleto == True))
    #
    #
    #           and
    #
    #           ((indiceEnMatriz +1) % (numeroLineasX+1) == 0) <=
    #
    #
    #            ( (misVarGlobales.matrizLineasHorizontales[indiceEnMatriz \
    #                                                 - indiceAuxiliar2-1] == 1)\
    #               and (misVarGlobales.matrizLineasHorizontales[indiceEnMatriz \
    #                             - indiceAuxiliar2-1 + numeroLineasX] == 1)\
    #          and (misVarGlobales.matrizLineasVerticales[indiceEnMatriz-1] == 1)
    #
    #                                        <= (esCuadradoCompleto == True))
    #           and
    #
    #           (indiceEnMatriz % (numeroLineasX +1) == 0) <= 
    #
    #
    #               ( misVarGlobales.matrizLineasHorizontales[indiceEnMatriz \
    #                                             - indiceAuxiliar2] == 1)\
    #               and (misVarGlobales.matrizLineasHorizontales[indiceEnMatriz \
    #                                - indiceAuxiliar2 + numeroLineasX] == 1)\
    #         and (misVarGlobales.matrizLineasVerticales[indiceEnMatriz +1] == 1)
    #
    #                                        <= (esCuadradoCompleto == True))


    #Variables globales usadas:
    # misVarGlobales.numeroPuntosX : int //numero de puntos horizontales
    # misVarGlobales.numeroPuntosY : int //numero de puntos verticales
    # misVarGlobales.matrizCuadrados : array of array of int //identifica quien
                                                             #gano algun cuadrado
    # misVarGlobales.matrizLineasHorizontales : array of int //identifica lineas
    #                                                        //marcadas
    # misVarGlobales.matrizLineasVerticales : array of int //identifica lineas
    #                                                        //marcadas

    #Variables locales usadas:
    # valorAnteriorMatrizCuadrados: array of array of int //Guarda el valor
    #                                                       //de la matriz
    #                           //misVarGlobales.matrizCuadrados para
    #                                                      //reservar el valor
    #                           //de esta antes de que se asigne un punto si
    #                           //esCuadradoCompleto es True.
    # numeroLineasX : int //numero de lineas horizontales 
    # numeroLineasY : int //numero de lineas verticales
    # x0, y0, x1, y1 : int //coordenadas de la linea actual
    # estaEnX : bool //True si linea actual es horizontal
    # lineaActual : int //identificador de la linea elegida
    # indiceAuxiliar1 : int //ayuda a identificar las lineas vecinas
    #                       // si la actual es horizontal
    # indiceAuxiliar2 : int //ayuda a identificar las lineas vecinas
    #                      // si la actual es vertical
    # esCuadradoCompleto : bool // True si hay un cuadrado completo
    #                         // que tenga a lineaActual
    


    if misVarGlobales.juegaOponente == True :
        color = misVarGlobales.colorOponente
    elif misVarGlobales.juegaOponente == False :
        color = misVarGlobales.colorJugador

    esCuadradoCompleto = False

    
    numeroLineasX = misVarGlobales.numeroPuntosX -1
    numeroLineasY = misVarGlobales.numeroPuntosY -1

    longitudLineaX = int(500/numeroLineasX)
    longitudLineaY = int(500/numeroLineasY)



    (x0, y0, x1, y1) = misVarGlobales.canvas.coords(lineaActual)

    

    if estaEnX == True :

        indiceAuxiliar1 = min(j for j in range(numeroLineasY+50) \
                                 if (indiceEnMatriz < j*numeroLineasX))


        if indiceEnMatriz < numeroLineasX :


            if (misVarGlobales.matrizLineasHorizontales[indiceEnMatriz \
                                                       + numeroLineasX] == 1)\
               and (misVarGlobales.matrizLineasVerticales\
                    [indiceEnMatriz+indiceAuxiliar1-1] == 1) \
                and (misVarGlobales.matrizLineasVerticales\
                    [indiceEnMatriz+indiceAuxiliar1] == 1) :

                esCuadradoCompleto = True
                actualizarMatrizCuadrados(indiceEnMatriz)
                sumarPuntos()
                misVarGlobales.canvas.create_rectangle(x0, y0+longitudLineaY,\
 x0+longitudLineaX, y0, fill=color)
                

        elif numeroLineasX <= indiceEnMatriz < numeroLineasX*numeroLineasY :


            if (misVarGlobales.matrizLineasHorizontales[indiceEnMatriz \
                                                       + numeroLineasX] == 1)\
               and (misVarGlobales.matrizLineasVerticales\
                    [indiceEnMatriz+indiceAuxiliar1-1] == 1) \
                and (misVarGlobales.matrizLineasVerticales\
                    [indiceEnMatriz+indiceAuxiliar1] == 1) :

                esCuadradoCompleto = True
                actualizarMatrizCuadrados(indiceEnMatriz)
                sumarPuntos()
                misVarGlobales.canvas.create_rectangle(x0, y0, x0+longitudLineaX,\
 y0+longitudLineaY, fill=color)


            if (misVarGlobales.matrizLineasHorizontales[indiceEnMatriz \
                                                          - numeroLineasX] == 1)\
                and (misVarGlobales.matrizLineasVerticales[indiceEnMatriz \
                                                           - numeroLineasX \
                                                           +indiceAuxiliar1-2]\
                     == 1) \
                and (misVarGlobales.matrizLineasVerticales[indiceEnMatriz \
                                                           - numeroLineasX \
                                                           +indiceAuxiliar1-1]\
                     == 1) :

                esCuadradoCompleto = True
                actualizarMatrizCuadrados(indiceEnMatriz-numeroLineasX)
                sumarPuntos()
                misVarGlobales.canvas.create_rectangle(x0, y0-longitudLineaY, \
x0+longitudLineaX, y0, fill=color)


        elif numeroLineasX*numeroLineasY <= indiceEnMatriz :

            if (misVarGlobales.matrizLineasHorizontales[indiceEnMatriz \
                                                          - numeroLineasX] == 1)\
                and (misVarGlobales.matrizLineasVerticales[indiceEnMatriz \
                                                           - numeroLineasX \
                                                           +indiceAuxiliar1-2]\
                     == 1) \
                and (misVarGlobales.matrizLineasVerticales[indiceEnMatriz \
                                                           - numeroLineasX \
                                                           +indiceAuxiliar1-1]\
                     == 1) :

                esCuadradoCompleto = True
                actualizarMatrizCuadrados(indiceEnMatriz - numeroLineasX)
                sumarPuntos()
                misVarGlobales.canvas.create_rectangle(x0, y0-longitudLineaY,\
 x0+longitudLineaX, y0, fill=color)


    elif estaEnX == False :

        indiceAuxiliar2 = max(j for j in range(numeroLineasY+50) \
                                 if j*(numeroLineasX+1)<= indiceEnMatriz)

        if ((indiceEnMatriz +1) % (numeroLineasX+1) != 0) \
           and (indiceEnMatriz % (numeroLineasX +1) != 0) :

            if (misVarGlobales.matrizLineasHorizontales[indiceEnMatriz \
                                                       - indiceAuxiliar2] == 1)\
               and (misVarGlobales.matrizLineasHorizontales[indiceEnMatriz \
                                - indiceAuxiliar2 + numeroLineasX] == 1)\
               and (misVarGlobales.matrizLineasVerticales[indiceEnMatriz +1] == 1):

                   esCuadradoCompleto = True
                   actualizarMatrizCuadrados(indiceEnMatriz - indiceAuxiliar2)
                   sumarPuntos()
                   misVarGlobales.canvas.create_rectangle(x0, y0, x0+longitudLineaX,\
 y0+longitudLineaY, fill=color)

                   


            if (misVarGlobales.matrizLineasHorizontales[indiceEnMatriz \
                                                       - indiceAuxiliar2-1] == 1)\
               and (misVarGlobales.matrizLineasHorizontales[indiceEnMatriz \
                                - indiceAuxiliar2-1 + numeroLineasX] == 1)\
               and (misVarGlobales.matrizLineasVerticales[indiceEnMatriz-1] == 1):

                   esCuadradoCompleto = True
                   actualizarMatrizCuadrados(indiceEnMatriz - indiceAuxiliar2-1)
                   sumarPuntos()
                   misVarGlobales.canvas.create_rectangle(x0-longitudLineaX, y0,\
 x0, y0+longitudLineaY, fill=color)


        elif  ((indiceEnMatriz +1) % (numeroLineasX+1) == 0) :

            if (misVarGlobales.matrizLineasHorizontales[indiceEnMatriz \
                                                       - indiceAuxiliar2-1] == 1)\
               and (misVarGlobales.matrizLineasHorizontales[indiceEnMatriz \
                                - indiceAuxiliar2-1 + numeroLineasX] == 1)\
               and (misVarGlobales.matrizLineasVerticales[indiceEnMatriz-1] == 1):

                   esCuadradoCompleto = True
                   actualizarMatrizCuadrados(indiceEnMatriz - indiceAuxiliar2-1)
                   sumarPuntos()
                   misVarGlobales.canvas.create_rectangle(x0-longitudLineaX, y0,\
 x0, y0+longitudLineaY, fill=color)


        elif (indiceEnMatriz % (numeroLineasX +1) == 0) :

            if (misVarGlobales.matrizLineasHorizontales[indiceEnMatriz \
                                                       - indiceAuxiliar2] == 1)\
               and (misVarGlobales.matrizLineasHorizontales[indiceEnMatriz \
                                - indiceAuxiliar2 + numeroLineasX] == 1)\
               and (misVarGlobales.matrizLineasVerticales[indiceEnMatriz +1] == 1):

                   esCuadradoCompleto = True
                   actualizarMatrizCuadrados(indiceEnMatriz - indiceAuxiliar2)
                   sumarPuntos()
                   misVarGlobales.canvas.create_rectangle(x0, y0, \
x0+longitudLineaX, y0+longitudLineaY, fill=color)


            

    return esCuadradoCompleto



def inicializarCuadrados(misVarGlobales = misVarGlobales) -> 'void' :
    #Pre : True
    #Post : True

    #Variables globales usadas :
    # misVarGlobales.canvas : Canvas //plano en el que se dibujan las lineas
    # misVarGlobales.matrizCuadrados : array of array of int //identifica quien
                                                             #gano algun cuadrado
    # misVarGlobales.colorJugador : str //color escogido por el jugador
    # misVarGlobales.colorOponente : str //color escogido para el oponente

    #Variables locales usadas:
    # columna : int // dummy variable
    # fila : int //dummy variable
    # numeroLineasX : int //numero de lineas horizontales
    # numeroLineasY : int //numero de lineas verticales
    # longitudLineasX : int //longitud de cada linea horizontal
    # longitud LineasY : int //longitud de cada linea vertical


    numeroLineasX = misVarGlobales.numeroPuntosX -1
    numeroLineasY = misVarGlobales.numeroPuntosY -1

    longitudLineaX = int(500/numeroLineasX)
    longitudLineaY = int(500/numeroLineasY)




    columna = 0

    for y in misVarGlobales.matrizCuadrados :

        fila = 0
        
        for x in y :


            if x == 1 :

                misVarGlobales.canvas.create_rectangle(10+columna*longitudLineaX,\
 10+fila*longitudLineaY,\
                     10+(columna+1)*longitudLineaX, 10+(fila+1)*longitudLineaY,\
                                                       fill = misVarGlobales.colorJugador)

            elif x == 2 :

                misVarGlobales.canvas.create_rectangle(10+columna*longitudLineaX,\
 10+fila*longitudLineaY,\
                      10+(columna+1)*longitudLineaX, 10+(fila+1)*longitudLineaY,\
                                             fill = misVarGlobales.colorOponente)

            fila += 1

        columna += 1 

                

        

def sumarPuntos(misVarGlobales = misVarGlobales)-> 'void' :
    #Pre: (0 < misVarGlobales.turnoActual) and (misVarGlobales.numeroJugadores == 2)
    #Post : 
    #   ((misVarGlobales.juegaOponente == True)<=(
    #   misVarGlobales.puntuacionOponente == puntuacionOponenteAnterior +1))and
    #   ((misVarGlobales.juegaOponente == False)<=
    #   (misVarGlobales.puntuacionJugador == puntuacionJugadorAnterior +1))

    #Variables globales usadas
    # misVarGlobales.nombreJugador : str //nombre del jugador
    # misVarGlobales.nombreOponente : str //nombre del oponente
    # misVarGlobales.juegaOponente : bool // True si le toca jugar al oponente
    # misVarGlobales.puntuacionOponente : int //puntuacion del oponente
    # misVarGlobales.puntuacionJugador : int //puntuacion del jugador

    #Variables locales usadas:
    # puntuacionJugadorAnterior : int //guarda la puntuacion del jugador antes
    #                               // de modificarla
    # puntuacionOponenteAnterior : int //guarda la puntuacion del oponente antes
    #                               // de modificarla
    

    if misVarGlobales.juegaOponente == False :

        misVarGlobales.puntuacionJugador += 1

        print(misVarGlobales.nombreJugador + " tiene " + \
              str(misVarGlobales.puntuacionJugador) + " puntos")

    else :

        misVarGlobales.puntuacionOponente += 1

        print(misVarGlobales.nombreOponente + " tiene " + \
              str(misVarGlobales.puntuacionOponente) + " puntos")


def buscaCuadradoCasiCompleto(color : str, misVarGlobales = misVarGlobales)-> 'void' :
    #Pre : (misVarGlobales.oponenteJuega == True) and
    #      (misVarGlobales.numeroJugadores == 1) and
    #      (misVarGlobales.turnoActual < 0 <= misVarGlobales.turnoActual < (2*
    #      (misVarGlobales.numeroPuntosX)*
    #                         (misVarGlobales.numeroPuntosY)
    #       - misVarGlobales.numeroPuntosX - misVarGlobales.numeroPuntosY))
    #Post : 
    #(
    #any((matrizLineasHorizontalesAnterior[int(i*(numeroLineasX)+j)] == 1) and
    #(matrizLineasHorizontalesAnterior[int((i+1)*(numeroLineasX)+j)] == 1) and
    #(matrizLineasVerticalesAnterior[int(i*(numeroLineasX+1)+j)] == 1) and
    #(matrizLineasVerticalesAnterior[int(i*(numeroLineasX+1)+j+1)] == 0)
    #<= (misVarGlobales.matrizLineasVerticales[int(i*(numeroLineasX+1)+j+1)] == 1))
    #
    #          and
    #
    #any((matrizLineasHorizontalesAnterior[int(i*(numeroLineasX)+j)] == 1) and
    #(matrizLineasHorizontalesAnterior[int((i+1)*(numeroLineasX)+j)] == 1) and
    #(matrizLineasVerticalesAnterior[int(i*(numeroLineasX+1)+j)] == 0) and
    #(matrizLineasVerticalesAnterior[int(i*(numeroLineasX+1)+j+1)] == 1)
    #<= (misVarGlobales.matrizLineasVerticales[int(i*(numeroLineasX+1)+j)] == 1))
    #
    #          and
    #
    #any((matrizLineasHorizontalesAnterior[int(i*(numeroLineasX)+j)] == 1) and
    #(matrizLineasHorizontalesAnterior[int((i+1)*(numeroLineasX)+j)] == 0) and
    #(matrizLineasVerticalesAnterior[int(i*(numeroLineasX+1)+j)] == 1) and
    #(matrizLineasVerticalesAnterior[int(i*(numeroLineasX+1)+j+1)] == 1)
    #<= (misVarGlobales.matrizLineasHorizontales[int((i+1)*(numeroLineasX)+j)] == 1))
    #
    #          and
    #
    #any((matrizLineasHorizontalesAnterior[int(i*(numeroLineasX)+j)] == 0) and
    #(matrizLineasHorizontalesAnterior[int((i+1)*(numeroLineasX)+j)] == 1) and
    #(matrizLineasVerticalesAnterior[int(i*(numeroLineasX+1)+j)] == 1) and
    #(matrizLineasVerticalesAnterior[int(i*(numeroLineasX+1)+j+1)] == 1)
    #<= (misVarGlobales.matrizLineasHorizontales[int(i*(numeroLineasX)+j)] == 1))
    # )

    #Variables Globales usadas:

    # misVarGlobales.numeroJugadores : int //1 si se juega con la maquina
    #                                     //2 si se juega con otra persona
    # misVarGlobales.listaLineasX : list //guarda identificadores de lineas 
    #                                    //horizontales
    # misVarGlobales.listaLineasY : list //guarda identificadores de lineas 
    #                                    //verticales
    # misVarGlobales.matrizLineasHorizontales : array of int //identifica lineas 
    #                                                       //marcadas
    # misVarGlobales.matrizLineasVerticales : array of int //identifica lineas 
    #                                                     //marcadas
    # misVarGlobales.canvas : Canvas //plano en el que se dibujan las lineas
    # misVarGlobales.turnoActual : int //lleva el numero de turnos completados
    # misVarGlobales.juegaOponente : bool // True si le toca jugar al oponente
    # misVarGlobales.turnoActual : int //indica el numero de turnos pasados
    # misVarGlobales.numeroPuntosX : int //numero de puntos horizontales
    # misVarGlobales.numeroPuntosY : int //numero de puntos verticales

    #Variables locales usadas

    # numeroLineasX : int //numero de lineas horizontales
    # puntuacionOponenteAnterior : int //puntuacion anterior del oponente
    # matrizCuadradosAnterior : array of array of int //valor de 
    #            //misVarGlobales.matrizCuadrados antes de entrar a juegaMaquina
    # matrizLineasHorizontalesAnterior : list //guarda el valor anterior de 
    #                                  //misVarGlobales.matrizLineasHorizontales
    # matrizLineasVerticalesAnterior : list  //guarda el valor anterior de 
    #                                   //misVarGlobales.matrizLineasVerticales
    # estaEnX : bool //es True si "lineaActual" es horizontal
    # estaMarcada : bool //es True si "lineaActual" ya ha sido marcada
    # indiceEnMatriz : int //indice de "lineaActual" en la lista de
                            # identificadores correspondiente
    # lineaActual : int //identificador de la linea que juegaMaquina ha  
    #                   //seleccionado
    # x0, y0, x1, y1 : int //coordenadas de la linea actual
    # noSalirDeBucle : bool //True si no se encontro un cuadrado casi completo
    #                       //False si se encontro uno



    noSalirDeBucle = True

    numeroLineasX = misVarGlobales.numeroPuntosX -1
    numeroLineasY = misVarGlobales.numeroPuntosY -1

    longitudLineaX = int(500/numeroLineasX)
    longitudLineaY = int(500/numeroLineasY)


    #Se busca una linea con la que se pueda completar de una vez algun cuadrado
    for i in range(numeroLineasY) :
        for j in range(numeroLineasX) :
            if (misVarGlobales.matrizLineasHorizontales\
[int(i*(numeroLineasX)+j)] == 1) and\
               (misVarGlobales.matrizLineasHorizontales\
[int((i+1)*(numeroLineasX)+j)] == 1) and\
               (misVarGlobales.matrizLineasVerticales\
[int(i*(numeroLineasX+1)+j)] == 1) and\
               (misVarGlobales.matrizLineasVerticales\
[int(i*(numeroLineasX+1)+j+1)] == 0) :

                misVarGlobales.canvas.itemconfig(misVarGlobales.listaLineasY\
[int(i*(numeroLineasX+1)+j+1)],\
                                       fill = color)
                misVarGlobales.canvas.update_idletasks()

                misVarGlobales.matrizLineasVerticales[int(i*(numeroLineasX+1)+j+1)] = 1

                lineaActual = misVarGlobales.listaLineasY[int(i*(numeroLineasX+1)+j)]

                (x0, y0, x1, y1) = misVarGlobales.canvas.coords(lineaActual)

                misVarGlobales.canvas.create_rectangle(x0, y0, x0+longitudLineaX,\
 y0+longitudLineaY, fill = color)

                sumarPuntos()

                actualizarMatrizCuadrados(int(i*(numeroLineasX)+j))
              

                noSalirDeBucle = False
                #break
                

                if (j+1 < numeroLineasX) and (misVarGlobales.matrizCuadrados[j+1][i] == 0):

                    if (misVarGlobales.matrizLineasHorizontales\
    [int((i)*(numeroLineasX)+j+1)] == 1) and\
                     (misVarGlobales.matrizLineasHorizontales\
    [int((i+1)*(numeroLineasX)+j+1)] == 1) and\
                     (misVarGlobales.matrizLineasVerticales\
    [int((i)*(numeroLineasX+1)+j+1)] == 1) and\
                     (misVarGlobales.matrizLineasVerticales\
    [int((i)*(numeroLineasX+1)+j+1+1)] == 1) :



                        misVarGlobales.canvas.itemconfig(misVarGlobales.listaLineasY\
    [int(i*(numeroLineasX+1)+j)],\
                                           fill = color)
                        misVarGlobales.canvas.update_idletasks()

                        misVarGlobales.matrizLineasVerticales[int(i*(numeroLineasX+1)+j+1)] = 1

                        lineaActual = misVarGlobales.listaLineasY[int(i*(numeroLineasX+1)+j+1)]

                        (x0, y0, x1, y1) = misVarGlobales.canvas.coords(lineaActual)

                        misVarGlobales.canvas.create_rectangle(x0, y0, x0+longitudLineaX,\
     y0+longitudLineaY, fill = color)

                        sumarPuntos()

                        actualizarMatrizCuadrados(int(i*(numeroLineasX)+j+1))

                        noSalirDeBucle = False
                        break

                

            elif (misVarGlobales.matrizLineasHorizontales\
[int(i*(numeroLineasX)+j)] == 1) and\
                 (misVarGlobales.matrizLineasHorizontales\
[int((i+1)*(numeroLineasX)+j)] == 1) and\
                 (misVarGlobales.matrizLineasVerticales\
[int(i*(numeroLineasX+1)+j)] == 0) and\
                 (misVarGlobales.matrizLineasVerticales\
[int(i*(numeroLineasX+1)+j+1)] == 1) :

                misVarGlobales.canvas.itemconfig(misVarGlobales.listaLineasY\
[int(i*(numeroLineasX+1)+j)],\
                                       fill = color)
                misVarGlobales.canvas.update_idletasks()

                misVarGlobales.matrizLineasVerticales[int(i*(numeroLineasX+1)+j)] = 1

                lineaActual = misVarGlobales.listaLineasY[int(i*(numeroLineasX+1)+j)]

                (x0, y0, x1, y1) = misVarGlobales.canvas.coords(lineaActual)

                misVarGlobales.canvas.create_rectangle(x0, y0, x0+longitudLineaX,\
 y0+longitudLineaY, fill = color)

                sumarPuntos()

                actualizarMatrizCuadrados(int(i*(numeroLineasX)+j))

                noSalirDeBucle = False
                #break

                if (j-1 >= 0) and (misVarGlobales.matrizCuadrados[j-1][i] == 0) :

                    if (misVarGlobales.matrizLineasHorizontales\
    [int(i*(numeroLineasX)+j-1)] == 1) and\
                   (misVarGlobales.matrizLineasHorizontales\
    [int((i+1)*(numeroLineasX)+j-1)] == 1) and\
                   (misVarGlobales.matrizLineasVerticales\
    [int(i*(numeroLineasX+1)+j-1)] == 1) and\
                   (misVarGlobales.matrizLineasVerticales\
    [int(i*(numeroLineasX+1)+j+1-1)] == 1) :

                        misVarGlobales.canvas.itemconfig(misVarGlobales.listaLineasY\
    [int(i*(numeroLineasX+1)+j+1)],\
                                           fill = color)
                        misVarGlobales.canvas.update_idletasks()

                        misVarGlobales.matrizLineasVerticales[int(i*(numeroLineasX+1)+j+1-1)] = 1

                        lineaActual = misVarGlobales.listaLineasY[int(i*(numeroLineasX+1)+j-1)]

                        (x0, y0, x1, y1) = misVarGlobales.canvas.coords(lineaActual)

                        misVarGlobales.canvas.create_rectangle(x0, y0, x0+longitudLineaX,\
     y0+longitudLineaY, fill = color)

                        sumarPuntos()

                        actualizarMatrizCuadrados(int(i*(numeroLineasX)+j-1))
                  

                        noSalirDeBucle = False
                        break
                    

                
            elif (misVarGlobales.matrizLineasHorizontales\
[int(i*(numeroLineasX)+j)] == 1) and\
                 (misVarGlobales.matrizLineasHorizontales\
[int((i+1)*(numeroLineasX)+j)] == 0) and\
                 (misVarGlobales.matrizLineasVerticales\
[int(i*(numeroLineasX+1)+j)] == 1) and\
                 (misVarGlobales.matrizLineasVerticales\
[int(i*(numeroLineasX+1)+j+1)] == 1) :

                misVarGlobales.canvas.itemconfig(misVarGlobales.listaLineasX\
[int((i+1)*(numeroLineasX)+j)],\
                                       fill = color)
                misVarGlobales.canvas.update_idletasks()

                misVarGlobales.matrizLineasHorizontales[int((i+1)*(numeroLineasX)+j)] = 1

                lineaActual = misVarGlobales.listaLineasY[int(i*(numeroLineasX+1)+j)]

                (x0, y0, x1, y1) = misVarGlobales.canvas.coords(lineaActual)

                misVarGlobales.canvas.create_rectangle(x0, y0, x0+longitudLineaX,\
 y0+longitudLineaY, fill = color)

                sumarPuntos()

                actualizarMatrizCuadrados(int(i*(numeroLineasX)+j))


                noSalirDeBucle = False
                #break

                if (i+1 < numeroLineasY) and (misVarGlobales.matrizCuadrados[j][i+1] == 0):


                    if (misVarGlobales.matrizLineasHorizontales\
    [int((i+1)*(numeroLineasX)+j)] == 1) and\
                     (misVarGlobales.matrizLineasHorizontales\
    [int((i+1+1)*(numeroLineasX)+j)] == 1) and\
                     (misVarGlobales.matrizLineasVerticales\
    [int((i+1)*(numeroLineasX+1)+j)] == 1) and\
                     (misVarGlobales.matrizLineasVerticales\
    [int((i+1)*(numeroLineasX+1)+j+1)] == 1) :

                        misVarGlobales.canvas.itemconfig(misVarGlobales.listaLineasX\
    [int((i+1)*(numeroLineasX)+j)],\
                                           fill = color)
                        misVarGlobales.canvas.update_idletasks()

                        misVarGlobales.matrizLineasHorizontales[int((i+1)*(numeroLineasX)+j)] = 1

                        lineaActual = misVarGlobales.listaLineasY[int((i+1)*(numeroLineasX+1)+j)]

                        (x0, y0, x1, y1) = misVarGlobales.canvas.coords(lineaActual)

                        misVarGlobales.canvas.create_rectangle(x0, y0, x0+longitudLineaX,\
     y0+longitudLineaY, fill = color)

                        sumarPuntos()

                        actualizarMatrizCuadrados(int((i+1)*(numeroLineasX)+j))

                        noSalirDeBucle = False
                        break



                
            elif (misVarGlobales.matrizLineasHorizontales\
[int(i*(numeroLineasX)+j)] == 0) and\
                 (misVarGlobales.matrizLineasHorizontales\
[int((i+1)*(numeroLineasX)+j)] == 1) and\
                 (misVarGlobales.matrizLineasVerticales\
[int(i*(numeroLineasX+1)+j)] == 1) and\
                 (misVarGlobales.matrizLineasVerticales\
[int(i*(numeroLineasX+1)+j+1)] == 1) :

                misVarGlobales.canvas.itemconfig(misVarGlobales.listaLineasX\
[int(i*(numeroLineasX)+j)],\
                                       fill = color)
                misVarGlobales.canvas.update_idletasks()

                misVarGlobales.matrizLineasHorizontales[int(i*(numeroLineasX)+j)] = 1

                lineaActual = misVarGlobales.listaLineasY[int(i*(numeroLineasX+1)+j)]

                (x0, y0, x1, y1) = misVarGlobales.canvas.coords(lineaActual)

                misVarGlobales.canvas.create_rectangle(x0, y0, x0+longitudLineaX,\
 y0+longitudLineaY, fill = color)

                sumarPuntos()

                actualizarMatrizCuadrados(int(i*(numeroLineasX)+j))

                noSalirDeBucle = False
                #break

                if (0<=i - 1) and (misVarGlobales.matrizCuadrados[j][i-1] == 0) :


                    if (misVarGlobales.matrizLineasHorizontales\
    [int((i-1)*(numeroLineasX)+j)] == 1) and\
                     (misVarGlobales.matrizLineasHorizontales\
    [int((i+1-1)*(numeroLineasX)+j)] == 1) and\
                     (misVarGlobales.matrizLineasVerticales\
    [int((i-1)*(numeroLineasX+1)+j)] == 1) and\
                     (misVarGlobales.matrizLineasVerticales\
    [int((i-1)*(numeroLineasX+1)+j+1)] == 1) :

                        misVarGlobales.canvas.itemconfig(misVarGlobales.listaLineasX\
    [int((i+1-1)*(numeroLineasX)+j)],\
                                           fill = color)
                        misVarGlobales.canvas.update_idletasks()

                        misVarGlobales.matrizLineasHorizontales[int((i+1-1)*(numeroLineasX)+j)] = 1

                        lineaActual = misVarGlobales.listaLineasY[int((i-1)*(numeroLineasX+1)+j)]

                        (x0, y0, x1, y1) = misVarGlobales.canvas.coords(lineaActual)

                        misVarGlobales.canvas.create_rectangle(x0, y0, x0+longitudLineaX,\
     y0+longitudLineaY, fill = color)

                        sumarPuntos()

                        actualizarMatrizCuadrados(int((i-1)*(numeroLineasX)+j))


                        noSalirDeBucle = False
                        break



            if not(noSalirDeBucle) :
                break
            
        if not(noSalirDeBucle) :
            break

    return noSalirDeBucle



def juegaMaquina(misVarGlobales = misVarGlobales)-> 'void' :
    #Pre : (misVarGlobales.oponenteJuega == True) and
    #      (misVarGlobales.numeroJugadores == 1) and
    #      (misVarGlobales.turnoActual < 0 <= misVarGlobales.turnoActual < (2*
    #      (misVarGlobales.numeroPuntosX)*
    #                         (misVarGlobales.numeroPuntosY)
    #       - misVarGlobales.numeroPuntosX - misVarGlobales.numeroPuntosY))
    #Post : 
    #(
    #any((matrizLineasHorizontalesAnterior[int(i*(numeroLineasX)+j)] == 1) and
    #(matrizLineasHorizontalesAnterior[int((i+1)*(numeroLineasX)+j)] == 1) and
    #(matrizLineasVerticalesAnterior[int(i*(numeroLineasX+1)+j)] == 1) and
    #(matrizLineasVerticalesAnterior[int(i*(numeroLineasX+1)+j+1)] == 0)
    #<= (misVarGlobales.matrizLineasVerticales[int(i*(numeroLineasX+1)+j+1)] == 1))
    #
    #          and
    #
    #any((matrizLineasHorizontalesAnterior[int(i*(numeroLineasX)+j)] == 1) and
    #(matrizLineasHorizontalesAnterior[int((i+1)*(numeroLineasX)+j)] == 1) and
    #(matrizLineasVerticalesAnterior[int(i*(numeroLineasX+1)+j)] == 0) and
    #(matrizLineasVerticalesAnterior[int(i*(numeroLineasX+1)+j+1)] == 1)
    #<= (misVarGlobales.matrizLineasVerticales[int(i*(numeroLineasX+1)+j)] == 1))
    #
    #          and
    #
    #any((matrizLineasHorizontalesAnterior[int(i*(numeroLineasX)+j)] == 1) and
    #(matrizLineasHorizontalesAnterior[int((i+1)*(numeroLineasX)+j)] == 0) and
    #(matrizLineasVerticalesAnterior[int(i*(numeroLineasX+1)+j)] == 1) and
    #(matrizLineasVerticalesAnterior[int(i*(numeroLineasX+1)+j+1)] == 1)
    #<= (misVarGlobales.matrizLineasHorizontales[int((i+1)*(numeroLineasX)+j)] == 1))
    #
    #          and
    #
    #any((matrizLineasHorizontalesAnterior[int(i*(numeroLineasX)+j)] == 0) and
    #(matrizLineasHorizontalesAnterior[int((i+1)*(numeroLineasX)+j)] == 1) and
    #(matrizLineasVerticalesAnterior[int(i*(numeroLineasX+1)+j)] == 1) and
    #(matrizLineasVerticalesAnterior[int(i*(numeroLineasX+1)+j+1)] == 1)
    #<= (misVarGlobales.matrizLineasHorizontales[int(i*(numeroLineasX)+j)] == 1))
    # )  
    #          or
    #(
    #(  any(misVarGlobales.matrizLineasHorizontales[i] != 
    #   matrizLineasHorizontalesAnterior[i] for i in 
    #   range(len(misVarGlobales.matrizLineasHorizontales))) or 
    #   any(misVarGlobales.matrizLineasVerticales[i] != 
    #   matrizLineasVerticalesAnterior[i] for i in 
    #   range(len(misVarGlobales.matrizLineasVerticales))))
    #)
    #   and
    #((cuadradoCompleto(lineaActual, indiceEnMatriz, estaEnX) == False) 
    #    <= (misVarGlobales.juegaOponente == False))
    # misVarGlobales.puntuacionOponente == (puntuacionOponenteAnterior 
    # + sum(1 for i in 
    #  range(misVarGlobales.numeroPuntosX-1) for j in 
    #  range(misVarGlobales.numeroLineasY-1) 
    #  if misVarGlobales.cuadradoCompleto[i][j] != matrizCuadradosAnterior[i][j]))



    #Variables Globales usadas:

    # misVarGlobales.numeroJugadores : int //1 si se juega con la maquina
    #                                     //2 si se juega con otra persona
    # misVarGlobales.listaLineasX : list //guarda identificadores de lineas 
    #                                    //horizontales
    # misVarGlobales.listaLineasY : list //guarda identificadores de lineas 
    #                                    //verticales
    # misVarGlobales.matrizLineasHorizontales : array of int //identifica lineas 
    #                                                       //marcadas
    # misVarGlobales.matrizLineasVerticales : array of int //identifica lineas 
    #                                                     //marcadas
    # misVarGlobales.canvas : Canvas //plano en el que se dibujan las lineas
    # misVarGlobales.turnoActual : int //lleva el numero de turnos completados
    # misVarGlobales.juegaOponente : bool // True si le toca jugar al oponente
    # misVarGlobales.turnoActual : int //indica el numero de turnos pasados
    # misVarGlobales.numeroPuntosX : int //numero de puntos horizontales
    # misVarGlobales.numeroPuntosY : int //numero de puntos verticales

    #Variables locales usadas

    # numeroLineasX : int //numero de lineas horizontales
    # puntuacionOponenteAnterior : int //puntuacion anterior del oponente
    # matrizCuadradosAnterior : array of array of int //valor de 
    #            //misVarGlobales.matrizCuadrados antes de entrar a juegaMaquina
    # matrizLineasHorizontalesAnterior : list //guarda el valor anterior de 
    #                                  //misVarGlobales.matrizLineasHorizontales
    # matrizLineasVerticalesAnterior : list  //guarda el valor anterior de 
    #                                   //misVarGlobales.matrizLineasVerticales
    # estaEnX : bool //es True si "lineaActual" es horizontal
    # estaMarcada : bool //es True si "lineaActual" ya ha sido marcada
    # indiceEnMatriz : int //indice de "lineaActual" en la lista de
                            # identificadores correspondiente
    # lineaActual : int //identificador de la linea que juegaMaquina ha  
    #                   //seleccionado


    terminaJuego()

    if misVarGlobales.numeroJugadores == 0 :

        if misVarGlobales.juegaOponente == True :
            color = misVarGlobales.colorOponente
        elif misVarGlobales.juegaOponente == False :
            color = misVarGlobales.colorJugador


    while ((misVarGlobales.numeroJugadores == 1)<=(misVarGlobales.juegaOponente \
== True)) and (misVarGlobales.numeroJugadores != 2)\
          and (misVarGlobales.numeroJugadores != 2):

        sleep(0.5)

        #terminaJuego()

        #misVarGlobales.turnoActual += 1

        if misVarGlobales.numeroJugadores == 0 :
            if terminaJuego() == True :
                break
            

        if misVarGlobales.numeroJugadores == 1 :

            color = misVarGlobales.colorOponente
            print("Le toca a "+misVarGlobales.nombreOponente)

        noSalirDeBucle = True

        numeroLineasX = misVarGlobales.numeroPuntosX -1
        numeroLineasY = misVarGlobales.numeroPuntosY -1

        longitudLineaX = int(500/numeroLineasX)
        longitudLineaY = int(500/numeroLineasY)



        puedeBuscarAlAzar = buscaCuadradoCasiCompleto(color)

        misVarGlobales.turnoActual += 1
        terminaJuego()

        #Ahora se busca una linea al azar

        if puedeBuscarAlAzar == True :

        

            eleccionDeStr = choice(("listahorizontal", "listavertical"))
            if (eleccionDeStr == "listahorizontal") and\
               (0 in misVarGlobales.matrizLineasHorizontales) :

                
                
                eleccion = choice(range(len(misVarGlobales.matrizLineasHorizontales)))

                
                
                while(True) :
                    eleccion = choice(range(len(misVarGlobales.matrizLineasHorizontales)))
                    if misVarGlobales.matrizLineasHorizontales[eleccion] == 0 :
                        break

                estaEnX = True
                lineaActual = misVarGlobales.listaLineasX[eleccion]

                indiceEnMatriz = misVarGlobales.listaLineasX.index(lineaActual)

                misVarGlobales.matrizLineasHorizontales[eleccion] = 1
                misVarGlobales.canvas.itemconfig(misVarGlobales.listaLineasX[eleccion],\
 fill = color)
                misVarGlobales.canvas.update_idletasks()



                if cuadradoCompleto(lineaActual, indiceEnMatriz, estaEnX) == False :

                    if misVarGlobales.numeroJugadores != 0 :

                        misVarGlobales.juegaOponente = False

                    elif misVarGlobales.numeroJugadores == 0 :

                        #misVarGlobales.turnoActual += 1

                        if misVarGlobales.juegaOponente == False :

                            misVarGlobales.juegaOponente = True
                            break

                        elif misVarGlobales.juegaOponente == True :

                            misVarGlobales.juegaOponente = False
                            break
                   

                    
            elif (eleccionDeStr) == "listavertical" and\
                 (0 in misVarGlobales.matrizLineasVerticales):
                eleccion = choice(range(len(misVarGlobales.matrizLineasVerticales)))

             
            
                while(True) :
                    eleccion = choice(range(len(misVarGlobales.matrizLineasVerticales)))
                    if misVarGlobales.matrizLineasVerticales[eleccion] == 0 :
                        break

                estaEnX = False
                lineaActual = misVarGlobales.listaLineasY[eleccion]

                indiceEnMatriz = misVarGlobales.listaLineasY.index(lineaActual)
                    
                misVarGlobales.matrizLineasVerticales[eleccion] = 1
                misVarGlobales.canvas.itemconfig(misVarGlobales.listaLineasY[eleccion],\
 fill = color)
                misVarGlobales.canvas.update_idletasks()
                
                

                if cuadradoCompleto(lineaActual, indiceEnMatriz, estaEnX) == False :

                    if misVarGlobales.numeroJugadores != 0 :

                        misVarGlobales.juegaOponente = False

                    elif misVarGlobales.numeroJugadores == 0 :

                        #misVarGlobales.turnoActual += 1

                        if misVarGlobales.juegaOponente == False :

                            misVarGlobales.juegaOponente = True
                            break

                        elif misVarGlobales.juegaOponente == True :

                            misVarGlobales.juegaOponente = False
                            break

                    

            elif (eleccionDeStr == "listahorizontal") and\
               (0 not in misVarGlobales.matrizLineasHorizontales) :

                eleccion = choice(range(len(misVarGlobales.matrizLineasVerticales)))

              
            
                while(True) :
                    eleccion = choice(range(len(misVarGlobales.matrizLineasVerticales)))
                    if misVarGlobales.matrizLineasVerticales[eleccion] == 0 :
                        break

                estaEnX = False
                lineaActual = misVarGlobales.listaLineasY[eleccion]

                indiceEnMatriz = misVarGlobales.listaLineasY.index(lineaActual)
                    
                misVarGlobales.matrizLineasVerticales[eleccion] = 1
                misVarGlobales.canvas.itemconfig(misVarGlobales.listaLineasY[eleccion],\
 fill = color)
                misVarGlobales.canvas.update_idletasks()
                
                           

                if cuadradoCompleto(lineaActual, indiceEnMatriz, estaEnX) == False :

                    if misVarGlobales.numeroJugadores != 0 :

                        misVarGlobales.juegaOponente = False

                    elif misVarGlobales.numeroJugadores == 0 :

                        #misVarGlobales.turnoActual += 1

                        if misVarGlobales.juegaOponente == False :

                            misVarGlobales.juegaOponente = True
                            break

                        elif misVarGlobales.juegaOponente == True :

                            misVarGlobales.juegaOponente = False
                            break

               

            elif (eleccionDeStr) == "listavertical" and\
                 (0 not in misVarGlobales.matrizLineasVerticales):

                eleccion = choice(range(len(misVarGlobales.matrizLineasHorizontales)))

             
                
                while(True) :
                    eleccion = choice(range(len(misVarGlobales.matrizLineasHorizontales)))
                    if misVarGlobales.matrizLineasHorizontales[eleccion] == 0 :
                        break

                estaEnX = True
                lineaActual = misVarGlobales.listaLineasX[eleccion]

                indiceEnMatriz = misVarGlobales.listaLineasX.index(lineaActual)

                misVarGlobales.matrizLineasHorizontales[eleccion] = 1
                misVarGlobales.canvas.itemconfig(misVarGlobales.listaLineasX[eleccion],\
 fill = color)
                misVarGlobales.canvas.update_idletasks()



                if cuadradoCompleto(lineaActual, indiceEnMatriz, estaEnX) == False :

                    if misVarGlobales.numeroJugadores != 0 :

                        misVarGlobales.juegaOponente = False

                    elif misVarGlobales.numeroJugadores == 0 :

                        #misVarGlobales.turnoActual += 1

                        if misVarGlobales.juegaOponente == False :

                            misVarGlobales.juegaOponente = True
                            break

                        elif misVarGlobales.juegaOponente == True :

                            misVarGlobales.juegaOponente = False
                            break
  



        #misVarGlobales.turnoActual += 1
        
        terminaJuego()
        
        
        
    #if misVarGlobales.numeroJugadores != 0 :
    #   print("Le toca a "+misVarGlobales.nombreJugador)
    if misVarGlobales.numeroJugadores == 0 :

        print("Turno Actual: "+str(misVarGlobales.turnoActual))

        if misVarGlobales.juegaOponente == True :
            print("Le toca a "+misVarGlobales.nombreOponente)

        elif misVarGlobales.juegaOponente == False :
            print("Le toca a "+misVarGlobales.nombreJugador)

        
    
#############################################################################
###################### Programa Principal ###################################
#############################################################################





instrucciones()

juegoNuevoSalvado()



               

        

            

            


            

                
            

        

    

    

    
        

    

    
                
            
            
        
        
        
        

    
        

    



    

        
        

       

            

            

        
            
            
        

    


    
        



