
from linkedlist import *
from algo1 import *
from myqueue import dequeue, enqueue


def printgrafo(grafo):
    for i in grafo:  #imprimo cada linkedlist de mi array de vertices
        printlinkedlist(i)
        print(" ")
    return 

#Ejercicio 1

#Implementar la función crear grafo 
#dada una lista de vértices y una lista de aristas 
#cree un grafo con la representación por Lista de Adyacencia.

#entrada: 2 linkedlist, lis_v para vertices, list_a para aristas
#salida: el nuevo grafo

def createGraph(List_v, List_a):
    n = length(List_v)
    graph = Array(n,LinkedList())
    i = 0
    current = List_v.head
    #guardo en la primer celda de cada fila el valor del vertice
    while current != None:
        graph[i] = LinkedList()  #creo una lista de adyacencia para cada vertice
        add(graph[i],current.value)
        current = current.nextNode 
        i += 1

    current = List_a.head
    while current != None:
        #busco en la lista de aristas el primer valor, y le agrego a esa lista el segundo valor del parentesis
        #que seria la arista. Por ej: (1,2) lo que hago es buscar en la lista el vertice 1, y le agrego 
        #el vertice de valor 2 a su linkedlist
        #uso search porq me devuelve la posicion del vertice

        ubic0 = search(List_v,current.value[0]) #me devuelve la pos
        ubic1 = search(List_v,current.value[1]) #me devuelve la pos

        add(graph[ubic0],current.value[1])
        #hago lo mismo pero al reves
        add(graph[ubic1],current.value[0])  #si saco este solo voy a estar mostrando una vez
        #la conexion de cada vertice, no ida y vuelta (es lo mismo si lo pongo o no)
        current = current.nextNode
    return graph

#--------------------------------------------------------------------------------------------
#ejercicio 2

#Descripción: Implementa la operación existe camino que busca si existe un camino entre 
#los vértices v1 y v2 

#Entrada: Grafo con la representación de Lista de Adyacencia, v1 y v2 vértices en el grafo.

#salida: retorna True si existe camino entre v1 y v2, False en caso contrario.
def existPath(grafo,v1,v2):
  if len(grafo) == 1: #caso 1: n = 1
    print("camino")
    return True
  else: #caso 2
    #buscar la posicion de v1 en el arreglo (columna 0)
    pos = posicionvertice(grafo,v1) 
    if search(grafo[pos],v2): #si v2 esta en la linkedlist de v1
      print("camino")
      return True
    else:
      L = list()
      L.append(v1) #hago una lista aux para guardar los vertices que ya he visitado
      return existPathR(grafo,grafo[pos],grafo[pos].head.nextNode,grafo[pos].head.nextNode,L,v2)
                            #lista de v1, nodo 1 de la lista de v1

def existPathR(grafo,list,current,node,L,v2):
  if node == None:#termino de recorrer list y no encontro v2
    if current.nextNode != None:
      current = current.nextNode #pasa al siguiente nodo de la lista de v1
      pos = posicionvertice(grafo,current.value)
      return existPathR(grafo,grafo[pos],current,grafo[pos].head.nextNode,L,v2)
    else:
      print("no hay camino")
      return False
  else:
    if search(list,v2): 
      print("camino")
      return True
    else:
      if node.value in L: #si el vertice ya fue visitado
        return existPathR(grafo,list,current,node.nextNode,L,v2) #paso al siguiente vertice de list
      else: #si no fue visitado
        L.append(node.value) #lo agrego a la lista aux
        pos = posicionvertice(grafo,node.value) #busco la pos de la lista del v actual
        nodeListaNueva = grafo[pos].head.nextNode #tomo el primer vertice de la lista de v actual
        if nodeListaNueva != None:
          if nodeListaNueva.value not in L: #si no lo he visitado, voy a la list de v
            return existPathR(grafo,grafo[pos],current,nodeListaNueva,L,v2)
          else: 
            if nodeListaNueva.nextNode == None: #si ya no hya mas vertices por verficar en esa lista vuelvo a la lista anterior que es la lista del vertice L[-2] 
              pos = posicionvertice(grafo,L[-2])
              return existPathR(grafo,grafo[pos],current,grafo[pos].head.nextNode,L,v2)
            else: #si hay mas vertices por verificar paso al siguiente
              return existPathR(grafo,grafo[pos],current,nodeListaNueva.nextNode,L,v2)

def posicionvertice(grafo,elemento):
    pos = 0
    while pos < len(grafo):
        if grafo[pos].head.value == elemento:
            return pos
        pos += 1
#--------------------------------------------------------------------------------------------
#ejercicio 3
#operacion es conexo
#retorna true si hay un camino entre cada para de vertice
def isConnected(grafo): 
    i = 0
    flag = True
    while i < len(grafo):
        v1 = grafo[i].head.value  #voy a ver si hay un camino de v1 a todos los otros vertices
        j = 0
        while j < len(grafo):
            if i != j:
                v2 = grafo[j].head.value #aca voy actualizando los vertices
                if existPath(grafo,v1,v2) == False: #comparo, si no hay camino ya termino
                    #print("no es conexo")
                    flag = False
                    return 
            j += 1
        i += 1
    if flag == False:
       #print("no conexo")
       return False
    else:
       #print("conexo")   
       return True         
    
#--------------------------------------------------------------------------------------------
#ejercicio 4      
#retorna True si el grafo es un árbol        
#es un arbol si: es conexo, no tiene ciclos y no es dirigido 
def isTree(grafo):          
    if isConnected == False:
        return False #si no es conexo y no es arbol
    else:
       #verificar que no tenga ciclos
       #si el grafo tiene exactamente n-1 aristas entonces no tiene ciclos
        if cant_aristas(grafo) == (len(grafo)-1):
            #print("no hay ciclos")
            return True
        else:
           #print("hay ciclo") #si hay ciclos no es arbol
           return False
          

#funcion que me va a contar la cantidad de aristas de un grafo
def cant_aristas(grafo):
    i = 0
    total = 0
    while i < len(grafo):
        total += length(grafo[i])
        i += 1
    total = int((total - len(grafo))/2) #le resto 5 y lo divido en 2 porq cuenta cada vertice inicial,
    #y porq las aristas se cuentan 2 veces
    #print(total)
    return total


#--------------------------------------------------------------------------------------------
#ejercicio 5

#retora true si el grafo es completo
#un grafo es completo si tiene n(n-1)/2 aristas, donde n es la cantidad de vertices

def isComplete(grafo): 
    n = len(grafo)
    #cuento la longitud de cada linkedlist y lo voy acumulando
     #esto es porq en la lista de adyacencia las aristas se colocan dos veces
    if cant_aristas(grafo) == (n*(n-1)/2):
        #print("es completo")
        return True
    else:
        #print("no es completo")
        return False

#otra forma de calcular si un grafo es completo
#ver si hay una arista entre todo par de vertices

def isComplete2(grafo):
    n = len(grafo)
    i = 0
    while i < n:
        if length(grafo[i]) != n:
            #print("no es completo")
            return None
        i += 1
    #print("es completo")
    return True


#--------------------------------------------------------------------------------------------
#Parte 2
#ejercicio 8

#Descripción: Convierte un grafo en un árbol BFS
#Entrada: Grafo con la representación de Lista de Adyacencia, 
#v vértice que representa la raíz del árbol
#Salida: Devuelve una Lista de Adyacencia con la representación BFS del grafo recibido usando v como raíz.


def convertToBFSTree(grafo, v):  
    #para que sea arbol debe ser conexo
    if isConnected(grafo):
        asignarvalores(grafo) #primero asigno todos mis vertices de blanco
        pos = posicionvertice(grafo,v)
        inicial = grafo[pos].head
        Q = LinkedList()
        enqueue(Q,inicial.value)
        convertToBFSTreeR(grafo,Q)

def convertToBFSTreeR(grafo,Q):
    if Q == None: #ya vacie mi lista, porq recorri todo el grafo
       return grafo
    else:
        pos = posicionvertice(grafo,Q.head.value)
        vertice = grafo[pos].head
        current = vertice.nextNode
        dequeue(Q)
        while current != None:
            posAux = posicionvertice(grafo,current.value) #debo actualizar el color de ese vertice
            if grafo[posAux].head.color == "white":
                enqueue(Q,current.value)
                current.color = "grey"
                current.parent = vertice
                current.distance = vertice.distance + 1
            else:
               if grafo[posAux].head.color == "grey":
                    dequeue(Q)
            current = current.nextNode
        grafo[pos].head.value = "black"
        return convertToBFSTreeR(grafo,Q)


def asignarvalores(grafo):
    for i in range(0,len(grafo)):
        current = grafo[i].head
        while current != None:
            current.color = "white"
            current.distance = 0
            current.parent = grafo[i].head  #vertice inicial de esa lista
            current = current.nextNode

#--------------------------------------------------------------------------------------------
#ejercicio 9
def convertToDFSTree(grafo,v):
  L = []
  for i in range(0,len(grafo)):
    grafo[i].head.color = "B"
    grafo[i].head.d = 0
    grafo[i].head.f = 0
    grafo[i].head.parent = None
    L.append(grafo[i].head.value)
  
  time = 0  
  pos = posicionElementoEnArray(grafo,v)
  if pos == None:
    return "el vertice no se encuentra en el grafo"
  else:
    if pos != 0:
      cont = 0
      while cont != pos:
        L.append(cont)
        cont += 1
    while pos <= len(grafo):
      if grafo[pos].head.color == "B":
        return dfsVisit(grafo,grafo[pos].head,time,L)
      pos += 1
      if pos == len(grafo)-1 and L != []:
        pos = L[0]
        L.pop(0)
        return dfsVisit(grafo,grafo[pos].head,time,L)
        
  

def dfsVisit(grafo,vertice,time,L):
  if vertice == None:
    return grafo
  else:
    time += 1
    pos = posicionElementoEnArray(grafo,vertice.value)
    current = grafo[pos].head
    
    current.d = time 
    current.color = "G"
    L.remove(vertice.value)
    current = current.nextNode
    while current:
      posAux = posicionElementoEnArray(grafo,current.value)
      if grafo[posAux].head.color == "B":
        grafo[posAux].head.parent = vertice
        dfsVisit(grafo,grafo[posAux].head,time,L)
      else:
        if grafo[posAux].head.color == "N":
          delete(grafo[pos],current.value)
          delete(grafo[posAux],vertice.value)
      current = current.nextNode
    grafo[pos].head.color = "N"
    time += 1
    grafo[pos].head.f = time
    return grafo

#--------------------------------------------------------------------------------------------
#ejercicio 10
#camino mas corto
# el dfs te permite encontrar el camino mas corto en terminos de aristas
#--------------------------------------------------------------------------------------------

#ejercicio 14
#Descripción: Implementa el algoritmo de PRIM 
#Entrada: Grafo con la representación de Matriz de Adyacencia.
#Salida: retorna el árbol abarcador de costo mínimo 

def PRIM(grafo): 
    U = []
    #tomo cualquier vertice y lo paso a U
    v1,v2 = aristainicial(grafo)
    listaA = PRIMR(grafo,{},U,v1,v2) #lista que va a guardar las aristas de costo minimo
   
    #armo mi matriz de adyacencia adquiriendo la arista corresponiente
    for i in range(0,len(grafo)):
        for j in range(0,len(grafo)):
            grafo[i][j] = listaA.get((i,j),0)
    #print(grafo)
    return grafo 

def PRIMR(grafo,listaA,U,v1,v2):
    if len(U) == len(grafo):
        return listaA
    else:
        #agrego la arista al grafo
        listaA[(v1,v2)] = grafo[v1][v2]
        listaA[(v2,v1)] = grafo[v2][v1] 
        #marco la arista como visitada, para que no la vuelva a tomar
        grafo[v1][v2] = 0
        grafo[v2][v1] = 0 

        #agrego los vertices a mi lista U, que es la lista de vertices visitados
        if v1 not in U:
            U.append(v1)
        if v2 not in U:
            U.append(v2)

        min = float('inf')

        #busco la arista de menor costo
        for vertice in U:
           min,v1,v2 = aristaMin(grafo,vertice,v1,v2,min,U)
        #llamo recursivamente para buscar la siguiente arista de menor costo
        return PRIMR(grafo,listaA,U,v1,v2)
        
def aristaMin(grafo,vertice,v1,v2,min,U):
    for j in range(0,len(grafo)):
        if grafo[vertice][j] > 0 and grafo[vertice][j] <= min and j not in U:
            min = grafo[vertice][j]
            v1 = vertice
            v2 = j
    return min,v1,v2

def aristainicial(grafo):
    min = float('inf') 
    v1 = 0
    v2 = 0
    #tengo que buscar la arista de menor valor en el arbol
    for i in range(0,len(grafo)):
        for j in range(0,len(grafo)):
            if grafo[i][j] > 0 and grafo[i][j] < min :
                min = grafo[i][j]
                v1 = i
                v2 = j
    #print("v1: ",v1)  #me va a devolver uno menos porque arranca desde el cero
    #print("v2: ",v2)  #aca igual
    #print(min)
    return v1,v2
#--------------------------------------------------------------------------------------
#ejercicio 15
#Descripción: Implementa el algoritmo de KRUSKAL 
#Entrada: Grafo con la representación de Matriz de Adyacencia.
#Salida: retorna el árbol abarcador de costo mínimo

def KRUSKAL(grafo):
    #conjuntos disjuntos para cada vertice (linea i)
    sets = {i: {i} for i in range(len(grafo))}

    #primero ordeno en una lista las aristas de menos a mayor por costo
    listaA = []
    for i in range(0,len(grafo)):
       for j in range(0,len(grafo)):
          if grafo[i][j] > 0:
             listaA.append(grafo[i][j])  #primero guardo en una losta todos los valores de las aristas
    listaA.sort() #las ordeno de menor a mayor
    print(listaA)   

    #lista de aristas del arbol de expansion minima
    minAristas = []


def find_sets(sets,vertice):
    for s in sets.value():
      if vertice in s:
         return s
    return None     

      
          

        
 