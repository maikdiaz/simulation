import numpy as np
import matplotlib.pyplot as plt
 
def mixedMethod1(x1,mod1):
    a1 = 171 #int(raw_input("Introduce el valor del multiplicador: "))
    b1 = 0 #int(raw_input("Introduce el valor de la constante aditiva: "))

    x1 = (a1 * x1 + b1) % mod1
    return x1

def mixedMethod2(x2,mod2):
    a2 = 172 #int(raw_input("Introduce el valor del multiplicador: "))
    b2 = 0 #int(raw_input("Introduce el valor de la constante aditiva: "))

    x2 = (a2 * x2 + b2) % mod2
    return x2

def mixedMethod3(x3,mod3):
    a3 = 170 #int(raw_input("Introduce el valor del multiplicador: "))
    b3 = 0 #int(raw_input("Introduce el valor de la constante aditiva: "))

    x3 = (a3 * x3 + b3) % mod3
    return x3

def valorU(x1,y1,z1,mod1,mod2,mod3):

    u=((x1/mod1) + (y1/mod2) + (z1/mod3)) % 1
    return u
 
def main():
    mod1=30269.0
    mod2=30307.0
    mod3=30323.0

    cant=1000 #float(raw_input("introduce la cantidad de aleatorios: "))
    x1 = 14.0 #float(raw_input("Introduce la semilla 1: "))
    x2 = 34.0 #float(raw_input("Introduce la semilla 2: "))
    x3 = 23.0 #float(raw_input("Introduce la semilla 3: "))
    lista=[]
    while cant>0:
        x1=mixedMethod1(x1,mod1)
        x2=mixedMethod2(x2,mod2)
        x3=mixedMethod3(x3,mod3)
        u=valorU(x1,x2,x3,mod1,mod2,mod3)
        print 'x',cant,': ',u
        lista.append(u)
        cant=cant-1

    x1 = 56.0 #float(raw_input("Introduce la semilla 1: "))
    x2 = 23.0 #float(raw_input("Introduce la semilla 2: "))
    x3 = 76.0 #float(raw_input("Introduce la semilla 3: "))
    lista2=[]
    cant=1000
    while cant>0:
        x1=mixedMethod3(x1,mod1)
        x2=mixedMethod1(x2,mod2)
        x3=mixedMethod2(x3,mod3)
        u=valorU(x1,x2,x3,mod1,mod2,mod3)
        print 'y',cant,': ',u
        
        lista2.append(u)
        cant=cant-1

    plt.scatter(lista,lista2,label='puntitos', color='k', marker='o', s=3)
    plt.show()
    
    input('push enter to finish')
 
if __name__ == "__main__":
    main()