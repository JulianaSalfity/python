#ej 1
from queue import LifoQueue as Pila

def ultima_aparicion(s: list[int], e: int) -> int:
    pila_numeros: Pila = Pila()
    for numero in s:
        pila_numeros.put(numero)
    longitud = len(s)
    posicion_hacia_atras: int = 0
    while not pila_numeros.empty():
        numero_sacadO : int = pila_numeros.get()
        if numero_sacadO == e:
            posicion_hacia_atras +=1
            return longitud - posicion_hacia_atras
        else:
            posicion_hacia_atras +=1
             
print(ultima_aparicion([-1,4,0,4,100,0,100,0,-1,-1],0))
print(ultima_aparicion([0,1,2,3,4,2,5],2))

#ej 2
def elementos_exclusivos(s:list[int], t:list[int]) -> list[int]:
    lista_final: list = []
    for elemento in s:
        if elemento not in t and elemento not in lista_final:
            lista_final.append(elemento)
    for elemento1 in t:
        if elemento1 not in s and elemento1 not in lista_final:
            lista_final.append(elemento1)
    return lista_final

print(elementos_exclusivos([-1,4,0,4,3,0,100,0,-1,-1],[0,100,5,0,100,-1,5]))
print(elementos_exclusivos([-1,4,0,4,3,0,100,0,-1,-1],[0,100,5,0,100,-1,5,6,7]))

#ej 3
def contar_traducciones_iguales(ing: dict[str, str], ale: dict[str,str]) -> int:
    contador: int = 0
    for clave in ing:
        if clave in ale and ale[clave] == ing[clave]:
            contador += 1
    return contador


aleman = {"Mano": "Hand", "Pie": "Fuss", "Dedo": "Finger", "Cara": "Gesicht", "Hola":"h"}
ingles = {"Pie": "Foot", "Dedo": "Finger", "Mano": "Hand","Hola":"h"}
print(contar_traducciones_iguales(ingles, aleman))

#ej 4
def convertir_a_diccionario(lista: list[int]) -> dict[int,int]:
    diccionario_numeros: dict = {}
    for numero in lista:
        if numero in lista:
            if numero in diccionario_numeros:
                diccionario_numeros[numero] += 1
            else:
                diccionario_numeros[numero] = 1
    return diccionario_numeros

print(convertir_a_diccionario([-1,0,4,100,100,-1,-1]))

