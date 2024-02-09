# String

palabra = "Hola"
word = 'hi'

# Numeros

entero = 5 # Entero, int, integer
decimal = 2.4 # decimal, float
complejo = 5j # complejo, complex

#----------------------------
# Listas

lista = [] # definiendo una lista vacia
la_lista = [1, 2, 3] # lista con elementos

# Métodos para listas

lista.append(1) # añade de uno en uno

lista.clear() # Limpia la lista, la borra

lista2 = lista.copy() # Copia lista a lista 2 y borra lo que tenía antes.

lista.count(4) # Cuenta cuantos 4 hay en la lista. Método contar.

len(lista) # Cuantos elementos hay en total
largo_de_lista = len(lista)

primer_elemnto = lista[0] # accediendo a elementos con indice. Primer elemento 0, último -1. contar de izquierda a derecha se usan positivos, y de derecha a izquierda se usan negativos.

lista.pop() # Elimina el último elemento de la lista
lista.remove("elemento en lista") # Elimina un elemento por su valor.

lista.reverse() # invierte el orden de la lista.
lista.sort()

print(lista2)
