from algo1 import*

def comparar_strings(T,S):
    if len(T) != len(S):
        #print("distinta long")
        return False
    else:
        for i in range(0,len(T)):
            if T[i] != S[i]:
                #print("distintas")
                return False
        #print("iguales")
        return True
    
def extraer_subcadena(S,start,end):
    subcadena = ""
    flag = True
    i = 0
    while flag:
        if i == start:
            for j in range(start,end+1):
                subcadena += S[j]
            flag = False
        i += 1
    print(subcadena)
    return subcadena

#Se tiene una cadena de caracteres y se quiere reducir a su longitud haciendo una serie de operaciones.
#En cada operación se selecciona un par de caracteres adyacentes que coinciden, y se los borra. 
#Por ejemplo, la cadena “aab” puede ser acortada a “b” en una sola operación. 
#Implementar una función que borre tantos caracteres como sea posible 
#devuelva la cadena resultante.

#los corto solo si son iguales y voy avanzano de a 1

def reduceLen(s):
    i = 0
    while i < len(s)-1:
        if s[i] == s[i+1]:
            nueva = s.replace(s[i],"",2)
            s = nueva
            i = -1 #porque empieza a contar desde el principio
        i += 1 #aca arrancaria en 0
    print(s)


#determina si p se encuentra en s en orden
def isContained(s,p):
    j = 0
    cont = 0
    for i in range(0,len(s)):
        if s[i] == p[j]:
            j += 1
        if j == len(p):
            #print("contenida")
            return True
    return False

#Ejercicio 3
#contar y decir cual es el caracter que mas se repite
def mostRepeatedChar(s):
    #creo un diccionario
    frecuencia = {}
    for letra in s:
        if letra in frecuencia:
            frecuencia[letra] += 1
        else:
            frecuencia[letra] = 1
    #ahora debo mostrar el que mas frecuencia tiene
    mayor = max(frecuencia, key=frecuencia.get)
    return mayor

#Ejercico 5
#determinar si una cadena es anarama de otra
#una cadena es anagrama de otra si al cambiar puedo cambiar el orden de una y obtener la otra
def IsAnagram(s,p):
    if len(s) == len(p):
        #todas las letras de p deben coinicir con las de s
        for letra in p:
            if letra not in s:
                print("no es anagrama")
                return False
        print("anagrama")
        return True
    else: return False



#Ejercicio 13    
#RABIN KARP
"""Implemente el algoritmo de Rabin-Karp estudiado. Para el mismo deberá implementarse una función de hash que dado un patrón p de tamaño m 
se resuelva en O(1). Considerar lo detallando en las presentación del tema correspondiente a las funciones de hash en Rabin-karp. """

def RK(p, t, q):
    m = len(p)
    n = len(t)
    d = n #long t
    hp = 0
    ht = 0
    h = 1

    for i in range(m-1):
        h = (h*d) % q

    # calculo hash value de p y t
    for i in range(m):
        hp = (d*hp + ord(p[i])) % q
        ht = (d*ht + ord(t[i])) % q

    #encuentro la subcadena en la cadena
    for i in range(n-m+1):
        if hp == ht:
            for j in range(m):
                if t[i+j] != p[j]: #los hash coinciden pero los caracteres no
                    break

            j += 1
            if j == m: #es porque no rompi el bucle anterior entonces encontre la subcadena
                print(p,"found at ", str(i+1))
                break

        if i < n-m: #si no, no podemos desplazarnos a la proxima subcadena porque no alcanza la long
            ht = (d*(ht-ord(t[i])*h) + ord(t[i+m])) % q #a ht le resto el termino de mayor orden y le sumo el de menor orden
            if ht < 0: #para que el hash no sea negativo
                ht += q
        else: return print("None")


#Ejercicio 12     
#AEF

def mostrarMatriz(matrix):
    filas = len(matrix)
    columnas = len(matrix[0])
    for i in range(0, filas):
        print("|", end="  ")
    for j in range(0, columnas):
        print(matrix[i][j], end="  ")
    print("|")


def construirAutomata(patron,m):

    automata = [[0] * 128 for _ in range(m + 1)] #tabla de estados inicializada en 0
    automata[0][ord(patron[0])] = 1 #paso inicial: primera transición del autómata 
    x = 0 #referencia para las transiciones cuando se encuentra un carácter que no coincide en el patrón
    for estado in range(1, m + 1): #para recorrer el patron en todas sus posiciones
        for c in range(128):
            automata[estado][c] = automata[x][c]
        if estado < m:
            automata[estado][ord(patron[estado])] = estado + 1 
            #Si el autómata se encuentra en el estado 'estado' y se encuentra el carácter patron[estado], se realizará una transición hacia el estado 'estado + 1'.
            x = automata[x][ord(patron[estado])] 
            #Esto garantiza que si se encuentra un carácter que no coincide en el patrón, el autómata regresará al estado anterior más largo coincidente para continuar la búsqueda.

    return automata


def AEF(texto, patron):
    n = len(texto)
    m = len(patron)
    automata = construirAutomata(patron,m)
    estado_actual = 0  #q
    for i in range(n):
        estado_actual = automata[estado_actual][ord(texto[i])]   # q = d(q,T[i])
        if estado_actual == m:
            print("Pattern occurs with shift ", i-len(patron)+1)
            break
    if estado_actual != m: 
        return print("None")


#Ejercicio 14                       
#KMP

def KMP(t,p):
    n = len(t)
    m = len(p)
    pi = computePrefixFunction(p)
    q = 0
    for i in range(0,n):
        while q > 0 and p[q] != t[i]:
            q = pi[q-1]
        if p[q] == t[i]:
            q += 1
        if q == m:
            print("Pattern occurs with shift", i-m+2)
            #q = pi[q]   -----> en caso de que haya q buscar mas de una ocurrencia
            break
    if q != m:
        return print("None")
    else:
        return

def computePrefixFunction(p):
    m = len(p)
    pi = [0]*m
    pi[0] = 0
    k = 0
    for q in range(1,m):
        while k > 0 and p[k] != p[q]:
            k = pi[k]
        if p[k] == p[q]:
            k += 1
        pi[q] = k
    return pi

        