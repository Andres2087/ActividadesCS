# -*- coding: utf-8 -*-

# Calcula la sumatoria total de los valores de un arreglo de enteros
def total(lst):
    accum=0
    for x in lst:
        accum=accum+x
    return accum

lst=[1,2,3,4]
res = total(lst)
print(res)


# Se agrega 5 al numero que se envia
def addit(x):
    y = x+5
    return y
res = addit(3)
print(res)


# Multiplica el numero enviado por el numero enviado + 5
def mult(z):
    q = z * addit(z)
    return q
res = mult(3)
print(res)

# Divide el numero a enviado entre el numero b enviado
def divide(a, b):
    return a/b
res = divide(8, 2)
print(res)

# Calcula el tamaño de una lista o string y devuelve un valor segun el tamaño
def length(lst):
    if len(lst) >=5:
        return "Longer than 5"
    else:
        return "Less than 5"
res = length([2, 3, 5, 2])
print(res)
res = length("Prueba")
print(res)

#Recibe un string y lo devulve al reves -> Ejemplo: casa -> asac

def reverse(mystr):
    reversed = ''
    for char in mystr:
        reversed = char + reversed
    return reversed

res = reverse("casa")
print(res)

#Recibe por parametro un string y una letra y se reemplaza la letra que se requera
def remove_letter(theLetter, theString):
    if theLetter in theString:
        return theString.replace(theLetter,"")
    else:
        return theString

res = remove_letter("a", "Hola esto es una prueba")
print(res)

#Recibe una arrelo de numeros y devuelve el numero mayor

def max(lst):
    max = 0
    for e in lst:
        if e > max:
            max = e
    return max

res = max([1, 8, 3, 0, 12])
print(res)


#recibe una lista de numeros y devuelve solo los elementos pares

def even_numbers(mix):
    ev_li = []
    for i in mix:
        if (i % 2 == 0):
            ev_li.append(i)
    return ev_li

res = even_numbers([1, 8, 3, 6, 12, 5])
print(res)

#recibe una lista de numeros y devuelve solo los elementos impares

def odd_numbers(mix):
    od_li = []
    for i in mix:
        if (i % 2 != 0):
            od_li.append(i)
    return od_li
res = odd_numbers([1, 8, 3, 6, 12, 5])
print(res)

#Recibe un numero, y devuelve un booleano, donde indica si es par

def is_even(number):
    return number % 2 == 0
res = is_even(23)
print(res)

