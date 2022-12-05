#funções auxiliares
def presente(verbo):
    palavra = verbo[:-2]
    eu = ['eu '+palavra+'o']
    tu = ['tu '+palavra+'as']
    ele = ['ele '+palavra+'a']
    nos = ['nós '+palavra +'amos']
    vos = ['vos '+palavra  + 'ais']
    eles = ['eles '+palavra+'am']
    return  eu,tu,ele,nos,eles
    
def passado(verbo):
    palavra = verbo[:-2]
    eu = ['eu '+palavra+'ava']
    tu = ['tu '+palavra+'avas']
    ele = ['ele '+palavra+'ava']
    nos = ['nós '+palavra +'ávamos']
    vos = ['vos '+palavra  + 'áveis']
    eles = ['eles '+palavra+'avam']
    return  eu,tu,ele,nos,eles
def futuro(verbo):
    palavra = verbo[:-2]
    eu = ['eu '+palavra+'arei']
    tu = ['tu '+palavra+'arás']
    ele = ['ele '+palavra+'ará']
    nos = ['nós '+palavra +'aremos']
    vos = ['vos '+palavra  + 'areis']
    eles = ['eles '+palavra+'arão']
    return  eu,tu,ele,nos,eles
def numeros_de_0_a_9(numero):
    numeros_0_a_9 = [
        'zero',
        'um',
        'dois',
        'tres',
        'quatro',
        'cinco',
        'seis',
        'sete',
        'oito',
        'nove',
    ]
    return numeros_0_a_9[numero]
def numero_de_10_19(numero):
    aux = numero - 10
    numeros_10_a_19 = [
        'dez',
        'onze',
        'doze',
        'treze',
        'quatorze ou catorze',
        'quinze',
        'dezesseis',
        'dezessete',
        'dezoito',
        'dezenove',
    ]

    return numeros_10_a_19[aux]


def numeros_20_a_90(numero):

    aux = int((numero - 20) / 10)

    numeros = [
        'vinte',
        'trinta',
        'quarenta',
        'cinquenta',
        'sessenta',
        'setenta',
        'oitenta',
        'noventa',
    ]
    return numeros[aux]






"""
PARTE II – Tuplas e Listas em Gera


P35: Defina a função somavet que determine a soma de dois vetores x e y, 
de origem no ponto (0,0) e situados no primeiro quadrante do plano cartesiano.
"""

def somavet(x,y):
	(x1,x2) = x
	(y1,y2) = y
	return [x1+x2]+[y1+y2]

#teste: somavet((2,3),(3,4))
#[5, 7]

"""
P36: Defina a função sumdo que dado um número inteiro positivo n, 
construa uma lista com todos os pares cuja soma de elementos é igual a n.
"""
def sumdo(n):
	return list(range(0,n,2))

#sumdo(8)
#[0, 2, 4, 6]

"""
P37: Dada uma lista L, contendo um número igual de números inteiros pares e 
ímpares (em qualquer ordem), defina a função alterna que, quando avaliada, 
produz uma lista na qual esses números pares e ímpares encontram-se alternados.

"""
def alterna(xs):
    def par(xs): 
    	return [y for y in xs if y%2==0] 
    def impa(xs): 
    	return [ y for y in xs if y%2!=0]
    def al(x,y):
    	if x == [] and y ==[] : return []
    	else: return [x[0]] + [y[0]] + al(x[1:],y[1:])
    return al(par(xs),impa(xs))

#alterna([5,7,9,2,6,8])
#[2, 5, 6, 7, 8, 9]

"""
P38: Defina a função intersec que a partir de 
duas listas de elementos distintos, determina a interseção entre elas.
"""
def intersec(l1,l2):
    if l2 == []: return l2
    elif l2[0] in l1: return [l2[0]] + intersec(l1,l2[1:])
    else: return [] + intersec(l1,l2[1:])

    
#intersec([2, 5, 6, 7, 8, 9],[5,7,9,2,6,8])
#[5, 7, 9, 2, 6, 8]
#intersec([2,9],[5,7,9,6,8])
#[9


"""
P39: Defina a função uni que dadas duas listas de 
elementos distintos, determina a união entre elas.

"""


def uni(l1,l2):
    m = l1+l2
    n = []
    for i in m:
        if i not in n:
            n = n + [i]
    return n
#uni([1,2,1,4,6,8,5],[2,3,7,4,1])


"""
PARTE III – Processamento de Cadeia de Caracteres

P40: Verificar se uma cadeia é uma palavra (apenas letras). e_palav(cadeia)


"""
#40
def number():
    l = []
    for i in range(46,58):
        l = l + [chr(i)]
    return l
number()
def letras():
    letras = []
    for i in range(65,91):
        letras = letras + [chr(i)]
    return letras
def mai():
    letras = []
    for i in range(97,123):
        letras = letras + [chr(i)]
    return letras
def head(li):
    return li[0]
def tail(li):
    return li[1:]
def e_palav(palavra):
    cont = 0
    contF = 0
    numero = number()
    for i in range(len(palavra)):
        for j in range(65,91):
            for c in range(97,123):
                for k in range(len(numero)):
                    if(palavra[i]==chr(j) or palavra[i]==chr(c)):
                        cont +=1
                    elif(palavra[i]==numero[k]):
                        contF +=1
    if(contF==0):
        return True
    else:
        return False
e_palav('JOSE')
#41
def e_int(numero):
    cont = 0
    nova_cadeia = [i for i in numero]
    n = number()
    for i in range(len(n)):
        for k in range(len(nova_cadeia)):
            if(n[i]==nova_cadeia[k]):
                cont = cont+1
    if(cont == len(nova_cadeia)):return True
    else:return False
e_int('1234')
#42
##P42: Dado um verbo regular e um tempo do modo indicativo, produzir as conjugações. conjuga(verbo,tempo)
##conjuga("jogar","presente") ==> [ "eu jogo", "tu jogas", "ele joga", "nos jogamos", "vos jogais", "eles jogam"]
def conjuga(verbo,tempo):
    if(tempo == 'presente'):
        return presente(verbo)
    elif(tempo == 'passado'):
        return passado(verbo)
    else:
        return futuro(verbo)
conjuga('jogar','futuro')



##P43
#P43: Verificar se uma cadeia representa um número real (escrito na notação com ponto decimal). e_float(cadeia)
def e_float(cadeia):
    posicao = len(cadeia)-1
    if(cadeia[posicao]=='.'): return False
    elif(e_int(cadeia)==True):return True
    else: return False
e_float('3.3')

#P44: Determinar a cadeia formada pela parte inteira e a cadeia formada pela parte fracionária da representação de um número através de cadeia de caracteres. Se o número for inteiro, a parte fracionária será zero. int_frac(cadeia)

def int_frac(cadeia):
    posicao = 0
    fracao  = ''
    tail = ''
    for i in range(len(cadeia)):
        if(cadeia[i] == '.'):
            posicao = i
    for i in range(0,posicao):
        fracao = fracao + cadeia[i]
    for i in range(posicao+1,len(cadeia)):
        tail = tail + cadeia[i]
    if(posicao == 0):return cadeia,'0'
    else: return fracao,tail
int_frac("324.8765")

#P45: Dado um número de dois algarismo, produzir a cadeia de caracteres que seja a sua representação literal. traduz(numero)

def traduz(numero):

    if numero <= 9:
        return numeros_de_0_a_9(numero)
    elif 19 >= numero > 9:
        return numero_de_10_19(numero)
    elif 90 >= numero > 19:

        numero_inteiro = (numero // 10) * 10
        numero_fracionado = numero % 10
        if numero_fracionado != 0:
            a = numeros_20_a_90(numero_inteiro)
            b= numeros_de_0_a_9(numero_fracionado)
            return f'{a} e {b}'
        else:
            return numeros_20_a_90(numero_inteiro)
print(traduz(90))



