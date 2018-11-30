#!/usr/bin/python3
    #author: João Vítor S. Fontoura
    #Date: 29/11/2018
    
#import de libs    
import functools

#function de maior divisor comum
def mdc(a, b):
    while b:
        a,b = b, a % b
    return a

#function menor multiplo comum
def mmc(a,b):
    return a*b // mdc(a,b)

#function menor multiplo comum chamando reduce() para soma de sequencia
def mmc2(res):
    return functools.reduce(mmc,res)

#entrada de valores     
a1 = int(input("Primeiro Valor da sequencia: ")) #assuma em digitar 1
a2 = int(input("Segundo Valor da sequencia: ")) #assuma em digitar 20

#criação de lista da sequencia usando a função range()
lst = range(a1,a2)

#Impressão de valores
print(mmc2(lst))
