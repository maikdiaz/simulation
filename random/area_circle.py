import numpy as np
import matplotlib.pyplot as plt

def random(x1,x2,x3,cant):
    a1 = 171
    b1 = 5
    a2 = 172
    b2 = 5
    a3 = 170
    b3 = 5
    mod1=30269.0
    mod2=30307.0
    mod3=30323.0

    x=[]

    for n in range(0,cant):
        x1 = (a1 * x1 + b1) % mod1
        x2 = (a2 * x2 + b2) % mod2
        x3 = (a3 * x3 + b3) % mod3
        u = ((x1/mod1) + (x2/mod2) + (x3/mod3)) % 1
        x.append(int(u*100))
    
    return x


def main():
    x=[]
    x=random(23,24,25,100)
    #print x

    x2=random(3,4,1,100)
    y=[i*2 for i in x] 
    y2=[i*3 for i in x]

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
    plt.scatter(x,x2,label='puntitos azules', color='b', marker='*', s=10)
    plt.scatter(x,y,label='puntitos rojos', color='r', marker='o', s=10)


    ###texto sobre la grafica
    plt.text(4,4,'text')
    plt.annotate('anotacion',(0,0), 
                 xytext=(0.9,0.9),textcoords='axes fraction',
                 arrowprops = dict(facecolor='black', color='black')
                )


    plt.xlabel('Numeros X')
    plt.ylabel('Numeros Y')
    plt.title('La grafica\n matematica')
    #plt.legend() #no se usa con histogram
    plt.show

    try:
        input('press something to finish')
    except:
        print 'finished program'


if __name__ == "__main__":
    main()