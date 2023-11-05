# -*- coding: utf-8 -*-
"""
ALGEBRA LINEAL

Algoritmo de Factorización QR
Es una descomposision de una matriz como el producto de una matriz ortogonal
por una trangular superior.

Este algoritmo lo que hace, es que dada una matriz real cuadrada "A"
                       A=QR
Se encuentran la matriz "Q" cuyos vectores columna son los vectores Ortonormalizados 
de las columas de "A" y "R" es una matriz triangular superior.
                       R=Q'A   
    
    (nota: Q' denota la transpuesta de Q)

"""


import math
#---------------------------------------------------
# Se obtiene la norma de un vector
def norma(v):
    norm=0
    for elem in v:
        norm += elem*elem
    return math.sqrt(norm)

# Producto escalar
def prodEsc(escalar, vector):
    v=[]
    for i in range(len(vector)):
        v.append(round(vector[i]*escalar,6))
    return v

# Se obtiene el producto interno estandar (Producto punto)
def Prod_Int_Estand(v,w):
    productoPunto = 0
    for elemento in range(len(w)):
        productoPunto += v[elemento]*w[elemento]
    return productoPunto

# Es la operacion (<vn,wi>/||wi||^2)*wi
def divProdInt(v,w):
    div=Prod_Int_Estand(v, w)/math.pow(norma(w),2) #<vn,wi>/||wi||**2 = K
    vec=prodEsc(div, w) # K*{a,b,c,..}
    return  vec

# Me va a dar los vectores que se van a restar a Vi con i={2,3,4,...}
def RestaToria(v, ind, W): #ind-1
    restaToria = []
    for i in range(ind-1):
        #print(v,"lll")
        #print(divProdInt(v, W[i]))
        restaToria.append(divProdInt(v, W[i]))
    return restaToria

# hace la resta entre dos vectores
def RestV(v,Wrest):
    aux = v
    for i in range(len(Wrest)):
        for j in range(len(v)):
            aux[j] = aux[j]-Wrest[i][j]
    return aux

# Ortogonaliza un vector de vectores como una base
def Ortogonalizacion(V):
    W_Ort=[]
    W_Ort.append(V[0])
    for i in range(len(V)): # Lo hace para cada vector de V
        Rest=RestaToria(V[i], i+1, W_Ort)
        a=RestV(V[i], Rest)
        if i>0:
            W_Ort.append(a)
    return W_Ort

# Ortonormaliza 
def Ortonormalizacion(V):
    W_Ort_Norm=[]
    subVnom=[]
    for j in range(len(V)):
        #print("imprimiendo los vectores de V ",V[j])
        longitudV=norma(V[j]) 
        #print("esta es la norma", longitudV)
        if longitudV!=0:
            for i in range(len(V[0])):
                #print(f"imprimiendo los subvectores de V -->{i}__{V[j][i]} ")
                subVnom.append(round(V[j][i]/longitudV,6))
            W_Ort_Norm.append(subVnom)
            subVnom=[]
        
    return W_Ort_Norm

#---------------------------------------------------
#---------------------------------------------------
#---------------------------------------------------

def pedirMat(tam):
    A=[]
    a=0
    for i in range(tam):
        A_2=[]
        for j in range(tam):
            print(f"introdusca el valor de a{i+1}{j+1} de la matriz ")
            a=float(input(""))
            A_2.append(a)
        A.append(A_2)
    
    return A

def Mat_Transp(A, tam):
    A_trans=[]
    for i in range(tam):
        A_2=[]
        for j in range(tam):
            A_2.append(A[j][i])
        A_trans.append(A_2)
        
    return A_trans

def Def_Q(A, tam):
    Q=[]
    v_Ort=Ortogonalizacion(A)
    BON=Ortonormalizacion(v_Ort)
    for i in range(tam):
        Q.append(BON[i])
    return Q

def Multy_A_B(A, B, tam): #(Faltan ajustar errores de redondeo)
    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
    for i in range(tam):
        for j in range(tam):
            temp=0.0
            for k in range(tam):
                temp += A[i][k] * B[k][j]
            result[i][j] = round(temp,3)
    return result


def matrix_vector_multiply(matrix, vector):
    if len(matrix[0]) != len(vector):
        raise ValueError("El número de columnas en la matriz debe ser igual al número de elementos en el vector")
    
    result = [0] * len(matrix)
    
    for i in range(len(matrix)):
        for j in range(len(vector)):
            result[i] += matrix[i][j] * vector[j]
    
    return result

def Despeje_Matriz(R,Sols):
    Soluciones=[0]*len(R[0])
    #print(R[2][2],Sols[2]," Solcsss")
    Sol_tem=0
    i=len(R)-1
    #Aqui se hace el despeje de una fila 
    while i>=0:
        j=len(R[0])-1 #se inicializa en el tamaño del vector
        #print(j,i)
        while j>=i:
            Sol_tem=Sols[j]-R[i][j] # se van restando los elemetos
            
            if i==j: # se agrega la primera solucion al vector de soluciones
               #print("La divicioe  ",R[i][j])
               Soluciones[i]=(Sol_tem/R[i][j])
               
            j-=1
            
        #Aqui se van a "sustituir" las soluciones obtenidas en la matriz R
        k=i-1 #posible error
        while k>=0:
            R[k][i]=R[k][i]*Soluciones[i]
            k-=1
        
        
        i-=1
        
    return Soluciones

            
            

# PRUEBAS
"""
tam=2
A=pedirMat(tam)
print(A)
A_T=Mat_Transp(A, tam)

Q=Def_Q(A_T, tam) #Esta es Q transpuesta
print("Matriz Q ",Q)


R=Multy_A_B(Q, A, tam) #Se obtiene R
print("MAtriz R ",R)

print(Multy_A_B(Q, R, tam))"""

#+++++++++++++++++++++++++++++
#+++++++++++++++++++++++++++++
#+++++++++++++++++++++++++++++

sols=[94,398,2910]
A=[[6,12,94],[12,94,468],[949,468,3190]]

A_T=Mat_Transp(A, 3)
Q=Def_Q(A_T, 3) #Esta es Q transpuesta
R=Multy_A_B(Q, A, 3) #Se obtiene R
#print(R)



QT=Mat_Transp(Q, len(Q))#Q normal 

print("Esto es Q ",QT)

sols2=matrix_vector_multiply(Q, sols)

print(sols2, "soluciones 222")
soluciones=Despeje_Matriz(R, sols2)

print(soluciones)







