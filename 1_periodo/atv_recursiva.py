#Escreva uma definição recursiva para a função norep(xs), 
#cuja avaliação associe uma lista similar a xs porém sem 
#nenhum elemento repetido.



def ocorre(x,xs):
    return [i for i in xs if x==i]

def norep(xs):
    if xs == []: return []
    elif ocorre(xs[0],xs[1:]) == []:
        return [xs[0]] + norep(xs[1:])
    else: return norep[xs[1:]]

#norep([9,9,3,4,3,4,2])
#[9, 3, 4, 2]
