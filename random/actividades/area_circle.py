import matplotlib.pyplot as plt
import numpy as np


    ##generador de numeros aleatorios
    #x=np.random.uniform(0,1,N)

    ###line graph
    #plt.plot(x,y,label='linea 1',color='r')
    #plt.plot(x,y2,label='linea 2',color='c')

    ###bars graph
    #plt.bar(x,y,label='Barras 1', color='r')
    #plt.bar(x,y2,label='Barras 2',color='c')

    ###Histogram
    #bins=range(0,110,10)
    #plt.hist(x,bins,histtype='bar',rwidth=0.8)

    ###scatter
    #plt.scatter(x,x2,label='puntitos azules', color='b', marker='*', s=10)
    #plt.scatter(x,y,label='puntitos rojos', color='r', marker='o', s=10)


    ###texto sobre la grafica
    #plt.text(4,4,'text')
    #plt.annotate('anotacion',(0,0), 
                #  xytext=(0.9,0.9),textcoords='axes fraction',
                #  arrowprops = dict(facecolor='black', color='black')
                # )

    ###mostrar circulo
    # def xy(r,phi):
    #     return r*np.cos(phi), r*np.sin(phi)
    
    # fig = plt.figure()
    # ax = fig.add_subplot(112,aspect='equal')

    # phis=np.arange(0,6.28,0.01)
    # r =1000.
    # ax.plot( *xy(r,phis), c='r',ls='-' )
    # plt.show()




def random(x1,x2,x3,escala,cantidad):
    a1 = 171.0
    b1 = 5.0
    a2 = 172.0
    b2 = 5.0
    a3 = 170.0
    b3 = 5.0
    mod1=30269.0
    mod2=30307.0
    mod3=30323.0

    x=[]

    for n in range(0,cantidad):
        x1 = (a1 * x1 + b1) % mod1
        x2 = (a2 * x2 + b2) % mod2
        x3 = (a3 * x3 + b3) % mod3
        v = ((x1/mod1) + (x2/mod2) + (x3/mod3)) %1
        
        #escalando al ancho del circulo
        v=(2*escala*v)-escala
        
        x.append(v)
    

    return x

    
def circulo(r,phi):
    return r*np.cos(phi), r*np.sin(phi)




def main():
    radio=5.0#float(input('radio del circulo: '))
    puntos=10000#float(input('cantidad de puntos aleatorios: '))
    semilla1=26
    semilla2=62
    semilla3=98

    x=random(semilla1,semilla2,semilla3,radio,puntos) # 3 semillas y cantidad de datos
    y=random(semilla3,semilla1,semilla2,radio,puntos)

    dx=[]
    dy=[]

    fx=[]
    fy=[]

    i=0
    for point in x:
        isin= (x[i]**2) + (y[i]**2)
        if( (isin) <= (radio**2) ):
            dx.append(x[i])
            dy.append(y[i])
        else:
            fx.append(x[i])
            fy.append(y[i])

        i=i+1

    print len(dx)
    print len(fx)


    area=(radio**2)*np.pi
    estimada=((2*radio)**2)*(float(len(dx))/float(puntos))
    error=area-estimada


    
    fig = plt.figure()
    ax = fig.add_subplot(111,aspect='equal')

    phis=np.arange(0,6.28,0.01)
    ax.plot( *circulo(radio,phis), c='k',ls='-' )
    ax.scatter(dx,dy,label='adentro', color='b', marker='o', s=2)
    ax.scatter(fx,fy,label='afuera', color='r', marker='o', s=2)
    

    ###mostraar la grafica con sus labels
    # plt.xlabel('Numeros X')
    # plt.ylabel('Numeros Y')
    plt.title('Area de un circulo\n Area real:'+str(area)+' Area estimada: '+str(estimada)+' Error: '+str(error))
    # #plt.legend() #no se usa con histogram

    plt.show()


    try:
        input('press something to finish')
    except:
        print 'finished program'


if __name__ == "__main__":
    main()