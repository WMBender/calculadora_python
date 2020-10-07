import math as m
def soma(a,b):
    return a+b

def subtracao(a,b):
    return a-b

def multiplicacao(a,b):
    return a*b

def divisao(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return "Erro: Divisão por zero"

def potenciacao(a,b):
    return pow(a,b)

def raizquadrada(a):
    return m.sqrt(a)

def km_to_mile(a):
    return a/1.609

def mile_to_km(a):
    return a*1.609

def kmh_to_ms(a):
    return a/3.6

def ms_to_kmh(a):
    return a*3.6

def inch_to_cm(a):
    return a*2.54

def cm_to_inch(a):
    return a/2.54

def foot_to_meter(a):
    return a/3.281

def meter_to_foot(a):
    return a*3.281
# a = int(input())
# function = ""
# b = int(input())
#  c = soma(a,b)
# c = function(a,b)
# print(c)
# c = subtracao(a,b)
# print(c)
# c = multiplicacao(a,b)
# print(c)
# c = divisao(a,b)
# print(c)
# c = potenciacao(a,b)
# print(c)
# c = raizquadrada(b)
# print(c)