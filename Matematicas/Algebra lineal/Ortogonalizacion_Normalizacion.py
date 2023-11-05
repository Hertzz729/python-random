"""
ALGEBRA LINEAL

 Dado un conjunto de vectores en R^n los ortogonaliza y normaliza
 con el metodo de Gram-Schmidt
 
 Nota 1: Se usa el producto interno usual.
 Nota 2: El programa no verifica que el vector introducido por el 
         usuario sea linealmente independiente o una base, por lo 
         que el usuario mismo debe estar seguro que si lo sea. 
     
"""
import math

#==============================FUNCIONES===============================

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
    
    print("esto es doble w ",w)
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

def PedirBase():
    Base=[]
    vecAux=[]
    cVec=int(input("Cual es la cantidad de vectores de la base? "))
    cSubVec=int(input("En que R^n esta su espacio vectorial? "))
    for i in range(cVec):
        print(f"introdusca el vector {i+1} de su Base ")
        for j in range(cSubVec):
            elem=float(input(f"introdusca el elemento {j+1} de su Vector {i+1} -> "))
            vecAux.append(elem)
        Base.append(vecAux)
        vecAux=[]
    return Base


#==============PRUEBAS NUEVO=======================
#     Vector de prueba. Que se puede sustituir el "base"3
#q=[[1,0,0],[1,1,0],[0,2,-3]]


base=PedirBase()
print("Esta es la base Ortogonal ",Ortogonalizacion(base))
r=Ortogonalizacion(base)
print("\n Esta es la base Ortonormal",Ortonormalizacion(r))
