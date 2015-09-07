
def main():
    seed=1
    while not (len(str(seed))%2==0):
        seed = int(input('enter a seed number of 2n digits: '))
    n=int(input('enter how many random numbers you want: '))
    
    list=[]

    x=0
    while x < n:
        #elevando al cuadrado
        square=seed*seed
        strsquare=str(square)
        #agregando cero a la izq en aso de necesitarlo
        if(len(strsquare)%2!=0):
            strsquare='0'+strsquare
        #obteniendo numero intermedio
        lsquare=len(strsquare)
        lseed=len(str(seed))
        seed=int(strsquare[(lsquare/2)-(lseed/2):(lsquare/2)+(lseed/2)])
        list.append(seed)
        x=x+1

    print list

if __name__ == '__main__':
    main()
