Python 3.10.2 (v3.10.2:a58ebcc701, Jan 13 2022, 14:50:16) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
def pedrap(p):
    (l,r) = p
    return l>=0 and l<=6 and r>=0 and r<=6

def maop(m): return [ p for p in m if pedrap(p)] == m and len(m)<=7

def carrocap(crp):
    (l,r) = crp
    return pedrap(crp) and l==r

def tem_carroca_p(m):
	return [p for p in m if carrocap(p)] and maop(m)

    
def tem_carroca(m):
    return [k for k in m if maop(m)] and [k for k in m if carrocap(k) and tem_carroca_p(m)]

#Segunda Parte



# P06: Escreva a função pontos que associe uma lista de "pedras" a soma dos pontos das pedras nela contidos. Onde os pontos de uma pedra é a soma de suas pontas.

def pontos(p):
    return sum([pt1+pt2 for (pt1,pt2) in p])

#pontos([(2,3),(2,5),(3,5)])
#20


# P07: Escreva a função garagem que associe uma lista de "pedras" ao maior múltiplo de 5 (cinco), menor ou igual à soma dos pontos nela contidos.

def garagem(p):
    return (pontos(p)/5)*5

#garagem([(2,3),(2,5),(3,5)])
#20.0


# P08: Escreva a função pedra_igual_p que associe dois pares de inteiros a True sss representam a mesma pedra e False caso contrário. É bom lembrar que a ordem das pontas é irrelevante, assim (2,4) e (4,2) representam a mesma pedra.


def pedra_igual_p(p1,p2):
    (pt1,pt2) = p1
    (pt3,pt4) = p2
    return pt1 == pt3 or pt1 == pt4 and pt2 == pt3 or pt2 == pt4

#pedra_igual_p([2,3],[3,2])
#True


# P09: Escreva a função ocorre_pedra_p que associe uma "pedra" e uma "mão" a True sss a "pedra" ocorre na "mão" e False caso contrário.


def ocorre_pedra_p(m,p):
    (a,b) = p
    pi = (b,a)
    if [ i for i in m if i==p or i == pi]: return True
    else: return False

    
    
#ocorre_pedra_p([(2,3),(3,4),(2,2)],(2,6))
#False
#ocorre_pedra_p([(2,3),(3,4),(2,2)],(2,3))
#True
    


# P10: Escreva a função ocorre_valor_p que associe um valor válido para "ponta" e uma "mão" e produza True sss o valor ocorre em alguma pedra da mão e False caso contrário.

def ocorre_valor_p(m,p):
    i=0
    if [ i for i in m]:
        (a,b) = m[i]
        if a == p or b==p:
            return True
        else: return False

        
#ocorre_valor_p([(2,3),(3,4),(2,2)],2)
#True
#ocorre_valor_p([(2,3),(3,4),(2,2)],6)
#False



# P11: Escreva a função ocorre_pedra que associe a um valor e uma "mão", uma lista contendo as pedras da "mão" que possuem o valor dado.

def ocorre_pedra(m,p):
    (a,b) = p
    pi = (b,a)
    return [k for k in m if p==k or pi == k]

#ocorre_pedra([(2,3),(3,4),(2,2)],(2,2))
#[(2, 2)]
#ocorre_pedra([(2,3),(2,2),(3,4),(2,2)],(2,2))
#[(2, 2), (2, 2)]


# P12: Escreva a função pedra_maior que associe uma "mão" a pedra de maior valor na "mão" dada. Uma pedra p1 é maior que uma outra p2 sss a soma das pontas de p1 for maior que a soma das pontas de p2.


def pedra_maior(mao):
    maior = 0
    maiorsoma = 0
    for i in range(len(mao)):
        (a,b) = mao[i]
        soma = a+b
        if(soma > maiorsoma):
            maiorsoma = soma
            maior = mao[i]
    return maior

#pedra_maior([(2,3),(2,2),(3,4),(2,2)])
#(3,4)


# P13: Escreva a função ocorre_valor_q que associe um valor e uma "mão" e produza o número de pedras na mão que possuem o valor dado.

def ocorre_valor_q(m,p):
    cont = 0
    (a,b) = p
    pi = (b,a)
    for i in range(len(m)):
        if p == m[i] or m[i] == pi:
            cont = cont + 1
    return cont

#ocorre_valor_q([(2,3),(2,2),(3,4),(2,2)],(2,2))
#2
#ocorre_valor_q([(2,3),(3,2),(3,4),(2,2)],(2,3))
#2


# P14: Escreva a função ocorre_carroca_q que associe uma mão à quantidade de carroças nela existentes.

def ocorre_carroca_q(m):
	return len([p for p in m if carrocap(p)])

	
#ocorre_carroca_q([(2,3),(2,2),(3,4),(2,2),(2,2)])
#3
#ocorre_carroca_q([(2,3),(2,2),(3,4),(2,2),(2,5)])
#2
    


# P15: Escreva a função tira_maior que associe uma mão a uma lista similar à "mão" de onde foi extraída a pedra de maior ponto.
def tira_maior(m):
    return [i for i in m if i != pedra_maior(m)]

#tira_maior([(2,3),(2,5),(3,4),(2,2),(2,2)])
#[(2, 3), (3, 4), (2, 2), (2, 2)]
#tira_maior([(2, 3), (3, 4), (2, 2), (2, 2)])
#[(2, 3), (2, 2), (2, 2)]

# P16: Escreva a função tira_maior_v que associe um valor e uma "mão" à lista similar à "mão" de onde se extraiu a pedra de maior pontos de um determinado valor para ponta.

def tira_maior_v(m,p):
    return [i for i in m if i != pedra_maior(m) and i!=p]

#tira_maior_v([(2, 3), (2, 2)],(2,3))
#[(2, 2)]

