from game import ejecutar_juego
from palabras import obtener_palabra
from random import randint

# EJERCICIO 1
def generar_pista(palabra):
    pista = palabra
    for i in range(0, len(pista)):
        p1 = randint(0, 1)
        if p1==1:
           pista = pista.replace(pista[i], "_")
    return pista

# EJERCICIO 2
def verificar_palabra(palabra, intento):
    palabra1=intento.lower()
    if palabra1==palabra.lower():
        return True
    else:
        return False
    
    pass

# EJERCICIO 3
def calcular_puntaje(tiempo_restante, intentos_restantes):
    puntaje_total=(tiempo_restante*10)+(intentos_restantes*20)
    return int(puntaje_total)

# Ejercicio Adicional
def actualizar_pista(pista: str, palabra):
    cantidad_ocultas = 0

    for letra in pista:
        cantidad_ocultas += 1 if letra == '_' else 0

    for i in range(0,len(pista)):
        rand_bin = randint(0, 1)
        agregada = False
        condition = cantidad_ocultas > 1 and rand_bin == 1 and pista[i] == '_' and not agregada
        if condition:
            pista.replace(pista[i], palabra[i])

    return pista


# ---------------- MAIN ----------------
palabra = obtener_palabra()

ejecutar_juego(
    palabra,
    generar_pista,
    verificar_palabra,
    actualizar_pista,
    calcular_puntaje
)