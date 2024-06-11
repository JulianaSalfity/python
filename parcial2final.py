import math
#1
def me_quedo_con_los_ultimos_tres(n:int):
    n_a_str:str = str(n)
    temp:str = ""
    i: int = len(n_a_str)-3
    while i < len(n_a_str):
        temp += n_a_str[i]
        i += 1
    n_final: int = int(temp)
    return n_final

def es_primo(n:int) -> bool:
    if n == 1:
        return False
    raiz_n: int = int(math.sqrt(n))
    while raiz_n > 1:
        if n%raiz_n != 0:
            raiz_n -= 1
        else:
            return False
    return True

def forman_un_primo_los_ultimos_tres(n: int) -> bool:
    parte_importante_del_codigo: int = me_quedo_con_los_ultimos_tres(n)
    if parte_importante_del_codigo < 0:
        parte_importante_del_codigo = parte_importante_del_codigo*-1
    if es_primo(parte_importante_del_codigo):
        return True
    else:
        return False

def filtrar_codigos_primos(codigos_barra:list[int]) -> list[int]:
    lista_final: list = []
    for codigo in codigos_barra:
        if forman_un_primo_los_ultimos_tres(codigo):
            lista_final.append(codigo)
    return lista_final

#2
def buscar_maximo(s:list[int]) -> int:
    max: int = 0
    for n in s:
        if n >= max:
            max = n
    return max

def buscar_minimo(s:list[int]) -> int:
    min: int = s[0]
    for n in s:
        if n <= min:
            min = n
    return min

def stock_productos(stock_cambios:list[(str,int)]) -> dict[str,(int,int)]:
    dict_productos_aux: dict = {}
    dict_productos: dict = {}
    for producto in stock_cambios:
        objeto: str = producto[0]
        cantidad: int = producto[1]
        if not objeto in dict_productos_aux:
            dict_productos_aux[objeto] = []
        dict_productos_aux[objeto].append(cantidad)
    for k,v in dict_productos_aux.items():
        maximo: int= buscar_maximo(v)
        minimo: int = buscar_minimo(v)
        dict_productos[k] = (minimo, maximo)
    return dict_productos
    
#3
def chequear(s:list[str]) -> (bool,bool):
    valor1: bool = True
    valor2 : bool = True
    i: int = 0
    while i < len(s)/2-1:
        p= s[i]
        p2= s[i+1]
        if s[i] != s[i+1]:
            valor1 = False
            break
        i += 1
    j: int = int(len(s)/2)
    while j < len(s)-1:
        p= s[j]
        p2= s[j+1]
        if s[j] != s[j+1]:
            valor2 = False
            break
        j += 1
    tupla: str=(valor1,valor2)
    return tupla

def un_responsable_por_turno(grilla_horaria:list[list[str]]) ->list[(bool,bool)]:
    columnas_en_filas: list[list[str]] = []
    i: int = 0
    while i < len(grilla_horaria):
        lista_aux: list = []
        for fila in grilla_horaria:
            j:int = i
            lista_aux.append(fila[j])
            j += 1
        columnas_en_filas.append(lista_aux)
        i += 1
    m:int = 1
    lista_bool: list = []
    while m < len(columnas_en_filas):
        lista_bool.append(chequear(columnas_en_filas[m]))
        m += 1
    return(lista_bool)

#4
def cant_seguidos(animal: str,tipos_pacientes_atendidos: list[str]) -> list[(int,int)]:
    tuplas_animal: list =[]
    indice:int = -1
    cant_animal: int = 0
    for paciente in tipos_pacientes_atendidos:
        indice += 1
        if paciente == animal:
            cant_animal += 1
        elif paciente != animal and cant_animal > 0:
            tuplas_animal.append((indice-cant_animal, cant_animal))
            cant_animal = 0
    if cant_animal >  0:
        tuplas_animal.append((indice-cant_animal+1, cant_animal))
    return tuplas_animal

def max_tupla(s:list[(int,int)]) -> (int,int):
    max:int = 0
    tupla_mayor:(int, int) = s[0]
    indice_menor:int = s[len(s)-1][0]
    for a,b in s:
        if b > max:
            tupla_mayor = a,b
            max = b      
    return tupla_mayor

def subsecuencia_mas_larga(tipos_pacientes_atendidos:list[str]) -> int:
    tuplas_gatos: list[(int,int)] = cant_seguidos('gato',tipos_pacientes_atendidos)
    tuplas_perros: list[(int,int)] = cant_seguidos('perro',tipos_pacientes_atendidos)
    max_tupla_gatos:(int,int) = max_tupla(tuplas_gatos)
    max_tupla_perros:(int,int) = max_tupla(tuplas_perros)
    if max_tupla_perros[1] == max_tupla_gatos[1]:
        if max_tupla_perros[0] < max_tupla_gatos[0]:
            return max_tupla_perros[0]
        else:
            return max_tupla_gatos[0]
    if max_tupla_perros[1] < max_tupla_gatos[1]:
        return max_tupla_gatos[0]
    else:
        return max_tupla_perros[0]
    
