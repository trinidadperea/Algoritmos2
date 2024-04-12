from calendar import c
import linkedlist

class Trie:
	root = None

class TrieNode:
    parent = None
    children = None   
    key = None
    isEndOfWord = False

#en esta clase de arboles trabajamos con cadenas

          
def insert(T,element):
  #La lista no esta creada
  if T.root.children == None:
  #creo la lista 
    T.root.children = linkedlist.LinkedList()
  #funcion recursiva que insertara el resto de los caracteres
  insertR(T.root.children,element,0,T.root)

def insertR(L, palabra, caracter,parent):
  #caso base
  if caracter == len(palabra): 
    return
  #debo averiguar si ya existe el caracter que quiero insertar
  if L == None:
    current = TrieNode()
    current.parent = parent
    current.children = linkedlist.LinkedList()
    current.key = palabra[caracter]
    linkedlist.add(L, current)
  else:
    current = L.head
    while current != None:
      #busco el caracter en la lista
      if current.value.key == palabra[caracter]:
        current = current.value
        break
      current = current.nextNode
    #si el caracter no existe en la lista, lo agrego
    if current == None:
      current = TrieNode()
      current.parent = parent
      current.children = linkedlist.LinkedList()
      current.key = palabra[caracter]
      linkedlist.add(L, current)
  #end of word
  if caracter == len(palabra)-1:
    current.isEndOfWord = True
    return 
  #llamo a la funcion recursiva para el próximo caracter
  #mis parametros son: la prox lista, la palabra, el prox caracter y el current que será el padre
  insertR(current.children, palabra, caracter+1,current)
          
         



     

  

         
         
      
