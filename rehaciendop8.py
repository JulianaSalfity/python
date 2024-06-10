from queue import LifoQueue as Pila
from queue import Queue as Cola



def buscar_el_maximo(p:Pila[int]) -> int:
    max:int = 0 
    while not p.empty():
        numero:int = p.get()
        if numero > max:
            max = numero
    return max

p:Pila = Pila()
p.put(1)
p.put(9)
p.put(8)
print(p.queue)
print(buscar_el_maximo(p))
print(p.queue)

def listar_s(s:str) -> list:
    temp :str = ""
    lista_final: list = []
    for expresion in s:
        if expresion != ' ':
            temp += expresion
        else:
            lista_final.append(temp)
            temp =""
    lista_final.append(temp)
    return lista_final

print(listar_s("hols como estas"))

def evaluar_expresion(s:str) -> float:
    pila_numeros: Pila = Pila()
    lista_s: list = listar_s(s)
    for expresion in lista_s:
        if expresion not in ['+','-','/','*']:
            pila_numeros.put(expresion)
        elif expresion in ['+','-','/','*']:
            numero1 :float = float(pila_numeros.get())
            numero2: float = float(pila_numeros.get())
            if expresion == '+':
                res:float= numero1 + numero2
                pila_numeros.put(res)
            elif expresion == '-':
                res:float= numero2 - numero1
                pila_numeros.put(res)
            elif expresion == '*':
                res:float= numero1 * numero2
                pila_numeros.put(res)
            elif expresion == '/':
                res:float= numero2 / numero1
                pila_numeros.put(res)
    return pila_numeros.get()
            
expresion = "38 4 + 5 * 2 -"
resultado = evaluar_expresion(expresion)
print(resultado)