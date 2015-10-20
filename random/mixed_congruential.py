import numpy as np


def mixedMethod(x, a, b, mod):
 
    periodo = 0
    bandera = 0

    v=[]
    k=0
    while k<20:#(bandera != x):
        if (periodo == 0):
            bandera = x
        x = (a * x + b) % mod
        u = (x/mod) % 1
        v.append(u)

        print('valorx ',x,' valoru: ',u)
        periodo = periodo + 1
        k+=1
        
 
    if(periodo == mod):
        print("periodo completo: ", periodo)
    else:
        print("periodo incompleto:", periodo)

    promedio=0
    suma=0
    for i in v:
        suma+=i
    promedio=suma/len(v)
    print 'promedio: ',promedio


    xmedia=promedio
    sumatoria=0.0
    for xi in v:
        sumatoria=sumatoria+(xi-promedio)**2

    print 'sumatoria',sumatoria
    print 'numeros x',len(v)
    desviacion=np.sqrt((1.0/(len(v)-1.0))*(sumatoria))
    print 'desviacion',desviacion
 
def main():
    x = 3.0 #int(raw_input("Introduce la semilla: "))
    a = 3.0 #int(raw_input("Introduce el valor del multiplicador: "))
    b = 7.0 #int(raw_input("Introduce el valor de la constante aditiva: "))
    mod = 29.0 #int(raw_input("Introduce el valor del modulo: "))
    mixedMethod(x,a,b,mod)
 
if __name__ == "__main__":
    main()