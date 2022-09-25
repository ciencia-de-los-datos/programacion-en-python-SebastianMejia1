"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""


from ast import IsNot
from asyncore import read



def pregunta_01():

    import csv
    with open("data.csv", "r") as file:
        Datos = file.readlines()
    Datos=[line.replace("\n","")for line in Datos]
    Datos=[line.split("\t")for line in Datos]

    suma=0
    for i in range(len(Datos)):
        suma += int(Datos[i][1])

    return suma

    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    


def pregunta_02():

    cantidad = {}
    letras = []

    for z in Datos:
        if z[0] not in cantidad:
            cantidad[z[0]]= 1
        else:
             cantidad[z[0]]= cantidad[z[0]]+1
    
    letras = list(cantidad.items())
    letras.sort()
    return letras


    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    


def pregunta_03():

    cantidadd = {}
    letrass = []

    for z in Datos:
        if z[0] not in cantidadd:
            cantidadd[z[0]]= int(z[1])
        else:
             cantidadd[z[0]]= cantidadd[z[0]]+ int(z[1])
    
    letrass = list(cantidadd.items())
    letrass.sort()
    return letrass

    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    
    


def pregunta_04():

    listaa =[z[2].replace("-",",") for z in Datos]
    listaa = [z.split(",") for z in listaa]

    dic_mes = {}
    listr =[]

    for z in listaa:
        if z[1] not in dic_mes:
            dic_mes[z[1]]=1
        else:
            dic_mes[z[1]]= dic_mes[z[1]]+1

    listr= list(dic_mes.items())
    listr.sort()
    return listr

    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    

    


def pregunta_05():

    Datos5= open("data.csv", "r").readlines()
    Datos5 = [z.replace("\n", "") for z in Datos5]
    Datos5 = [z.split("\t") for z in Datos5]
    Datos5 = [z[:2] for z in Datos5]
    
    Dic5={}
    for letra,valor in Datos5:
        valor=int(valor)
        if letra in Dic5.keys():
            Dic5[letra].append(valor)
        else:
            Dic5[letra]=[valor]
    Dic5=[(key,max(valor),min(valor)) for key, valor in Dic5.items()]
    Dic5.sort()
    print(Dic5)
    return Dic5
    
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    
    
   



def pregunta_06():
    file = open("data.csv")
    data = file.readlines()
    max = {

    }
    min = {

    }
    for i in data:
        fila = i.replace("\t", " ").split()
        diccionarios=fila[4].split(",")
        for j in diccionarios:
            clave ,numero = j.split(":")
            if clave in min:
                if min[clave] > int(numero):
                    min[clave] = int(numero)
                elif max[clave] < int(numero):
                    max[clave] = int(numero)
            else:
                min[clave] = int(numero)
                max[clave] = int(numero)

    lista=list(zip(min.keys(),min.values(),max.values()))
    lista.sort()
    return lista

    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """

   


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    return



def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    return


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
   



def pregunta_10():
    with open("data.csv","r") as file:
        Datos10=file.readlines()
    Datos10=[row.replace("\n","") for row in Datos10]
    Datos10=[row.split("\t") for row in Datos10]
    
    rta=[]
    for i in Datos10:
        letra=i[0]
        valor1=i[3].split(",")
        valor2=i[4].split(",")
        tupla=(letra,len(valor1),len(valor2))
    rta.append(tupla)
    print(rta)
    return rta


    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    


def pregunta_11():

    with open("data.csv","r") as file: 
        Datos11 = file.readlines() 
    Datos11 = [f.replace("\n","") for f in Datos11]
    Datos11 = [row.split("\t") for row in Datos11]

    D11 = [row[3] for row in Datos11]
    D11 = [x.split(',') for x in D11]
    lista11 = sorted(set([x[y] for x in D11 for y in range(len(x))]))

    dic11 = dict()

    for x in lista11:
        for y in Datos11:
            if x in y[3] and x not in dic11.keys():
                dic11[x] = int(y[1])
            elif x in y[3]:
                dic11[x] +=int(y[1])   
    
    return dic11

    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    
    


def pregunta_12():

    dict12 = {

    }
    let = sorted(set([z[0] for z in Datos11]))
        
    for x in let:
            for y in Datos11:
                if x == y [0] and x not in dict12.keys():
                    dict12[x] = sum([ int(i[4:]) for i in y[4].split(',')])
                elif  x == y [0]:
                    dict12[x] += sum([int(i[4:]) for i in y[4].split(',')])  
    return dict12

    """
        Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
        los valores de la columna 5 sobre todo el archivo.

        Rta/
        {
            'A': 177,
            'B': 187,
            'C': 114,
            'D': 136,
            'E': 324
        }

        """ 