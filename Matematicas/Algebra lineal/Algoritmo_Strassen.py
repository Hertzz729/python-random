import math

#---------------FUNCION PARA PEDIR MATRICES------------------------
def Pedir_Mat():
    fila=int(input("Digite el tamaño de la matriz "))
    columna=fila
    matrizF=[]
    
    for i in range(fila):
        matrizC=[]
        for j in range(columna):
            print("a",i,j)
            matrizC.append(float(input("Digite el elelmeto " )))
        matrizF.append(matrizC)
        print(matrizF)
        
    return matrizF



#----------------FUNCION PARA ENCONTRAL LA PONTENCIA DE 2^N------------------
def Find_2n(matriz):
    tam=len(matriz)
    pot_2n = math.log(tam, 2)
    if pot_2n!=1:
        pot_2n = int(pot_2n)+1
    return pot_2n

#----------------FUNCION RELLENAR CON CEROS-------------------------
def FullCeros(matriz, tam_2n):#rellenara con ceros si el tamaño de la matriz != 2^n
    tam = len(matriz)
    p = int(pow(2, tam_2n))
    
    # Añade filas de ceros si el tamaño de la matriz no es 2^n
    while len(matriz) < p:
        matriz.append([0] * tam)
    
    # Añade ceros a las filas existentes si es necesario
    for i in range(len(matriz)):
        while len(matriz[i]) < p:
            matriz[i].append(0)


    
#---------------FUNCION RECURSIVA DIVIDE Y VENCERAS MATRICES--------------
def Divid_Mat(matriz, tamM):
    
    if tamM==2:
        return 
    
#---------------ALGORITMO STRASSEN--------------
def Strassen(mat1,mat2): # esta mal
    p1 = mat1[0][0]*(mat2[0][1] - mat2[1][1])
    p2 = (mat1[0][0] + mat1[0][1]) * mat2[1][1]
    p3 = (mat1[1][0] + mat1[1][1]) * mat2[0][0]
    p4 = mat1[1][1] * (mat2[1][0] - mat2[0][0])
    p5 = (mat1[0][0] + mat1[1][1]) * (mat2[0][0] + mat2[1][1])
    p6 = (mat1[0][1] - mat1[1][1]) * (mat2[1][0] + mat2[1][1])
    p7 = (mat1[0][0] - mat1[1][0]) * (mat2[0][0] + mat2[0][1])
    
    
    




#==================PRUEBAS Y MAIN======================================

mat=Pedir_Mat()
p=Find_2n(mat)
FullCeros(mat, p)
print(mat)



