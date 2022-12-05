#(1) Defina a função orx(a,b) onde a e b são valores lógicos e cuja avaliação 
# resulta em True caso um - e apenas um - dos parâmetros seja 
# True e resulta em False caso contrário. 

def orx(a,b): 
    if a or b == True: 
        return True
    else:
        return False

    
#orx(True,False)
#True
#orx(False,False)
#False


#(2) Defina a função pag(a,b,c) onde a, b e c são números 
#  e cuja avaliação resulta em True caso dois deles sejam termos 
#  de uma PA ou de uma PG e o outro seja a 
# razão - note que os termos e a razão podem ser informados em qualquer ordem.

def pag(a,b,c):
   
 def pag(a,b,c):
   if (b+a == c) or (c+a == b) or (b+c == a): 
       return True
   elif (c == b/a * b ) or (b == c/a * c ) or (c == b/a * b ): return True
   else: return False

   
#pag(3,5,7)
#True
#pag(2,4,8)
#True

#(3) Considere que o preço de uma passagem 
# de avião em um trecho, pode variar dependendo 
# da idade do passageiro. Pessoas com 60 ou mais anos de idade 
# pagam 60% do preço padrão. Crianças até 10 anos, pagam 50% e bebês 
# (abaixo de 2 anos) pagam apenas 10%. Escreva a função pgp(vl,i) cuja 
# avaliação associa um valor 
# a ser pago dados vl (valor nominal da passagem) e i (idade do passageiro).

def pgp(vl,i):
    if i>=60: return (vl*0.6)
    elif i <=10 and i>1: return (vl*0.5)
    elif i < 2: return (vl * 0.1)
    else: return vl

#pgp(1000,2)
#900.0
#pgp(2000,10)
#1000.0
#pgp(3000,60)
#1200.0