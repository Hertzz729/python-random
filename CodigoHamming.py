#+++++LIBRERIAS+++++++
from math import log
import random


mensaje = input("escribe tu mensaje:  ")
longMen = len(mensaje)*8 #longitud del mensaje 
nBitsPar= log(longMen,2)+1 #espacios para agregar de los bits de pariedad
totalEsVec = int(longMen + nBitsPar)  #espacio de arrelo

vectorBits=[]

#-----------FUNCIONES---------------------

#PASA TODO EL MENSAJE INCLUYENDO LOS BIT DE PARIDAD A UN VECTOR
def binario(mensaje):
    i=0
    vectorBinario = []
    cadena = list(mensaje)
    #selecciona la letra de la cadena y la pasa a entero
    for i in range(len(cadena)):
        valor = ord(cadena[i])
        n=7
        #convierte a binario el numero y rellena el vector
        for i in range(8):
            if valor>= 2**n:
                vectorBinario.append(1)
                valor =valor - pow(2,n)
                n-=1
             
            else:
                vectorBinario.append(0)
                n-=1     
    
    return vectorBinario

#DESCOMPOINE LAS POTENCIAS DE LA POSISCION
def descomponer(numero):
    vectorCom = []
    pot1=0
    pot2=1
    suma=0
    
    while True:
        #si el numero esta en el intervalo de 2^n<=numero<2^(n+1) se entra en el condicional, pasa al else y se le suma 1 para ambas potencias
        if numero>=pow(2,pot1) and numero<pow(2,pot2):
            
            #hasta que la suma sea igual a el numero se repetira el ciclo
            while suma!=numero:
                vectorCom.append(pot1) #agregar potencias al vector de combinaciones
                suma+=pow(2,pot1)
                
                #si la suma es mayor al numero. se resta lo ultimo que se le sumo y se quita de la lista
                if(suma>numero):
                    suma-=pow(2,pot1)
                    vectorCom.remove(pot1)
                    
                pot1-=1
                
            break
    
        else: 
            pot1+=1
            pot2+=1

    return vectorCom

#ASIGNA LOS BITS DE PARIEDAD 
def editBitsPar(vectorBinario,nBitsPar):
#-----Crea el vector de pariedad
    vectorPar = []
    n=0
    for i in range(int(nBitsPar)):
        vectorPar.append(0)

#+++++Rellena el vector de pariedad con los bits de pariedad 
    for i in range(len(vectorBinario)):
        #entraria a el bit para despues modificar el bit de pariedad 
        if pow(2,n) != i+1:
            #si el bit del SMS es 1 modifica los bits de pariedad 
            if vectorBinario[i]==1:
                vectorPot = descomponer(i+1) #descomponer el valor que ocupa en el vector el bit del SMS
               
                for potencia in vectorPot:
                    if vectorPar[potencia]==1: #el vector par es el vector de solo pariedades
                        vectorPar[potencia]=0
                    else:
                        vectorPar[potencia]=1
    return vectorPar
                       
#FUNCIÓN PARA MODIFICAR ALEATORIAMENTE UN BIT DEL MENSAJE ENVIADO
def modAleatoria(vectorBits):
    mensajeMod=copiarV(vectorBits)
    seleccion = random.randint(2,len(vectorBits)-1)
    if  mensajeMod[seleccion]==1:
        mensajeMod[seleccion]=0
    else:
        mensajeMod[seleccion]=1
    return mensajeMod
    
#COPIAR VECTOR DE BITS
def copiarV(vectorBits):
    vecMod=[]
    for i in range(len(vectorBits)):
        vecMod.append(vectorBits[i])
    return vecMod

#IDENTIFICA EL ERROR 
def comparar(vectorBits,vpariedad):
    suma=0
    for i in range(len(vectorBits)):
        if vectorBits[i]!=vpariedad[i]:
            suma+=pow(2,i)

    return suma

#RELLENA EL VECTOR CON LOS BITS DE PARIEDAD Y DEL MENSAJE, ADEMAS MODIFICA EL MENSAJE ORIGINAL
def rellenar(vectorBits,binario,totalEsVec,nBitsPar):
    n=0
    j=0
    for i in range(totalEsVec):
        if pow(2,n) != i+1: 
           vectorBits.append(binario[j])
           j+=1
        #si i+1 es igual a la potencia 2^n se agrega un bit de pariedad
        else:
            vectorBits.append("bt")
            n+=1
    #se crea el vector con las pariedades del mensaje original
    vectorPariedad=editBitsPar(vectorBits,nBitsPar)
    mensajeMod=modAleatoria(binario)
    decod=decodificar(mensajeMod)
    print("Esto diria el mensaje de no ser corregido ---> ",decod)
    
    r=0
    k=0
    for j in range(totalEsVec):
        if pow(2,k) != j+1: 
           vectorBits[j]=mensajeMod[r]
           r+=1
        else:
            vectorBits[j]=" "#str(vectorPariedad[k])
            k+=1
          
    vectorPariedadMod=editBitsPar(vectorBits,nBitsPar)
    posicion=comparar(vectorPariedad,vectorPariedadMod)
    #print(vectorBits)
    return posicion

#CORRIGE EL ERROR CON LA POSICION OBTENIDA DE LA PARIEDAD Y OBTIENE LOS BITS DEL MENSAJE
def corregir(vectorBits,posicion):
    
    n=0
    if vectorBits[posicion-1]==1:
        vectorBits[posicion-1]=0
    else:
        vectorBits[posicion-1]=1
    
    t=len(vectorBits)
    for i in range(t):
        if pow(2,n) == i+1:
            vectorBits.remove(" ")
            n+=1
    
#PASA DE BINARIO A CODIGO ACII
def decodificar(vectorBits):
    vecTexto=[]
    k=0
    #PASAR EL VECTOR DE BITS A TEXTO AGREGANDO "," CADA 8 ESPACIOS
    for i in range(len(vectorBits)):
        if k%8==0 and k!=0:
            vecTexto.append(",")
            
        vecTexto.append(vectorBits[i])
        k+=1
        
    textoBits="".join([str(_) for _ in vecTexto])
    
    #PASAR A TEXTO LEGIBLE LOS BITS
    numeros = textoBits.split(",")
    decodificado = ""
    for numero_binario in numeros:
        numero_decimal = int(numero_binario, 2)
        letra = chr(numero_decimal)
        decodificado += letra
    return decodificado   
 

#+++++++++++++PRUEBAS+++++++++++++++++

sms=binario(mensaje)#mensaje originarl binario
#se obtiene la posicion donde se provoco el error 
posicion=rellenar(vectorBits,sms,totalEsVec,nBitsPar)
print("la modificacion se hizo en la posicion ---> ", posicion)
#corregimos el error
corregir(vectorBits,posicion)
#decodificamos el mensaje ya corregido
print("El texto mensaje corregio es el siguiente ---> ",decodificar(vectorBits))





    
