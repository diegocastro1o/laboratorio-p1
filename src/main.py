from game import ejecutar_juego
from palabras import obtener_palabra

# EJERCICIO 1
import random
def generar_pista(palabra):
    pista = palabra
    for i in range(0, len(pista)):
        p1 = random.randint(0, 1)
        if pista[p1] != "_" and p1==1:
           pista = pista.replace(pista[i], "_", 1)
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
    return puntaje_total

# Ejercicio Adicional
def actualizar_pista(pista: str, palabra):
    # Si me queda una letra por adivinar, no hago nada y devuelvo la misma pista que tenía
    pass


# ---------------- MAIN ----------------
palabra = obtener_palabra()

ejecutar_juego(
    palabra,
    generar_pista,
    verificar_palabra,
    actualizar_pista,
    calcular_puntaje
)