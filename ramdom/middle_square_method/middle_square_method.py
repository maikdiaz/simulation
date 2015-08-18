n = int(input("ingrese un numero de cuatro digitos: "))
cant=int(input("ingrese la cantidad de numeros aleatorios: "))

#listado = list()
while cant>0:
    n1 =str(n * n).zfill(8)[2:6]
    result="0."+n1
    n=int(n1)
    print(result)
    cant=cant-1