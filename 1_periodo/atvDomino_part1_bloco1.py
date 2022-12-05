Python 3.10.2 (v3.10.2:a58ebcc701, Jan 13 2022, 14:50:16) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
#parte 1

#P01: Escreva a função pedrap que associe um par a True se e somente se (sss) o par é uma representação válida para uma "pedra" e False caso contrário.

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


#P04: Escreva a função tem_carroca_p que associe uma "mão" a True sss a mão possuir pelo menos uma #carroça e False caso contrário.

def tem_carroca_p(m):
	return [p for p in m if carrocap(p)] and maop(m)

    
#tem_carroca_p([(3,5),(5,6),(4,4)])
#True


#P05: Escreva a função tem_carrocas que associe a uma "mão" a lista das "carroças" nela contida.

def tem_carroca(m):
    return [k for k in m if maop(m)] and [k for k in m if carrocap(k) and tem_carroca_p(m)]

#teste
#tem_carroca([(2,3),(3,3),(2,2)])
#[(3, 3), (2, 2)]