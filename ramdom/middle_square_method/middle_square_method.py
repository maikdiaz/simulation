n=1
while len(str(n))<4:
    n = int(input("ingrese un numero de cuatro digitos: "))

listado = list()
while n not in listado:
    listado.append(n)
    n1 =str(n * n).zfill(8)[2:6]
    result="0."+n1
    n=int(n1)
    print(result)
print('periodicity = ', len(listado) - listado.index(n))