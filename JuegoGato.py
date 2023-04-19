"""
JUEGO DE GATO
"""
from itertools import combinations

matrizG = [["0","0","0"],["0","0","0"],["0","0","0"]]
matrizV=[[1.1,1.2,1.4], [1.03,1.09,1.07], [1.006,1.005,1.008]]


def AsignarChar(jugador):
    if jugador==1:
        print("Jugador 1 ")
    else:
        print("Jugador 2 ")
    caracter = input("elija un caracter que con el que jugar: ")
    return caracter

def PedirCoord():
    n = int(input("Digite la coordenada n: "))
    m = int(input("Digite la coordenada m: "))
    return n,m

def ValidarMov(matrizG,n, m):
    if matrizG[n][m]=='0':
        return True
    else:
        return False
    
def ColocarChar(matrizG, matrizV, caracter, Vpx):
    while True:
        n,m = PedirCoord()

        if ValidarMov(matrizG, n, m)==True:
            break
        else:
            print("La posicion elegida ya esta ocupada")
            
    matrizG[n][m]=caracter
    Vpx.append(matrizV[n][m])
    print(Vpx)



def ValidWin(arr):
    total = 0
    for comb in combinations(arr, 3):
        total += sum(comb)
    if total in [3.7, 3.19, 3.019, 3.295, 3.478, 3.496, 3.136, 3.198]:
        return True
    else:
        return False

def ImpirmirMat(matriz):

    for fila in matriz:
        for elemento in fila:
            print(elemento, end=" ")
        print()

    
def JUEGO(matrizG, matrizV):
    Vp1=[]
    Vp2=[]
    
    j1C=AsignarChar(1)
    j2C=AsignarChar(2)
    
    t1=0
    t2=1
    
    
    while True:
         
            
        print("Turno Jugador1 ")
        ColocarChar(matrizG, matrizV, j1C, Vp1)
        print(t1)
        t1+=1
        ImpirmirMat(matrizG)
        
        if ValidWin(Vp1)==True:
            print("El jugador 1 ha ganado ")
            break
            
        
        print("Turno Jugador2 ")
        ColocarChar(matrizG, matrizV, j2C, Vp2)
        t2+=1
        ImpirmirMat(matrizG)
        
        if ValidWin(Vp2)==True:
            print("El jugador 2 ha ganado ")
            break





    
#+++++++++++++++++++++++
# PROGRAMA PRINCIPAL
#+++++++++++++++++++++++

JUEGO(matrizG, matrizV)
