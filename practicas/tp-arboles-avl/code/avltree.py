from linkedlist import *
from algo1 import *
from myqueue import *

class AVLTree:
	root = None
class AVLNode:
	parent = None
	leftnode = None
	rightnode = None
	key = None
	value = None
	bf = None

def newBinaryNode(key,value):
  newNode = AVLNode()
  newNode.value = value
  newNode.key = key
  return newNode

#----------------------------------------------------------------------
#Busca un elemento en el TAD arbol binario
#Devuelve la key asociada a la primera instancia del elemento. Devuelve None si el elemento no se encuentra.
def search(B,element):
  if B.root == None:
    return None
  else:
    #print(search(B.root,element))  DUDA: NO ME IMPRIME EL currentNode.key
    return searchR(B.root,element)
    
#-----------

def searchR(currentNode,element):
    if currentNode != None:
      if currentNode.value == element:
        return currentNode.key
      else:
        if currentNode.value > element:
         return searchR(currentNode.leftnode,element)
        else:
          if currentNode.value < element:
           return searchR(currentNode.rightnode,element)
    else:
      return None

def searchRkey(currentNode,key):
  if currentNode != None:
    if currentNode.key == key:
      return currentNode
    else:
      if currentNode.key > key:
        return searchRkey(currentNode.leftnode,key)
      else:
        if currentNode.key < key:
         return searchRkey(currentNode.rightnode,key)
  else:
    return None
      
#---------------------------------------------------------------------
#Si pudo insertar con éxito devuelve la key donde se inserta el elemento. En caso contrario devuelve None.  
def insert(B,element,key):
  newNode = newBinaryNode(key,element)
  currentNode = B.root

  if currentNode == None: #arbol vacio
    B.root = newNode
    return newNode.key
  else: #arbol NO vacío 
    if newNode.key > currentNode.key:
      if currentNode.rightnode == None:
        currentNode.rightnode = newNode
        newNode.parent = currentNode
        
        return newNode.key
      else:
        currentNode = currentNode.rightnode
        return insertR(currentNode,newNode)
    else:
      if newNode.key < currentNode.key:
        if currentNode.leftnode == None:
          currentNode.leftnode = newNode
          newNode.parent = currentNode
          return newNode.key
        else:
          currentNode = currentNode.leftnode
          return insertR(currentNode,newNode)
      else:
        #la key ya se encuentra en el arbol
       return None
#_______
#funcion insert recursiva
def insertR(currentNode, newNode):
  if newNode.key > currentNode.key:
    if currentNode.rightnode == None:
      currentNode.rightnode = newNode
      newNode.parent = currentNode
      return newNode.key
    else: 
      insertR(currentNode.rightnode,newNode)
  else:
    if newNode.key < currentNode.key:
      if currentNode.leftnode == None:
        currentNode.leftnode = newNode
        newNode.parent = currentNode
        return newNode.key
      else:
        insertR(currentNode.leftnode,newNode)

#----------------------------------------------------------------------
#Devuelve clave (key) del elemento a eliminar. Devuelve None si el elemento a eliminar no se encuentra.
def delete(B,element):
  currentNode = B.root
  #nodo a eliminar
  node = searchRE(B.root,element)
  if node == None:
    return None
  else:
    
    #VERIFICA SI EL NODO A ELIMINAR TIENE HIJOS
    #SI TIENE HIJOS ENTONCES BUSCA EL NODO SUSTITUTO --->
    
    #1. EL NODO A ELIMINAR NO TIENE HIJOS (por lo tanto no hay nodo sustituto)
    if node.rightnode == None and node.leftnode == None:
      if node.parent.leftnode == node:
        node.parent.leftnode = None
      else:
        node.parent.rightnode = None
      return node.key
    else:
      #2. EL NODO A ELIMINAR TIENE HIJOS:
      #1.tiene un hijo del lado izquierdo
      if node.rightnode == None:
        newNode = nodoSustitutoI(node.leftnode)
      else:
        #2.tiene un hijo del lado derecho o dos hijos 
        newNode = nodoSustitutoD(node.rightnode)

      #ACTUALIZA LOS VALORES DEL NODO QUE HAY QUE ELIMINAR
      if node == B.root:
        B.root.value = newNode.value
        B.root.key = newNode.key
      else:
        node.value = newNode.value
        node.key = newNode.key
        
      #ELIMINA EL NODO SUSTITUTODEPENDIENDO DE LA CANT DE HIJOS QUE TENGA
      #el nodo sust esta del lado izquierdo del padre
      if newNode.parent.leftnode == newNode:
        if newNode.rightnode == None:
          #si tiene cero hijos
          newNode.parent.leftnode = None
        else:
          #si tiene un hijo
          newNode.parent.leftnode = newNode.rightnode
        return node.key
      #el nodo sustituto esta del lado derecho del padre
      else:
        if newNode.rightnode == None:
          #si tiene cero hijos
          newNode.parent.rightnode = None
        else:
          #si tiene un hijo
          newNode.parent.rightnode = newNode.rightnode
        return node.key
      
#-----------  
def searchRE(currentNode,element):
  if currentNode != None:
    if currentNode.value == element:
      return currentNode
    else:
        return searchRE(currentNode.leftnode,element)
      #este código solo me sirve cuando comparó letras pero si quiero eliminar números tengo que usar > o >
     # else:
        #if currentNode.value < element or currentNode.value != element:
          #return searchRE(currentNode.rigthnode,element)
  else:
    return None
    
#----------
def nodoSustitutoD(currentNode):
  #menor de sus mayores (solo va a tener hijo a la derecha)
  if currentNode.leftnode == None:
    return currentNode
  else:
    return nodoSustitutoD(currentNode.leftnode)
    
def nodoSustitutoI(currentNode):
  #mayor de sus menores (solo va a tener hijo a la derecha)
  if currentNode.rightnode == None:
    return currentNode
  else:
    return nodoSustitutoI(currentNode.rightnode)

#----------------------------------------------------------------------
#Devuelve clave (key) a eliminar. Devuelve None si el elemento a eliminar no se encuentra.
def deleteKey(B,key):
  node = searchRE(B.root,key)
  
  if node == None:
    return None
  else:
    return delete(B,node.value)
#------------------------------------------------------------------------#Devuelve el valor de un elemento con una key del árbol binario, devuelve None si no existe elemento con dicha clave.
def access(B,key):
  node = searchRkey(B.root,key)
  if node == None: 
    return None
  else:
    return node.value
  
#------------------------------------------------------------------
#Devuelve None si no existe elemento para dicha clave. Caso contrario devuelve la clave del nodo donde se hizo el update.
def update(B,element,key):
  node = searchRkey(B.root,key)
  if node == None:
    return None
  else:
    node.value = element
    return node.key

#-----------------------------------------------------------------------
#Devuelve una lista (LinkedList) con los elementos del árbol en orden. Devuelve None si el árbol está vacío.
def traverseinOrder(B):
  if B.root == None:
    return None
  else:
    L = LinkedList()
    L = traverseinOrderAux(L,B.root)
    L = invertirLista(L)
    return L
    
def traverseinOrderAux(L,node):
  if node == None:
    return 
  else: 
    traverseinOrderAux(L,node.leftnode)
    add(L,node.value)
    traverseinOrderAux(L,node.rightnode)
    return L

#-----------------------------------------------------------------------------
#Devuelve una lista (LinkedList) con los elementos del árbol en post-orden. Devuelve None si el árbol está vacío.
def traverseInPostOrder(B):
  if B.root == None:
    return None
  else:
    L = LinkedList()
    traverseInPostOrderR(L,B.root)
    L = invertirLista(L)
    return L

def traverseInPostOrderR(L,node):
  if node == None:
    return
  else:
    traverseInPostOrderR(L,node.leftnode)
    traverseInPostOrderR(L,node.rightnode)
    add(L,node.value)
  return L
#-----------------------------------------------------------------------------
#Devuelve una lista (LinkedList) con los elementos del árbol en pre-orden. Devuelve None si el árbol está vacío.
def traverseInPreOrder(B):
  if B.root == None:
    return None
  else:
    L = LinkedList()
    traverseInPreOrderR(L,B.root)
    L = invertirLista(L)
    return L

def traverseInPreOrderR(L,node):
  if node == None:
    return
  else:
    add(L,node.value)
    traverseInPreOrderR(L,node.leftnode)
    traverseInPreOrderR(L,node.rightnode)
  return L

#-----------------------------------------------------------------------------
# Devuelve una lista (LinkedList) con los elementos del árbol ordenados de acuerdo al modo primero en amplitud. Devuelve None si el árbol está vacío.
#por niveles
def traverseBreadFirst(B):
  L = LinkedList()
  LList = LinkedList()
  enqueue(L,B.root)
  while L.head != None:
    currentNode = dequeue(L)
    add(LList,currentNode.value)
    if currentNode.leftnode != None:
      enqueue(L,currentNode.leftnode)
    if currentNode.rigthnode != None:
      enqueue(L,currentNode.rightnode)
  LList = invertirLista(LList)
  return LList

#-----------------------------------------------------------------------------
#hijo derecho es la nueva raiz
#la antigua raiz ahora es el hijo izq

  
def rotateLeft(Tree,avlnode):
  nuevaRaiz = avlnode.rightnode
  #si el nodo a rotar es la raiz
  if avlnode == Tree.root:
    #si la nueva raiz no tiene un hijo izquierdo
    if nuevaRaiz.leftnode == None:
      avlnode.rightnode = None
      
    else:
      #si la nueva raiz tiene un hijo derecho 
      avlnode.rightnode = nuevaRaiz.leftnode
      nuevaRaiz.leftnode.parent = avlnode

    nuevaRaiz.leftnode = avlnode
    avlnode.parent = nuevaRaiz
    Tree.root = nuevaRaiz
    return nuevaRaiz
  else: 
    
    if avlnode.parent.leftnode == avlnode:
      avlnode.parent.leftnode = nuevaRaiz
    else:
      avlnode.parent.rightnode = nuevaRaiz
    
    avlnode.parent = nuevaRaiz
    nuevaRaiz.parent = avlnode.parent
       
    if nuevaRaiz.leftnode == None:
      avlnode.rightnode = None
    else: 
      avlnode.rightnode = nuevaRaiz.leftnode

    nuevaRaiz.leftnode = avlnode
   
    return nuevaRaiz
  
#-----------------------------------------------------------------------------

#igual al anterior pero de forma inversa 
#devielvo la raiz nueva
def rotateRight(Tree,avlnode):
  nuevaRaiz = avlnode.leftnode
  #El nodo a rotar es la raiz 
  if avlnode == Tree.root:
    #si la nueva raiz tiene un hijo derecho
    if avlnode.leftnode.rightnode != None:
      #nuevaRaiz = avlnode.leftnode
      avlnode.leftnode = nuevaRaiz.rightnode
      nuevaRaiz.rightnode.parent = avlnode
    else:
      #si la nueva raiz no tiene un hijo derecho
      avlnode.leftnode = None
        
    nuevaRaiz.rightnode = avlnode
    avlnode.parent = nuevaRaiz
    Tree.root = nuevaRaiz
    return nuevaRaiz
      
  else:
    #si el nodo a rotar no es la raiz
    if avlnode.parent.leftnode == avlnode:
      #el hijo izquierdo del padre de avlnode (avlnode.parent.leftnode) 
      avlnode.parent.leftnode = nuevaRaiz
    else:
      avlnode.parent.rightnode = nuevaRaiz
    avlnode.parent = avlnode.leftnode
    #si la nueva raiz tiene un hijo derecho
    if avlnode.leftnode.rightnode == None:
      avlnode.leftnode.rightnode = avlnode
      avlnode.leftnode = None #importante, sino no se hace bien el arbol
      return nuevaRaiz
    else:
      #si la nueva raiz no tiene un hijo derecho
      avlnode.leftnode = avlnode.leftnode.rightnode
      avlnode.leftnode.parent.rightnode = avlnode
      return nuevaRaiz

#-----------------------------------------------------------------------------
#funcion recursiva
#calcula el bf
#bf = (cantidad de nodos a la izq) - (cantidad de nodos a la der)
#el bf es la altura max del nodo izq menos la altura max del nodo derecho 
#def altura(nodoI, nodoD):



def calculateBalance(AVLTree):
  if AVLTree.root == None:
    return 
  else:
    calculateBalanceR(AVLTree.root)

def calculateBalanceR(avlnode):
  if avlnode == None:
    return 
  else:
    avlnode.bf = altura(avlnode.leftnode) - altura(avlnode.rightnode)
    calculateBalanceR(avlnode.leftnode)
    calculateBalanceR(avlnode.rightnode)
    return avlnode.bf

def altura(avlnode):
  if avlnode == None:
    return
  else:
    return 1 + max(altura(avlnode.leftnode),altura(avlnode.rightnode))


  



#-----------------------------------------------------------------------------
#primr calculo el bf, si es 0,1 o .1 termino porq esta balanceado
#sino, aplico alguna rotacion para que se balancee
#salida: un arbol binario de busqeuda balanceado 


def rebalance(AVLTree): 
  calculateBalance(AVLTree)
  if AVLTree.root == None:
    return 
  else:
    recorreAbajoR(AVLTree,AVLTree.root)
    return AVLTree

def recorreAbajoR(T,node):
  if node == None:
    return 
  else: 
    if node.bf < -1:
      recorreAbajoR(T,node.rightnode)
    else:
      if node.bf > 1:
        recorreAbajoR(T,node.leftnode)
      else:
        rebalanceAux(T,node.parent)

def recorreArribaR(T,node):
  if node == None:
    return T
  else:
    if node.bf < 1 and node.bf > -1:
      recorreArribaR(T,node.parent)
    else:
      rebalanceAux(T,node)
  
def rebalanceAux(T,node):
  if node == None:
    return
  else:
    if node.bf < -1:
      if node.rightnode.leftnode != None:
        #si el hijo derecho tiene un hijo izquierdo
        #hago rotacion a la derecha del hijoderecho
        rotateRight(T,node.rightnode)
        #hago rotacin a la izquierda del nodo
        rotateLeft(T,node)
      else:
        rotateLeft(T,node)
      calculateBalance(T)
    else: 
      if node.bf > 1:
        if node.leftnode.rightnode != None:
          rotateLeft(T,node.leftnode)
          rotateRight(T,node)
        else:
          rotateRight(T,node)
        calculateBalance(T)
      else:
        recorreArribaR(T,node)

    

  




  
  
  


	


		
 


	

