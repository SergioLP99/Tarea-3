from flask import Flask, json, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Bienvenido'

# Funciones de manipulación de datos
def agregar_clave_valor(diccionario, clave, valor):
    diccionario[clave] = valor
    return diccionario

def eliminar_clave_valor(diccionario, clave):
    if clave in diccionario:
        del diccionario[clave]
    return diccionario

def modificar_valor_clave(diccionario, clave, nuevo_valor):
    if clave in diccionario:
        diccionario[clave] = nuevo_valor
        return True
    else:
        return False

def combinar_diccionarios(dic1, dic2):
    return {**dic1, **dic2}

def agregar_elemento_conjunto(conjunto, elemento):
    if elemento not in conjunto:
        conjunto.add(elemento)
        return True
    else:
        return False

def eliminar_elemento_conjunto(conjunto, elemento):
    if elemento in conjunto:
        conjunto.remove(elemento)
        return True
    else:
        return False

def combinar_conjuntos(conjunto1, conjunto2):
    return conjunto1.union(conjunto2)

def diferencia_conjuntos(conjunto1, conjunto2):
    return conjunto1.difference(conjunto2)

def agregar_elemento_tupla(tupla, elemento):
    return tupla + (elemento,)

def eliminar_elemento_tupla(tupla, elemento):
    lista = list(tupla)
    if elemento in lista:
        lista.remove(elemento)
    return tuple(lista)

def concatenar_tuplas(tupla1, tupla2):
    return tupla1 + tupla2

def revertir_tupla(tupla):
    return tupla[::-1]

# Rutas en Flask para manipulación de datos

@app.route("/dict/agregar/<path:diccio>/<clave>/<valor>")
def agregar_a_diccionario(diccio, clave, valor):
    diccionario = json.loads(diccio)
    diccionario = agregar_clave_valor(diccionario, clave, valor)
    return jsonify(diccionario)

@app.route("/dict/eliminar/<path:diccio>/<clave>")
def eliminar_de_diccionario(diccio, clave):
    diccionario = json.loads(diccio)
    diccionario = eliminar_clave_valor(diccionario, clave)
    return jsonify(diccionario)

@app.route("/dict/modificar/<path:diccio>/<clave>/<nuevo_valor>")
def modificar_diccionario(diccio, clave, nuevo_valor):
    diccionario = json.loads(diccio)
    resultado = modificar_valor_clave(diccionario, clave, nuevo_valor)
    return jsonify({"modificado": resultado, "diccionario": diccionario})

@app.route("/dict/combinar/<path:dic1>/<path:dic2>")
def combinar_diccionarios_route(dic1, dic2):
    dic1 = json.loads(dic1)
    dic2 = json.loads(dic2)
    combinado = combinar_diccionarios(dic1, dic2)
    return jsonify(combinado)

@app.route("/set/agregar/<path:conjunto>/<elemento>")
def agregar_a_conjunto(conjunto, elemento):
    conjunto = set(json.loads(conjunto))
    resultado = agregar_elemento_conjunto(conjunto, elemento)
    return jsonify({"agregado": resultado, "conjunto": list(conjunto)})

@app.route("/set/eliminar/<path:conjunto>/<elemento>")
def eliminar_de_conjunto(conjunto, elemento):
    conjunto = set(json.loads(conjunto))
    resultado = eliminar_elemento_conjunto(conjunto, elemento)
    return jsonify({"eliminado": resultado, "conjunto": list(conjunto)})

@app.route("/set/combinar/<path:conjunto1>/<path:conjunto2>")
def combinar_conjuntos_route(conjunto1, conjunto2):
    conjunto1 = set(json.loads(conjunto1))
    conjunto2 = set(json.loads(conjunto2))
    combinado = combinar_conjuntos(conjunto1, conjunto2)
    return jsonify(list(combinado))

@app.route("/set/diferencia/<path:conjunto1>/<path:conjunto2>")
def diferencia_conjuntos_route(conjunto1, conjunto2):
    conjunto1 = set(json.loads(conjunto1))
    conjunto2 = set(json.loads(conjunto2))
    diferencia = diferencia_conjuntos(conjunto1, conjunto2)
    return jsonify(list(diferencia))

@app.route("/tuple/agregar/<path:tupla>/<elemento>")
def agregar_a_tupla(tupla, elemento):
    tupla = tuple(json.loads(tupla))
    nueva_tupla = agregar_elemento_tupla(tupla, elemento)
    return jsonify(nueva_tupla)

@app.route("/tuple/eliminar/<path:tupla>/<elemento>")
def eliminar_de_tupla(tupla, elemento):
    tupla = tuple(json.loads(tupla))
    nueva_tupla = eliminar_elemento_tupla(tupla, elemento)
    return jsonify(nueva_tupla)

@app.route("/tuple/concatenar/<path:tupla1>/<path:tupla2>")
def concatenar_tuplas_route(tupla1, tupla2):
    tupla1 = tuple(json.loads(tupla1))
    tupla2 = tuple(json.loads(tupla2))
    nueva_tupla = concatenar_tuplas(tupla1, tupla2)
    return jsonify(nueva_tupla)

@app.route("/tuple/revertir/<path:tupla>")
def revertir_tupla_route(tupla):
    tupla = tuple(json.loads(tupla))
    nueva_tupla = revertir_tupla(tupla)
    return jsonify(nueva_tupla)

@app.route("/imprimir/diccionario/<path:diccio>")
def imprimir_diccionario(diccio):
    diccionario = json.loads(diccio)
    print(diccionario)
    return jsonify(diccionario)

@app.route("/imprimir/tupla/<path:tupla>")
def imprimir_tupla(tupla):
    tupla = tuple(json.loads(tupla))
    print(tupla)
    return jsonify(tupla)

@app.route("/imprimir/conjunto/<path:conjunto>")
def imprimir_conjunto(conjunto):
    conjunto = set(json.loads(conjunto))
    print(conjunto)
    return jsonify(list(conjunto))

if __name__ == '__main__':
    app.run(debug=True)
