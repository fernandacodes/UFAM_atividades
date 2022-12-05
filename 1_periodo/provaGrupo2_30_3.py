Python 3.10.2 (v3.10.2:a58ebcc701, Jan 13 2022, 14:50:16) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
#prova 30/03 grupo 2 - Fernanda de Melo#questão 1


def eventos(ag,d) :return [e for(e,i,f) in ag if f>=d and i<=d]

#testeeventos([(879,56,72),(910,65,75),(1010,50,100)],75) [910, 1010]


#questão 2

def imPA(a,b,c,d,e,f) :return (a-b==b-c==c-d==d-e==e-f) and (a%2!=0 and b%2!=0 and c%2!=0 and d%2!=0 and e%2!=0 and f%2!=0)

#teste#imPA(3,19,5,7,9,11)#False

#questão 3


def rep(xs) : return [x for x in xs if len([n for n in xs if n==x])>1] !=[]

#teste#xs=[1,1,1,3,4]#rep(xs)#True


#questão 4

def pontos(p1,p2):
    (a,b) = p1
    (c,d) = p2
    if (a+c)%5==0 :return a+c
    elif (a+d)%5==0 :return a+d
    elif (b+c)%5==0 :return b+c
    elif (a+b)%5==0 :return b+c
    else: return 0

    
#teste#pontos((10,5),(5,25))#15