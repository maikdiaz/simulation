import time

def random(escala, cantidad):

    a1 = 171.0
    b1 = 5.0
    a2 = 172.0
    b2 = 5.0
    a3 = 170.0
    b3 = 5.0
    mod1 = 30269.0
    mod2 = 30307.0
    mod3 = 30323.0

    x1 = current_milli_time()
    x2 = current_milli_time()*2
    x3 = current_milli_time()*3


    x = []

    for n in range(0, cantidad):
        x1 = (a1 * x1 + b1) % mod1
        x2 = (a2 * x2 + b2) % mod2
        x3 = (a3 * x3 + b3) % mod3
        v = ((x1/mod1) + (x2/mod2) + (x3/mod3)) % 1

        #escalando al ancho del circulo
        v=(2*escala*v)-escala

        x.append(v)


    return x


def main():

    aleatorios = random(100, 100)

    print(aleatorios)

    try:
        input('\n\npush enter to finish')
    except:
        print 'finished program'

if __name__ == "__main__":
    current_milli_time = lambda: int(round(time.time() * 1000))
    main()