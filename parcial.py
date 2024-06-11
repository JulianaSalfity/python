from queue import Queue as Cola

def cola_priorizando_vips(filaClientes: Cola[(str,str)]) -> Cola[str]:
    cola_vips:Cola = Cola()
    cola_comun:Cola = Cola()
    while not filaClientes.empty():
        tupla= filaClientes.get()
        if tupla[1] == 'vip':
            cola_vips.put(tupla[0])
        else:
            cola_comun.put(tupla[0])
    cola_final:Cola = Cola()
    while not cola_vips.empty():
        vip:str = cola_vips.get()
        cola_final.put(vip)
    while not cola_comun.empty():
        comun:str =cola_comun.get()
        cola_final.put(comun)
    return cola_final

filaClientes: Cola = Cola()
filaClientes.put(('Sara','vip'))
filaClientes.put(('Juan','vip'))
filaClientes.put(('Pedro','comun'))
filaClientes.put(('Jose','vip'))
filaClientes.put(('Marta','comun'))
print(filaClientes.queue)
print(cola_priorizando_vips(filaClientes).queue)

def torneo_de_gallinas(estrategias: dict[str,str]) -> dict[str,int]:
    lista_tuplas: list[(str,str)] = estrategias.items()
    puntajes: dict[str,int]= {}
    for k in estrategias:
        puntajes[k] = 0
        for tupla in lista_tuplas:
            if estrategias[k] == 'me desvio siempre':
                if k != tupla[0]:
                    if tupla[1] == 'me desvio siempre':
                        puntajes[k] -= 10
                    else:
                        puntajes[k] -= 15
            else:
                if k != tupla[0]:
                    if tupla[1] == 'me desvio siempre':
                        puntajes[k] += 10
                    else:
                        puntajes[k] -= 5
    return puntajes

estrategias = {'Pedro': 'me desvio siempre','Juan': 'me la banco y no me desvio', 'Jose': 'me desvio siempre', 'Agus': 'me desvio siempre', 'Ana': 'me desvio siempre', 'Juana': 'me la banco y no me desvio'}

print(torneo_de_gallinas(estrategias))

def hay_tres_consecutivas(s:str, lista_de_listas: list) -> bool:
    valor: bool = False
    for lista in lista_de_listas:
        i : int = 0
        while i < len(lista)-2:
            if lista[i] == s and lista[i+1] == s and lista[i+2] ==s:
                return True
            else:
                i += 1
    return valor
 


def quien_gano_el_tateti_facilito(tablero:list[list[int]]) -> int:
    tablero_columnas: list = []
    lista: list = []
    i: int = 0
    j: int = 0
    while i < len(tablero):
        for jugada in tablero:
            lista.append(jugada[j])
        tablero_columnas.append(lista)
        lista = []
        j += 1
        i += 1
    print (tablero_columnas)
    if hay_tres_consecutivas('O',tablero_columnas) and hay_tres_consecutivas('X',tablero_columnas):
        return 3
    elif hay_tres_consecutivas('X',tablero_columnas):
        return 1
    elif hay_tres_consecutivas('O',tablero_columnas):
        return 2
    else: 
        return 0

tablero:list = [['X','O','X','O','X'], ['X','X','X','O','O'], ['O','X','X','O','X'], ['O','O','O','O','O'], ['X','X','X','X','X']]

print(quien_gano_el_tateti_facilito(tablero))

def sacar_primero(s:str) -> str:
    temp: str = ""
    i:int = 1
    while i < len(s):
        temp += s[i]
        i += 1
    return temp

print(sacar_primero("hola"))

def es_palindromo(s:str) -> bool:
    valor: bool = True
    longitud: int = len(s)
    if longitud == 1:
        return True
    elif (longitud%2) != 0:
        l: int = len(s)-1
        i : int = 0
        while i < longitud/2 +1:
            if s[i] != s[l]:
                return False
            i += 1
            l -= 1
    else:
        l: int = len(s)-1
        i : int = 0
        while i < longitud/2:
            if s[i] != s[l]:
                return False
            i += 1
            l -= 1
    return valor

print(es_palindromo("holaaloh"))
print(es_palindromo("holaasaloh"))
print(es_palindromo("holafaloh"))

def cuantos_sufijos_son_palindromo(texto: str) -> int:
    lista_sufijo: list = []
    i:int= len(texto)
    while i > 0:
        lista_sufijo.append(texto)
        texto = sacar_primero(texto)
        i -= 1
    print(lista_sufijo)
    contador: int = 0
    for sufijo in lista_sufijo:
        if es_palindromo(sufijo):
            contador += 1
    return contador

print(cuantos_sufijos_son_palindromo("holaala"))
print(cuantos_sufijos_son_palindromo("Diego"))
print(cuantos_sufijos_son_palindromo("juanajuj"))
