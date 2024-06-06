#ej 1
from queue import LifoQueue as Pila

def acomodar(s: list[str]) -> list[str]:
    lista_UP: list = []
    lista_LLA: list = []
    pila_final:Pila = Pila()
    lista_final: list =[]
    for lista in s:
        if lista == "UP":
            lista_UP.append(lista)
        else:
            lista_LLA.append(lista)
    for cantidad in lista_LLA:
        pila_final.put(cantidad)
    for cantidad1 in lista_UP:
        pila_final.put(cantidad1)
    while not pila_final.empty():
        lista_final.append(pila_final.get())
    return lista_final

print(acomodar(["LLA", "UP", "LLA", "LLA", "UP"]))
    
#ej 2
def pos_umbral(s:list[int], u: int) -> int:
    suma_positivos: int = 0
    posicion:int = 0
    for numero in s:
        if numero > 0 :
            suma_positivos += numero
        if suma_positivos > u:
            return posicion
        posicion += 1
    return -1

print(pos_umbral([1,-2,0,5,-7,3], 8))
print(pos_umbral([1,-2,0,5,-7,3], 5))
print(pos_umbral([1,-2,0,5,-7,3], 20))

#ej 3
#def columnas_repetidas(mat:list[list[int]]) -> bool:
 
#ej 4
def cuenta_posiciones_por_nacion(naciones: list[str], torneos:dict[int, list[str]]) -> dict:
       diccionario_final: dict ={}
       for nacion in naciones:
           diccionario_final[nacion] =[0,0,0,0]
       lista_resultados: list= []
       for k,v in torneos.items():
           lista_resultados.append(v)
       for clave in diccionario_final:
           for pais in lista_resultados:
                if clave == pais[0]:
                    diccionario_final[clave][0] += 1
                if clave == pais[1]:
                    diccionario_final[clave][1] += 1
                if clave == pais[2]:
                    diccionario_final[clave][2] += 1
                if clave == pais[3]:
                    diccionario_final[clave][3] += 1
       return diccionario_final
           

naciones= ["arg", "aus", "nz", "sud"]
torneos= {2023:["nz", "sud", "arg", "aus"], 2022:["nz", "sud", "aus", "arg"]}
print(cuenta_posiciones_por_nacion(naciones, torneos))
    
    
               