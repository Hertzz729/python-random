"""
JUEGO DE GATO
"""
import decimal

matrizG = [["0","0","0"],["0","0","0"],["0","0","0"]] #Matriz de Simbolos
matrizV=[[1.1,1.2,1.4], [1.03,1.09,1.07], [1.006,1.005,1.008]] #Matriz de Valores

#/+/+/+/+/+/+/+/+/+/
#     FUNCIONES 
#/+/+/+/+/+/+/+/+/+/

# El jugador escoje su caracter
def AsignarChar(jugador):
    if jugador==1:
        print("Jugador 1 ")
    else:
        print("Jugador 2 ")
    caracter = input("elija un caracter que con el que jugar: ")
    return caracter

# Pide las cooredenadas del movimiento al jugador respecto a la matriz 3x3
def PedirCoord():
    n = int(input("Digite la coordenada n: "))
    m = int(input("Digite la coordenada m: "))
    return n,m

# Hace la validacion del movimiento
def ValidarMov(matrizG,n, m):
    if matrizG[n][m]=='0':
        return True
    else:
        return False

# Coloca el caracter del jugador en la casilla seleccionada
def ColocarChar(matrizG, matrizV, caracter, Vpx):
    while True:
        n,m = PedirCoord()

        if ValidarMov(matrizG, n, m)==True:
            break
        else:
            print("La posicion elegida ya esta ocupada")
            
    matrizG[n][m]=caracter # Se asigna el caracter del jugador en curso a la matrizG
    Vpx.append(matrizV[n][m]) # Se asigna el valor de la posicion de la matrizV a un arreglo del jugador
    print(Vpx)


# Valida al ganador
def ValidWin(arr, turno):
    suma=0
    # NOTA: se utilizo decimal.getcontex para que python no redondeara las suma de decimales
    decimal.getcontext().prec = 4
    v=False
    # Con tres ciclos anidados se hacen las combinaciones de 3 numeros que pertenecen al  
    # arreglo del jugador si alguna de las combinaciones da un valor esperado regresa un True 
    for i in range(0,turno-2):
        for j in range(1,turno-1):
            for k in range(2,turno):
                suma=float(decimal.Decimal((arr[i])) + decimal.Decimal((arr[j])) + decimal.Decimal((arr[k])))
                #print(suma)
                if suma in [3.7, 3.19, 3.019, 3.295, 3.478, 3.496, 3.136, 3.198]:
                    v = True
                    break
    return v

# Imprime la matriz de caracteres
def ImpirmirMat(matriz):
    for fila in matriz:
        for elemento in fila:
            print(elemento, end=" ")
        print()

# Implementa todas las funciones anteriores para el juego  
def JUEGO(matrizG, matrizV):
    # Arreglos de valores de cada jugador
    Vp1=[]
    Vp2=[]
    
    #Caracteres de cada jugador
    j1C=AsignarChar(1)
    j2C=AsignarChar(2)
    
    #Turnos de cada jugador
    t1=0
    t2=0
    
    while True:
                
        print("Turno Jugador1 ")
        ColocarChar(matrizG, matrizV, j1C, Vp1)
        print(t1)
        t1+=1
        ImpirmirMat(matrizG)
        if t1>=3:
            if ValidWin(Vp1,t1)==True:
                print("El jugador 1 ha ganado ")
                break
            
        print("Turno Jugador2 ")
        ColocarChar(matrizG, matrizV, j2C, Vp2)
        t2+=1
        ImpirmirMat(matrizG)
        if t2>=3:
           if ValidWin(Vp2,t2)==True:
               print("El jugador 2 ha ganado ")
               break
    
#/+/+/+/+/+/+/+/+/+/+/+/+/+/
# PROGRAMA PRINCIPAL
#/+/+/+/+/+/+/+/+/+/+/+/+/+/
while(1):
    print("BIENVENIDO AL JUEGO DEL GATO \nmade by Jerson Ismael Gallardo Hurtado \n ")
    JUEGO(matrizG, matrizV)
    print("FIN DEL JUEGO...")
    opcion=int(input("Opciones:\n1.- Volver a Jugar \n2.- Salir\n"))
    
    if opcion!=1:
        break
    
#PROBAR EL CASO [1.1, 1.4, 1.09, 1.005, 1.008]
