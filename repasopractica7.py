def pertenece (n:int, s:[int]) -> bool:
    for numero in s:
        if n == numero:
            return True
    return False
print(pertenece(2,[3,5,5]))
def divide_a_todos(n:int, s :[int]) -> bool:
    valor: bool = True
    for numero in s:
        if (numero%n) != 0:
            valor = False
    return valor

def suma_total(s:[int]) -> int:
    total: int = 0
    for numero in s:
        total += numero
    return total

def ordenados(s:[int]) -> bool:
    valor: bool = True
    i: int = 0
    while i < len(s)-1:
        if s[i] > s[i+1]:
            valor = False
        i += 1 
    return valor

print(ordenados([1,2,3]))
print(ordenados([1,2,1]))

def palindromo(p:str) -> bool:
    i: int = 0
    long: int = len(p) -1
    valor: bool = False
    if (len(p)%2) != 0:
        while i < len(p)/2 -1:
            if p[i] == p[long]:
                valor = True
            else:
                return False
            i += 1
            long -= 1
    else:
        while i < len(p)/2:
            if p[i] == p[long]:
                valor = True
            else:
                return False
            i += 1
            long -= 1
    return valor
print("Palindromo")
print(palindromo("holaaloh"))
print(palindromo("holawaloh"))
print(palindromo("holawealoh"))

def ceros(s:[int]) -> None:
    long = len(s)
    s.clear()
    while long > 0:
        s.append(0)
        long -=1
        

s:list= [1,2,3]
print(s)
ceros(s)
print(s)

def sin_vocales(s: str) -> str:
    vocales: list = ['a','e','i','o','u','A','E','I','O','U']
    palabra_final:str = ""
    for letra in s:
        if letra not in vocales:
            palabra_final += letra
    return palabra_final

print(sin_vocales("hola"))

def reemplaza_vocales(s: str) -> str:
    vocales: list = ['a','e','i','o','u','A','E','I','O','U']
    palabra_final:str = ""
    for letra in s:
        if letra not in vocales:
            palabra_final += letra
        else:
            palabra_final += '_'
    return palabra_final

print(reemplaza_vocales("hola"))

from queue import LifoQueue as Pila

def dar_vuelta_str(s: str) -> str:
    string_final: str = ""
    p: Pila = Pila()
    for letra in s:
        p.put(letra)
    while not p.empty():
        string_final += p.get()
    return string_final

print(dar_vuelta_str("hola"))    

def eliminar_repetidos(s: str) -> str:
    string_final: str = ""
    for letra in s:
        if letra not in string_final:
            string_final += letra
    return string_final

print(eliminar_repetidos("hooolaaalah"))

def calcular_promedio(s:[int]) -> float:
    final: float = 0
    suma: int = 0
    for numero in s:
        suma += numero
    float(suma)
    final = suma/ len(s)
    return final

def todas_mayores_iguales_4(s:[int]) -> bool:
    valor: bool = True
    for numero in s:
        if numero < 4:
            return False
    return valor

def aprobado(s:[int]) -> int:
    promedio: int = calcular_promedio(s)
    if todas_mayores_iguales_4 and promedio >= 7:
        return 1
    elif todas_mayores_iguales_4 and promedio >= 4:
        return 2
    else:
        return 3
    
def pertenece_a_cada_uno(s:list[list[int]],e:int, res:[bool]) -> None:
    res.clear()
    for lista in s:
        if e in lista:
            res.append(True)
        else:
            res.append(False)

s:list =[[1,2,3],[2,3,4],[1,2,5]]
res:list= [True, True, True]
print(res)
pertenece_a_cada_uno(s,1,res)
print(res)

def es_matriz(s:list[list[int]]) -> bool:
    longitud:int = len(s[0])
    for lista in s:
        if len(lista) != longitud:
            return False
    return True

print(es_matriz([[1,2,3],[4,5]]))

def filas_ordenados(s:list[list[int]], b:list[bool]) -> None:
    b.clear()
    for lista in s:
        if ordenados(lista):
            b.append(True)
        else:
            b.append(False)

b= [True,False]
print(b)
filas_ordenados([[1,2,3],[4,5,6]],b)    
print(b)   

def columnas_repetidas(mat:list[list[int]]) -> bool:
    valor:bool = True
    for fila in mat:
        longitud_filas: int = int(len(mat[0])/2)
        inicial: int  = 0
        i:int = int(len(mat[0])/2)
        while i > 0:
            print(fila[inicial]) 
            print(fila[longitud_filas])
            if fila[inicial] != fila[longitud_filas]:
                return False
            longitud_filas += 1
            inicial += 1
            i -= 1
    return valor    

m = [[1,2,1,2],[-5,6,-5,6],[0,1,0,1]]
n = [[1,2,1,2],[-5,6,-5,6],[0,1,0,7]]
print(columnas_repetidas(m))
print(columnas_repetidas(n))


import random
def siete_y_medio() -> list[int]:
    posibles:list = [1,2,3,4,5,6,7,10,11,12]
    carta:int = random.choice(posibles)
    historial:list= []
    historial.append(carta)
    while True:
        decision: str = input()
        if decision == 'seguir':
            historial.append(random.choice(posibles))
        else:
            break
    contador:float = 0
    for numero in historial:
        if numero in [10,11,12]:
            contador += 0.5
        else:
            contador += numero
    if contador > 7.5:
            print("Has perdido")
    return historial
    
print(siete_y_medio())