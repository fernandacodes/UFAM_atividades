#parte 1

#P01: Escreva a função pedrap que associe um par a True se e somente se (sss) o par é uma representação válida para uma "pedra" e False caso contrário. 
#pedrap(2,7) ==> False
#pedrap((-3),4) ==> False
#pedrap(3,4) ==> True

def pedrap(p):
    (l,r) = p
    return l>=0 and l<=6 and r>=0 and r<=6

#pedrap([2,7])
#False
#pedrap([3,6])
#True

#P02: Escreva a função maop que associe uma lista de pares de inteiros a True sss a lista é uma representação #válida para a "mão" de um jogador e False caso contrário.

def maop(m): return [ p for p in m if pedrap(p)] == m and len(m)<=7

#maop([(3,5),(5,7),(4,4)])
#False
#maop([(3,5),(5,6),(4,4)])
#True


#P03: Escreva a função carrocap que associe um par a True sss o par é uma "carroça" e False caso contrário.

def carrocap(crp):
    (l,r) = crp
    return pedrap(crp) and l==r

#carrocap([5,4])
#False
#carrocap([5,5])
#True



#P04: Escreva a função tem_carroca_p que associe uma "mão" a True sss a mão possuir pelo menos uma #carroça e False caso contráqrio.


def tem_carroca_p(m):
	return [p for p in m if carrocap(p)] and maop(m)

tem_carroca_p([(3,5),(5,6),(4,4)])


#P05: Escreva a função tem_carrocas que associe a uma "mão" a lista das "carroças" nela contida.

def tem_carroca(m):
    return [k for k in m if maop(m)] and [k for k in m if carrocap(k) and tem_carroca_p(m)]

#teste
#tem_carroca([(2,3),(3,3),(2,2)])
#[(3, 3), (2, 2)]


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




#terceira parte



#P17: Escreva a função mesap que associe uma quadrupla de listas a True sss a quadrupla for uma descrição válida de "mesa".


def mesap(lista):
    novalista = []
    cont = 0
    for i in range(len(lista)):
        novalista = novalista+lista[i]
    for i in range(len(novalista)):
        if(novalista[i]>6):
            cont = cont+1
            break
    if(cont>0 or len(lista)!=4):
        return False
    else:
        return True


#teste
#mesap(([5],[5,5],[0],[5]))
#True


#P18: Escreva a função carroca_m_p que associe uma mesa a True sss pelo menos uma das pontas for carroça.

def carroca_m_p(lista):
    num  = []
    carroca = False
    for i in range(len(lista)):
        if(len(lista[i])==2):
            num = lista[i]
    if(len(num)==2 and num[0]==num[1]):
        carroca = True
    else:
        carroca = False
    if(mesap(lista)and carroca == True):
        return True
    else:
        return False

    
#carroca_m_p(([5],[5,5],[0],[5]))
#True


#P19: Escreva a função pontos_marcados que associe uma mesa ao o número de pontos a serem marcados se a soma das pontas for múltiplo de cinco e zero em caso contrário.

def pontos_marcados(lista):
    cont = 0
    novalista = []
    somapontas = []
    for i in range(len(lista)):
        somapontas = sum(lista[i])
        if(somapontas%5==0):
            cont = cont+1
        novalista = novalista+lista[i]
    somalista = sum(novalista)
    if(somalista%5==0 and cont==4 and mesap(lista)==True):
        return somalista
    else:
        return 0

    
#pontos_marcados([[5],[5,5],[5],[5]])
#25
#pontos_marcados([[5],[5,5],[0],[5]])
#20


#P20: Escreva a função pode_jogar_p que associe uma "pedra" e uma "mesa" a True sss a pedra possui uma ponta que combina com pelo menos uma das pontas da mesa.

def pode_jogar_p(lista,pedra):
    novalista = []
    (a,b) = pedra
    for i in range(len(lista)):
        novalista = novalista+lista[i]
    for i in range(len(novalista)):
        if(novalista[i]==a or novalista[i]==b and mesap(lista)==True):
            return True
        else:
            return False

        

#pode_jogar_p([[5],[5,5],[0],[5]],(2,3))
#False
#pode_jogar_p([[5],[5,5],[0],[5]],(2,5))
#True


#P21: Escreva a função marca_ponto_p que tenha como entrada uma "pedra" e uma "mesa" e produza True sss a pedra pode ser jogada fazendo pontos em uma das pontas da mesa. Lembre-se que as carroças devem ser contadas pelas duas pontas da pedra.


def marca_ponto_p(mesa,pedra):
    (a,b) = pedra
    novapedra = []
    novamesa = []
    for i in range(len(mesa)):
        novamesa = novamesa+mesa[i]
    for i in range(len(novamesa)):
        if(novamesa[i]==a or novamesa[i]==b and mesap(mesa)==True):
            return True
        else:
            return False


#marca_ponto_p([[5],[5,5],[5],[5]],(2,5))
#True





#P22: Escreva a função maior_ponto que associa uma pedra e uma mesa ao número da "ponta" da mesa onde pode ser marcado o maior valor de ponto que será marcado pela pedra. Considere que a em uma "mesa" as pontas são numeradas a partir de zero, da esquerda para a direita.


def maior_ponto(mesa,pedra):
    a = pedra[0]
    b = pedra[1]
    cont  = 0
    novamesa = []
    for i in range(len(mesa)):
        novamesa = novamesa+mesa[i]
    for i in range(len(novamesa)):
        if(novamesa[i]==a or novamesa[i]==b):
            cont = i
            break
        else:
            cont = 100
    if(cont==100 or a>6 or b>6):
        return 'jogada invalida'
    if(a>b):
        return a
    else:
        return b

#maior_ponto([[5,5],[3],[4],[2]],[5,5])
#5

#P23: Escreva a função joga_pedra que associe uma "pedra", uma "mesa" e um número de "ponta" da mesa a uma nova mesa obtida ao se jogar a "pedra" na "ponta" indicada.

def joga_pedra(mesa,pedra,ponta):
    novalista = []
    novamesa = []
    novapedra = []
    novamesa = []
    for i in range(len(mesa)):
        novalista = novalista+mesa[i]
        for i in range(len(novalista)):
            if(novalista[i]==ponta[0]):
                novapedra = mesa[i-1]
    for i in range(len(mesa)):
        if(mesa[i]!=novapedra):
            novamesa =  novamesa + [mesa[i]]
    novamesa = novamesa+[ponta]
    if(mesap(mesa)and novapedra!=[]):
        return novamesa
    else:
        return 'mesa invalida'

    
#joga_pedra([[5,5],[5],[5],[0]],[4,5],[5])
#[[5, 5], [0], [5]]



#P24: Escreva a função jogap que associe uma "mão" e uma "mesa" e produza True sss existe pelo menos uma pedra na mão que possa ser jogada em pelo menos uma ponta da mesa. Caso contrário produza False.

def jogap(mesa,mao):
    cont = 0
    lista = []
    nova_mao = []
    for i in range(len(mao)):
        nova_mesa = []
        nova_mao = nova_mao+mao[i]
        for j in range(len(mesa)):
            nova_mesa = nova_mesa+mesa[j]
    for i in range(len(nova_mesa)):
        for j in range(len(nova_mao)):
            if(nova_mesa[i]==nova_mao[j]):
                cont = cont+1
    if(cont>0):
        return True
    else:
        return False

    
#jogap([[5,5],[3,5],[4,2],[5]],[[3,2],[5,5],[2]])
#True


#P25: Escreva a função jogada que associe uma "mão" e uma "mesa" ao número da pedra na mão e número da ponta na mesa onde pode ser feita a jogada que marque mais ponto. Considere inclusive jogada onde não há marcação de ponto.

def jogada(mao,mesa):
    cont = 0
    lista = []
    nova_mao = []
    maior = 0
    pontamaior = 0
    for i in range(len(mao)):
        nova_mesa = []
        nova_mao = nova_mao+mao[i]
        for j in range(len(mesa)):
            nova_mesa = nova_mesa+mesa[j]
            if(nova_mesa[j]>pontamaior):
                pontamaior = j
    for i in range(len(nova_mesa)):
        for j in range(len(nova_mao)):
            if(nova_mesa[i]==nova_mao[j]):
                lista = lista +[nova_mesa[i]]
    if(len(lista)==0):
        return 0
    elif(len(lista)>0):
        for i in range(len(lista)):
            if(lista[i]>maior):
                maior = i
    return lista[maior],nova_mesa[pontamaior]


#jogada([[2,2],[4,1],[2,3],[5,2]],[[5],[5,5],[0],[5]])

#(5, 5)




#P26: Escreva a função faz_jogada que associe uma "mão" e uma "mesa" e produza uma nova "mesa" obtida por se jogar marcando o maior número de pontos possível


def faz_jogada(mao_do_jogador, mesa):

    pedra, _, m_ponto_default = localiza_pedra(mao_do_jogador, mesa)[0]
    return joga_pedra(pedra, mesa, m_ponto_default)



def suma(values):
    if len(values) == 0:
        return 0

    return topo(values) + suma(baixa(values))


def topo(mesa_itens):
    if len(mesa_itens) == 0:
        return []
    else:
        return mesa_itens[0]


def baixa(mesa_itens):
    if len(mesa_itens) == 0:
        return []
    else:
        return mesa_itens[1:]


def pedrap_is(pedra):

    if len(pedra) == 0:
        return True
    return pedrap((topo(pedra), topo(pedra))) and pedrap_is(baixa(pedra))

def sum_pontas(pontas):
    if len(pontas) == 0:
        return 0
    return suma(pontas[0]) + sum_pontas(pontas[1:])


def pontos_marcados_v(mesa):
    if multiplo_cinco(sum_pontas(mesa)) == sum_pontas(mesa):
        return sum_pontas(mesa)
    else:
        return 0


def validar_p(pontas, mao_do_jogador):

    if len(pontas) == 0:
        return False

    return ocorre_valor_p(topo(pontas), mao_do_jogador) or validar_p(
        baixa(pontas), mao_do_jogador
    )
def aponta(nib, nova_pedra):

    nova_pedra_a, nova_pedra_b = nova_pedra

    return nova_pedra_a == nib or nova_pedra_a == nib or nova_pedra_b == nib or nova_pedra_b == nib    
def pedras_com_encaixe(ponta, mao_do_jogador):
    return [pedra for pedra in mao_do_jogador if aponta(ponta, pedra)]

def ocorre_valor_p(ponta, mao_do_jogador):

    return len(pedras_com_encaixe(ponta, mao_do_jogador)) != 0



def nova_ponta(pedra, ponta):
    if pedra[0] == ponta[0] and pedra[0] != pedra[1]:
        return [pedra[1]]
    elif pedra[0] == ponta[0] and pedra[0] == pedra[1]:
        return [pedra[0], pedra[1]]
    else:
        return [pedra[0]]


def localizar_index(lado_a, mesa):
    indece = []
    for ind in range(0, len(mesa)):
        if len(mesa[ind]) != 0 and lado_a == mesa[ind][0]:
            indece.append(ind)

    return indece


def encontrar_ponto(defaults, pedra, mesa):
    if len(defaults) == 0:
        return False

    return pontos_marcados(
        joga_pedra(pedra, mesa, topo(defaults))
    ) or encontrar_ponto(baixa(defaults), pedra, mesa)


def m_mais_ponto(pedra, mesa):

    defaults = localizar_index(pedra[0], mesa) + localizar_index(pedra[1], mesa)

    maior_ponto = 0
    maior_ponto_default = 0

    for auxiliar in defaults:
        if maior_ponto <= sum_pontas(joga_pedra(pedra, mesa, auxiliar)):
            maior_ponto = sum_pontas(joga_pedra(pedra, mesa, auxiliar))
            maior_ponto_default = auxiliar

    return (maior_ponto, maior_ponto_default)


def localiza_pedra(mao_do_jogador, mesa):

    grande_ponto = 0

    pedras = []

    for pedra in mao_do_jogador:
        m_ponto, m_ponto_default = m_mais_ponto(pedra, mesa)
        if m_ponto > grande_ponto:
            grande_ponto = m_ponto
            pedras = [(pedra, m_ponto, m_ponto_default)]
        elif m_ponto == grande_ponto:
            pedras.append((pedra, m_ponto, m_ponto_default))

    return pedras