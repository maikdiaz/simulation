import numpy as np
import matplotlib.pyplot as plt
import time
 
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

def random_list(cantidad):
    mod1=30269.0
    mod2=30307.0
    mod3=30323.0

    x1 = current_milli_time()
    x2 = current_milli_time()+123456 #float(raw_input("Introduce la semilla 2: "))
    x3 = current_milli_time()+987654 #float(raw_input("Introduce la semilla 3: "))
    l=[]
    while cantidad>0:
        x1=mixedMethod1(x1,mod1)
        x2=mixedMethod2(x2,mod2)
        x3=mixedMethod3(x3,mod3)
        v=valorU(x1,x2,x3,mod1,mod2,mod3)
        #print 'x',cant,': ',u
        l.append(v)
        cantidad = cantidad-1

    return l

#hallar la funcion de distribucion de probabilidad
def cdfp(landa,cantidad):

    p=[]
    for x in range(cantidad):
        p.append((np.exp(-landa)*(landa**x))/(np.math.factorial(x)))
    #print 'probabilidades: ',p

    cdf=[]
    acumulado=0.0
    for valor in p:
        acumulado=valor+acumulado
        cdf.append(acumulado)

    #print 'acumuladas',cdf
    return cdf

def metodo_inversion(cantidad, acumulada):

    aleatorios=random_list(cantidad)
    resultados=[]

    for aleatorio in aleatorios:
        i=0
        for elemento in acumulada:
            if aleatorio <= elemento:
                resultados.append(i)
                break
            i=i+1

    return resultados

def main():
    cantidad=50 #float(input('cantidad aleatorios: '))
    landa=4.0 #float(input('valor de landa: '))
    cdf=[]
    cdf=cdfp(landa,cantidad)
    valeatoria=metodo_inversion(cantidad,cdf)
    print 'Variables aleatorias con distribucion poisson: \n',valeatoria

    


    try:
        input('\n\npush enter to finish')
    except:
        print 'finished program'
 
if __name__ == "__main__":
    current_milli_time = lambda: int(round(time.time() * 1000))
    main()






# def poisson(x,landa):
#     n=0
#     y=1.0
#     v=np.exp(-landa/x)
#     l=random_list(1000)

#     while (y>=v) :
#         y = y*l[n]
#         n = n+1

#     return n