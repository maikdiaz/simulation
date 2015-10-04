__author__ = 'maick'
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
style.use("ggplot")



##########################################
def random(escala, cantidad, semilla):

    a1 = 171.0
    b1 = 5.0
    a2 = 172.0
    b2 = 5.0
    a3 = 170.0
    b3 = 5.0
    mod1 = 30269.0
    mod2 = 30307.0
    mod3 = 30323.0

    x1 = semilla
    x2 = semilla**2
    x3 = semilla**3


    x = []

    for n in range(0, cantidad):
        x1 = (a1 * x1 + b1) % mod1
        x2 = (a2 * x2 + b2) % mod2
        x3 = (a3 * x3 + b3) % mod3
        v = ((x1/mod1) + (x2/mod2) + (x3/mod3)) % 1

        #escalando al ancho del circulo
        v=(escala*v)

        x.append(v)

    return x



def main():

    escala=5 #int(input('rango de aleatorios 0 a x: '))

    puntos=[]
    x = random(escala, 100, 4568)
    y = random(escala, 100, 6543)

    for i in range(len(x)):
        puntos.append( [ x[i], y[i] ] )

    #print puntos
    ###########################################

    k= 3 #int(input('numero de centroides: '))
    centros = []
    x = random(escala, k, 4568+k+escala)
    y = random(escala, k, 6543+k+escala)

    for i in range(len(x)):
        centros.append( [ x[i], y[i] ] )

    #print centros
    ###########################################
    colors = "bgrcmykw"
    cn= 0

    for i in range(len(centros)):
        plt.scatter(centros[i][0],centros[i][1], color=colors[cn], marker='x', s=150)
        centros[i].append(colors[cn])
        cn+=1

    for i in range(len(puntos)):
        plt.scatter(puntos[i][0],puntos[i][1], marker='*', s=100)
        cn+=1

    plt.show()
    

    for i in range(len(puntos)):
        distancia=[]
        for j in range(len(centros)):
            distancia.append( np.sqrt( (puntos[i][0]-centros[j][0])**2) +((puntos[i][1]-centros[j][1])**2))

        cercano=100000000000000000000000000000000000
        index=0
        for k in distancia:
            if cercano > k :
                cercano = k
                index +=1
        print index
        puntos[i].append(centros[index][2])

    for i in range(len(puntos)):
        plt.scatter(puntos[i][0],puntos[i][1], color=puntos[i][2], marker='o', s=100)

    plt.show()


        



    try:
        input('\n\npush enter to finish')
    except:
        print 'finished program'

if __name__ == "__main__":
    main()