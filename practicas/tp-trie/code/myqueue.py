from algo1 import *
from linkedlist import * 

def enqueue(Q,element):
  add(Q,element)
  return

#extraigo el ultimo elemento de la cola
#devuelvo el elemento que elimino 
def dequeue(Q):
  current = Q.head
  cont = 0
  if current != None:
    while current.nextNode != None:
      current = current.nextNode
      cont = cont + 1
    delete(Q,current.value)
    return current.value
  else:
    return None