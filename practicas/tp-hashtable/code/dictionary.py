from os import link
from algo1 import *
from linkedlist import *
import math



class dictionaryNode:
	value = None
	key = None
	nextNode = None

class dictionary:
	head = None


def printhash(D):
	for i in range(0,len(D)):
		if D[i] != None:
			print("pos ",i,":",end= " ")
			printlinkedlist(D[i])
			print("")
		else:
			print("pos ",i,":", "none")
	return
			

#Descripción: Inserta un key en una posición determinada por la función de hash (1)  
#en el diccionario (dictionary). Resolver colisiones por encadenamiento. 
#En caso de keys duplicados se anexan a la lista.
#Entrada: el diccionario sobre el cual se quiere realizar la inserción  y el valor del key a insertar. 
#Salida: Devuelve D

def insert(D,key,value):
	m = 9
	insertdiv(m,D,key,value)


def insertdiv(m,D,key,value):
	pos = int(key % m)
	if D[pos] == None:
		D[pos] = LinkedList()
		add(D[pos],key,value)
	else:
		add(D[pos],key,value)
	#printlinkedlist(D[h])
	return D

#Descripción: Busca un key en el diccionario
#Entrada: El diccionario sobre el cual se quiere realizar la búsqueda (dictionary) y 
#el valor del key a buscar.
#Salida: Devuelve el value de la key. Devuelve None si el key no se encuentra.

#search con div
def search(D,key):
	m = 9
	searchdiv(m,D,key)

def searchdiv(m,D,key):
	encontro = False
	pos = int(key % m)
	if D[pos] != None:
		current = D[pos].head
		while current != None:
			if current.key == key:
				break
			current = current.nextNode
		if current == None:
			return None
		else:
			return current.value
		
#Descripción: Elimina un key en la posición determinada por la función de hash (1) del diccionario
#Poscondición: Se debe marcar como None el key a eliminar.  
#Entrada: El diccionario sobre el se quiere realizar la eliminación  y el valor del key que se va a eliminar.
#Salida: Devuelve D

#delete con div
def delete(D,key):
	m = 9
	deletediv(m,D,key)

def deletediv(m,D,key):
	pos = int(key % m)
	if D[pos] == None:
		return D
	else: #busco el key a eliminar
		current = D[pos].head
		while current != None:
			if current.key == key:
				current.key = None
				current.value = None
				break
			else:
				current = current.nextNode
		return D
		
#-----------------------------------------------------------
#Parte 2

#ejercicio 4

#devuelva True o False si uno es pemutacion de otro
#entra s y p, devolver true si p s permutacion de s

#utilizamos esta funcion para calcular el codigo ascii de cada cadena
def calcular_numero(cadena):
    total = 0
    for caracter in cadena:
        total += ord(caracter)
    return total

def permutation(s,p):
	if len(s) != len(p):
		return False #si tienen distinta long no pueden ser permutacion
	#calculamos el codigo ascii de cada cadena, si da el mismo nro es porq son permutacion
	if calcular_numero(s) == calcular_numero(p):  #complejidad del algoritmo, O(n)
		return True
	else:
		return False
	
#-----------------------------------------------------------
#ejercicio 5

#Implemente un algoritmo que devuelva True si la lista que recibe de entrada
#tiene todos sus elementos únicos
def unicos(L):
	if len(L) < 1:
		return True #si la lista tiene un solo elemento es unico
	else:
		i = 0
		primero = L[0]
		cont = 0
		j = 0
		while i < len(L): 
			if primero == L[j]:
				cont += 1
				if cont == 2:  #cuando sa dos conto a si mismo y a otro, entonces False
					print("Falso, el numero: ",primero, " se repite en la posicion: ",i + 1," y en la posicion: ",j + 1)
					return False #tiene elementos repetidos
			j += 1
			if j == len(L):
				j = 0
				i += 1
				cont = 0
				if i == len(L):
					return
				else:
					primero = L[i]
		return True
#algoritmo que devuelva true i hay elementos repetidos en la lista
#implementacion con hashtable
def numPrimo(n):  #funcion que dado un n me devuelve el numero primo q esta antes de n/2
	if (n/2) <= 2:
		m = prevprime(n)
	else:
		if (n/2) % 2 == 0:
			m = prevprime(n/2)
		else:
			m = int(n/2)
	return m

def prevprime(n):
	num = n + 1
	while num > 1:
		if calcular_primo(num): #si es primo el num anterior lo devuelvo
			return num
		num -= 1
	return None #no encuentra un nro primo anterior

def calcular_primo(n): #esta funcion tiene que devolver el numero primo anterior a n
	for i in range (2,int(n**0.5) + 1):
		if n % i == 0: #encontramos un divisor, entonces no es primo
			return False
	return True


def unicos_hash(L):
	D = dictionary()
	m = 9 #numPrimo(len(L))
	D = [None]*m  #lleno una hash con todos sus elementos none
	current = None
	for i in range(0,len(L)):
		current = search(D,L[i])
		if current != None: #si es distinto a none, es porq ya fue insertado
			print("elemento repetido")
			return 
		else: #si es igual a none, lo inserto en la hash
			insert(D,L[i],L[i])
	print("no hay repetidos")
	return 
#-----------------------------------------------------------
#ejercicio 7

#realizar la comprension basica de una cadena
#contar los caracteres repetidos, y pasarlos a numeros
#por ejemplo aabcccccaaa seria: a2b1c4a3


def caracteres_repetidos(palabra):  
	m = ord("z") #todas las letras del abecedario, cada una tiene su valor entonces no van a repetirse
	#a no ser que sea la misma letra 
	D = dictionary()
	D = [None]*m
	resultado = ""
	valor = 1
	for i in range(0,len(palabra)):
		letra = palabra[i]
		node = searchdiv(m,D,ord(letra))
		if node == None: #si no lo encuentro lo insert
			insertdiv(m,D,ord(letra),valor) 
			node = searchdiv(m,D,ord(letra)) #el campo value me va a devolver las ocurrencias
		else:
			valor += 1 #si lo encontro, entonces sumo a la ocurrencia (value)
		if i < (len(palabra)-1): #no estamos en la ultima letra
			if palabra[i+1] != letra: #si la letra que sigue es distinta, entonces concateno con su recurrencia
				resultado += letra + str(valor)
				valor = 1 #reinicio por si mas adelante se repite la letra
		else: #ultimo caracter
			if i == (len(palabra)-1):
				resultado += letra + (str(valor))
				valor = 1
	if len(resultado) > len(palabra):
		print(palabra) #deuvelvo la original, ya que la comprimida no es menor
		return palabra
	else:
		print(resultado)
		return resultado
	
#-----------------------------------------------------------
#ejercicio 8

#dadas des palabras, indicar el indice donde arranca la palabra mas corta en la palabra mas larga
#Ejemplo 1:
#Entrada: S = ‘abracadabra’ , P = ‘cada’
#Salida: 4, índice de la primera ocurrencia de P dentro de S (abracadabra)

def ocurrencia(larga,corta):
	for i in range(0,len(larga)): #el for va a correr en toda la longitud de la cadena mas larga
		if larga[i] == corta[0]:
			if larga[i:i + len(corta)] == corta: #si la subcadena desde i hasta longitud de la corta es igual a la corta, 
				#entonces devuelvo i que seria la posicion donde inicia la corta
				print(i)
				return i
	return None #si no retorna i es porq no esta esa palabra mas corta dentro de la otra, devuelvo None
#-----------------------------------------------------------
#ejercicio 9
#Implemente un algoritmo que utilice una tabla de hash para determinar si S ⊆ T (S subconjunto de T).

def subconjunto(S,P):  #decir si s es subconjuto de p
	m = ord("z")
	D = dictionary()
	D = [None]*m
	if len(S) > len(P): #si la longitud de s es mayor a la de p, ya no puede ser suconjunto
		return None
	else:
		#hago una hash del conjunto mas grande e inserto sus letras
		for i in range(0,len(P)):
			insertdiv(m,D,P[i],P[i]) #value == key

		for i in range(0,len(S)): #busco los elementos de s en p, si no hay uno no es subconjunto
			if searchdiv(m,D,S[i]) == None:
				print("no es subconjunto")
				return None
		print("es subconjunto")
		return True
  














	









		







		
