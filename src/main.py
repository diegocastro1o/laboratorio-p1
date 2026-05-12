from game import ejecutar_juego
from palabras import obtener_palabra
from random import randint

def normalizar(palabra):
    vocales_esp=['á', 'é', 'í', 'ó', 'ú']
    vocales=['a', 'e', 'i', 'o', 'u']
    
    for i in range(len(vocales_esp)):
        if vocales_esp[i] in palabra:
            palabra = palabra.replace(vocales_esp[i], vocales[i])        
    
    return palabra

def obtener_cantidad_ocultas(pista):
    cantidad_ocultas = 0
    
    for letra in pista:
        cantidad_ocultas += 1 if letra == '_' else 0
        
    return cantidad_ocultas

def agregar_caracter(palabra, index, caracter):
    resultado = ''
    
    for i in range(len(palabra)):
        resultado += palabra[i] if i != index else caracter
        
    return resultado

# EJERCICIO 1
def generar_pista(palabra):
    pista = palabra
    
    for i in range(len(palabra)):
        cantidad_ocultas = obtener_cantidad_ocultas(pista)
        rand_bin = randint(0, 1)
        if rand_bin == 1 and cantidad_ocultas <= len(palabra) * 0.6:
            pista = agregar_caracter(pista, i, '_')
    
    return pista

# EJERCICIO 2
def verificar_palabra(palabra, intento):
    es_correcto = normalizar(palabra.lower()) == normalizar(intento.lower())
    
    return es_correcto

# EJERCICIO 3
def calcular_puntaje(tiempo_restante, intentos_restantes):
    puntaje_total=round((tiempo_restante*10)+(intentos_restantes*20), 2)
    
    return puntaje_total

# Ejercicio Adicional
def actualizar_pista(pista, palabra):
    cantidad_ocultas = obtener_cantidad_ocultas(pista)
    pista_actualizada = pista
    
    while pista == pista_actualizada and cantidad_ocultas > 1:
        for i in range(0,len(pista)):
            rand_bin = randint(0, 1)
            if rand_bin == 1 and pista[i] == '_':
                pista_actualizada = agregar_caracter(pista_actualizada, i, palabra[i])
                break

    return  pista_actualizada


# ---------------- MAIN ----------------
palabra = obtener_palabra()

ejecutar_juego(
    palabra,
    generar_pista,
    verificar_palabra,
    actualizar_pista,
    calcular_puntaje
)