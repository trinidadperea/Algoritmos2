from algo1 import *
from linkedlist import *
from oavanzado import *
#ordenamienot O(n2)
def contieneSum(A,n):
    terminar = False
    encontro = False
    num = A.head
    while terminar == False and num.nextNode != None:
        valorBusc = n - num.value
        num2 = num.nextNode
        while encontro == False:
            if num2.value == valorBusc:
                encontro = True
                terminar = True
                print("true")
                return True
            else: 
                num2 = num2.nextNode
                if num2 == None:
                    break
        num = num.nextNode

#ordenamiento O(nlgn)
#recibo ua lista de enteros
#devuelvo true si existe un par de elementos que sumados den n

#estategia: pongo 2 punteros, i al iniio del arreglo, y j al final
#los sumo si dan n devuelvo true, sino, si la suma es mayor a n, aumento i, si s menos aumento j


            
                


