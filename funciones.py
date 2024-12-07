def saludar(nombre):
	return "Hola %s" % nombre

def sumar(*args):
    resultado = 0
    for i in args:
        resultado += i
    return resultado

def mayor_edad(edad):
	return edad > 18

def devolver_variable(var):
	return var

def devolver_none(var):
	return  None if (len(var) > 4) else "Hola"

def dividir(a, b):
	return a/b

def convertir_numero(a):
	try:
		numero = int(a)
	except ValueError:
		raise ValueError("No se pudo convertir a entero")
	return numero