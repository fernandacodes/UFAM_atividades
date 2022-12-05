#Defina a função placa(x) cuja avaliação resulta em um dos seguintes: 
# 'carro', 'moto', ou 'nada', dependendo se x é uma string válida para, 
# respectivamente, uma representação de 
# placa de carro, de placa de moto ou nenhuma das anteriores. 
# No Brasil, uma placa veicular no padrão Mercosul 
# tem atualmente a configuração LLLNLNN para carros e LLLNNLN para motos, 
# onde L denota uma letra e N um algarismo.

def valida_placa(x):
    contL = 0
    contn = 0
    for i in range(48,58):
        for j in range(len(x)):
            if(x[j]==chr(i)):
                contn = contn+1
    for i in range(65,123):
        for j in range(len(x)):
            if(x[j]==chr(i)):
                contL = contL+1
    if(contL !=4 and contn!=3):
        return False
    else:
        return True


def placa(x):
    c=0
    for i in range(48,58):
        if(x[5]==chr(i)):
            c +=1
    if(valida_placa(x)==False):
        return 'nada'
    elif(c>0):
        return 'carro'
    else:
        return 'moto'


#placa('BEE4R22')
#'carro'
#placa('bee42u2')
#'moto'
#placa('4444332')
#'nada'