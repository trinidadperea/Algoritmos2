from algo1 import *
#linkedlist
class LinkedList:
  head = None
class Node:
  value = None
  nextNode = None


def printlinkedlist(L):
  newNode = Node()
  newNode = L.head
  print("L =",end = " ")
  while newNode != None:
    print(newNode.value,end = "," )
    newNode = newNode.nextNode
    #if newNode.nextNode == None:
      #print(newNode.value,end = " ")
  return

def printlinkedlistnombre(L):
  newNode = Node()
  newNode = L.head
  print("L =",end = " ")
  while newNode != None:
    print(newNode.value.nombre,end = "," )
    newNode = newNode.nextNode
   # if newNode.nextNode == None:
   #   print("",end = " ")
  return


  
def add(L,key,element):
  newNode = Node()
  newNode.value = element
  newNode.key = key
  newNode.nextNode = L.head
  L.head = newNode

  
#search 
#entrada: lista y elemento
#salida: la posicion
def search(L,element):
  currentNode = L.head
  pos = 0
  encontrado = 0
  while currentNode != None:
    if currentNode.value == element:
      encontrado = 1
      return pos
    currentNode = currentNode.nextNode
    pos = pos + 1
  if encontrado == 0:
    #no lo encuentra
    return None
    
#insert
#entrada: la lista, el elemento a insertar y la posicion
def insert(L, element, position):
  Current = Node()
  Current = L.head
  newNode = Node()
  newNode.value = element
  previous = Node()
  cont = 0

  if position <= length(L):
    if position == 0:
      newNode.nextNode = L.head
      L.head = newNode
      return position
    else:
      previous = None
      while Current != None and cont < position:
        previous = Current
        Current = Current.nextNode
        cont += 1
        if cont == position:
          previous.nextNode = newNode
          newNode.nextNode = Current
          return position

def deleteL(L,element):
  Current = Node()
  Current = L.head
  previousNode = Node()
  borrado = False
  cont = 0

  while Current != None and borrado == False:
    if Current.nextNode != None:
      print(" ")
      if Current.value == element:
        if cont == 0: 
          L.head = Current.nextNode
          borrado = True
          return cont
        else: 
          previousNode.nextNode = Current.nextNode
          borrado = True
          return cont         
      else:
        previousNode = Current
        Current = Current.nextNode
        cont += 1
    else:
      if Current.value == element:
        if cont == 0 :
          L.head = None
          borrado = True
          return cont
        else:
          previousNode.nextNode = None
          borrado = True
          return cont
      else:
        return None
def deletePosicion(L,posicion):
  Current = Node()
  Current = L.head
  previousNode = Node()
  borrado = False
  cont = 0

  while Current != None and borrado == False:
    if Current.nextNode != None:
      if cont == posicion:
        if cont == 0: 
          L.head = Current.nextNode
          borrado = True
          return L
        else: 
          previousNode.nextNode = Current.nextNode
          borrado = True
          return L         
      else:
        previousNode = Current
        Current = Current.nextNode
        cont += 1
    else:
      if cont == posicion:
        if cont == 0 :
          L.head = None
          borrado = True
          return L
        else:
          previousNode.nextNode = None
          borrado = True
          return L
      else:
        print("n")
        return None      


def length(L):
    currentNode = L.head
    size = 0
    while currentNode != None:
        size += 1
        currentNode = currentNode.nextNode
    return size

#devuelve el valor del elemento en la posicion ingresada
def access(L,position):
  currentNode = L.head
  cont = 0
  while currentNode != None:
    if cont > position:
      return None
    else: 
      if cont == position:
        val = currentNode.value
        return val
      else:
        cont = cont + 1
        currentNode = currentNode.nextNode
#cambia el valor de una posicion 
def update(L,element,position):
  currentNode = L.head
  pos = 0
  while currentNode != None:
    if pos > position:
      #posicion muy grande, sale del bucle
      return None
    else:
      #comparo la posicion con el contador
      #si es igual le pongo su nuevo valor
      if pos == position:
        currentNode.value = element
        return pos
    pos = pos + 1
    currentNode = currentNode.nextNode
#calculo de o(f)
#add: O(1)
#search: O(n)
#insert: O(n)
#delete: O(n)
#length: O(n)
#access: O(n)
#update: O(n)
def CheckCycles(L):
  current = L.head
  contcycles = 0
  #recorro la lista
  while current.nextNode != None:
    #tiene un ciclo sobre si mismo 
    if current.nextNode == current:
      contcycles = 1
    else:
      #tiene un ciclo cin otro 
      if current.nextNode.nextNode == current:
        contcycles = 1
    current = current.nextNode
    
  if contcycles == 1:
    #tiene un ciclo
    return True
  else:
    #no tiene un ciclo
    return False

def invertirLista(L):
  Current = L.head
  pos = 0

  while Current != None:
    if Current != L.head:
      deletePosicion(L,pos)
      add(L,Current.value)

      Current = Current.nextNode
    else:
      Current = Current.nextNode
    pos += 1
  return L


