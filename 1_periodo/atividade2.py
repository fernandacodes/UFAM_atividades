Python 3.10.2 (v3.10.2:a58ebcc701, Jan 13 2022, 14:50:16) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.

from math import *

# Questão 1

def xp(n) : return n>=0 and n<=100 and n%3==0 and n%5==0

#teste
xp(15)
True
xp(9)
False

# Questão 2 

def amarelo(y1,y2) : return (y1-y2)/sqrt(2)

#teste
amarelo(60, 35)
17.677669529663685
