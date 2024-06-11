import math
def me_quedo_con_los_ultimos_tres(n:int):
    n_a_str:str = str(n)
    temp:str = ""
    i: int = len(n_a_str)-3
    while i < len(n_a_str):
        temp += n_a_str[i]
        i += 1
    n_final: int = int(temp)
    print(n_final)
    return n_final

print(me_quedo_con_los_ultimos_tres(345542))
print(me_quedo_con_los_ultimos_tres(345002))
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

print(es_primo(9))
print(es_primo(1))
print("primo uno",es_primo(1))
print(es_primo(3))
print(es_primo(101))
print(es_primo(240))
print(es_primo(39))
print(es_primo(57))
print(es_primo(83))
print("prueba primo",es_primo(721))

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

lista_ingresada: list =[101,3003,4045,107,5044,-101,-4040404]
print(lista_ingresada)
print(filtrar_codigos_primos(lista_ingresada))
print(lista_ingresada)

def buscar_maximo(s:list[int]) -> int:
    max: int = 0
    for n in s:
        if n >= max:
            max = n
    return max

print(buscar_maximo([8,2,34,56,6]))

def buscar_minimo(s:list[int]) -> int:
    min: int = s[0]
    for n in s:
        if n <= min:
            min = n
    return min

print(buscar_minimo([8,2,34,56,6]))


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
    print(dict_productos_aux)
    return dict_productos
    

stock_cambios= [("comida",30),("correa",20),("pecera",5),("comida",35),("correa",25),("pecera",1),("comida",3),("correa",2),("pecera",5),("comida",34),("correa",5),("pecera",0)]
print(stock_productos(stock_cambios))

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
    print(columnas_en_filas)
    m:int = 1
    lista_bool: list = []
    while m < len(columnas_en_filas):
        lista_bool.append(chequear(columnas_en_filas[m]))
        m += 1
    print(lista_bool)
    return(lista_bool)


grilla_horaria:list[list[str]] = [[9,'M','C','D','A','A','J','A'],[10,'M','C','D','A','A','J','A'],[11,'M','D','D','J','A','J','A'],[12,'M','D','D','J','A','J','A'],[14,'C','M','M','J','J','C','J'],[15,'C','M','M','J','J','C','J'],[16,'D','M','C','M','J','M','J'],[17,'D','M','C','C','C','C','J']]
                                  
un_responsable_por_turno(grilla_horaria)

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

print(max_tupla([(0, 1), (2, 2), (7, 1), (11, 2)]))
print(max_tupla([(1, 1), (4, 3), (8, 4)]))

def subsecuencia_mas_larga(tipos_pacientes_atendidos:list[str]) -> int:
    tuplas_gatos: list[(int,int)] = cant_seguidos('gato',tipos_pacientes_atendidos)
    print (tuplas_gatos)
    tuplas_perros: list[(int,int)] = cant_seguidos('perro',tipos_pacientes_atendidos)
    print (tuplas_perros)
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
    


animales: list = ['gato','perro','gato','gato','perro','perro','perro','gato','perro','perro','perro','perro','gato','gato']
animales1: list = ['gato','perro','gato','gato','perro','perro','perro','gato','perro','perro','perro','perro','gato','gato','gato','gato']

animales2: list = ['gato','perro','gato','gato','gato','gato','perro','perro','perro','gato','perro','perro','perro','perro','gato','gato','gato','gato']

animales3: list = ['gato','perro','gato','gato','gato','gato','perro','perro','perro','gato','perro','perro','perro','perro','gato','gato','gato','gato','gato']

animales4: list = ['gato','perro','gato','gato','gato','gato','perro','perro','perro','gato','perro','perro','perro','perro','gato','gato','gato','gato','gato','perro','perro','perro','perro','perro','perro']

print(subsecuencia_mas_larga(animales))
print(subsecuencia_mas_larga(animales1))
print(subsecuencia_mas_larga(animales2))
print(subsecuencia_mas_larga(animales3))
print(subsecuencia_mas_larga(animales4))