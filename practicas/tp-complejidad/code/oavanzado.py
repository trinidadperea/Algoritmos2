from linkedlist import *

def bubbleSort(L):
    longitud = length(L)
    for i in range(0, longitud - 1):
        for j in range(0, longitud - 1):
        	if (access(L, j) > access(L, j + 1)):
        	    currentValue = access(L, j)
        	    update(L, access(L, j + 1), j) 
        	    update(L, currentValue, j + 1)
    return L

def selectionSort(L):
	longitud = length(L)
	for i in range(0, longitud - 1):
		smallestValue = access(L, i)
		for j in range(i, longitud - 1):			
			if(smallestValue > access(L, j+1)):
				smallestValue = access(L, j+1)
				positionToChange = j +1
		currentValue = access(L, i)
		update(L, smallestValue, i)
		update(L, currentValue, positionToChange)
	return L

def insertionSort(L):
	longitud = length(L)
	for i in range (0, longitud - 1):
		for j in range(i, longitud -1) :			
			if(access(L, i)  > access(L, j+1)):
				move(L, j+1, i)
	return L

#-------------------------------Ordenamient avanzado-------------------------------
def quickSort(L):
	Lfinal = LinkedList()
	Lfinal = quickSortRecursivo(L, Lfinal)

	L.head = None
	currentNode = Lfinal.head
	while(currentNode != None):
		add(L, currentNode.value)
		currentNode = currentNode.nextNode
	return L
	
	
	
def quickSortRecursivo(L, Lfinal):
	LMenor = LinkedList()
	LMayor = LinkedList()
	
	if(length(L) > 1):
		
		pivote = random.randint(0, length(L)-1)
		node = Node()
		node.value = access(L, pivote)
		LMayor.head = node
		currentNode = L.head
		
		while (currentNode != None):
			if(currentNode.value < node.value):
				add(LMenor, currentNode.value)
			elif(currentNode.value > node.value):
				add(LMayor, currentNode.value)
			currentNode = currentNode.nextNode
				
		quickSortRecursivo(LMenor, Lfinal)
		quickSortRecursivo(LMayor, Lfinal)
		
	elif(L.head != None):
		add(Lfinal, L.head.value)
		
	return Lfinal

def mergeSort(L):
	lista1 = LinkedList()
	lista2 = LinkedList()
	longitud = length(L)

	if(longitud > 1):
		for i in range(0, longitud):
			elemento = access(L, i)
			if(i < longitud // 2):
				add(lista1, elemento)
			else:
				add(lista2, elemento)
		mergeSort(lista1)
		mergeSort(lista2)

		L.head = None

		i = j = k = 0
		L.head = None
		
		while i < length(lista1) and j < length(lista2):
			if(access(lista1, i) < access(lista2, j)):
				insert(L, access(lista1, i), k)
				i += 1
			else:
				insert(L, access(lista2, j), k)
				j += 1
			k += 1

		while i < length(lista1):
			insert(L, access(lista1, i), k)
			i += 1
			k += 1

		while j < length(lista2):
			insert(L, access(lista2, j), k)
			j += 1
			k += 1



