 
def mixedMethod(x, a, b, mod):
 
    periodo = 0
    bandera = 0
 
    while(bandera != x):
        if (periodo == 0):
            bandera = x
        x = (a * x + b) % mod
        print(x),
        periodo = periodo + 1
 
    if(periodo == mod):
        print("periodo completo: ", periodo)
    else:
        print("periodo incompleto:", periodo)
 
def main():
    x = int(raw_input("Introduce la semilla: "))
    a = 5 #int(raw_input("Introduce el valor del multiplicador: "))
    b = 1 #int(raw_input("Introduce el valor de la constante aditiva: "))
    mod = 9 #int(raw_input("Introduce el valor del modulo: "))
    mixedMethod(x,a,b,mod)
 
if __name__ == "__main__":
    main()