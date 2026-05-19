from game import ejecutar_juego
from palabras import obtener_palabra
from random import randint

# Cambia las vocales con tilde por vocales sin tilde
# para que la comparación no falle por acentos
def normalizar(palabra):
    vocales_esp=['á', 'é', 'í', 'ó', 'ú']
    vocales=['a', 'e', 'i', 'o', 'u']
    
    for i in range(len(vocales_esp)):
        if vocales_esp[i] in palabra:
            palabra = palabra.replace(vocales_esp[i], vocales[i])        
    
    return palabra

# Devuelve la palabra con el caracter en la posicion index reemplazado
def agregar_caracter(palabra, index, caracter):
    resultado = ''
    
    for i in range(len(palabra)):
        resultado += palabra[i] if i != index else caracter
        
    return resultado

# EJERCICIO 1
# Genera una pista ocultando letras al azar con '_'
# Se ocultan letras hasta un maximo del 60% de la palabra
def generar_pista(palabra):
    pista = palabra
    
    for i in range(len(palabra)):
        rand_bin = randint(0, 1)
         # Oculta la letra si el random da 1 y no se supero el limite de ocultamiento
        if rand_bin == 1 and pista.count('_') <= len(palabra) * 0.6:
            pista = agregar_caracter(pista, i, '_')
    
    return pista

# EJERCICIO 2
# Compara la palabra correcta con el intento del jugador
# Normaliza ambas para ignorar mayusculas y tildes
def verificar_palabra(palabra, intento):
    es_correcto = normalizar(palabra.lower()) == normalizar(intento.lower())
    
    return es_correcto

# EJERCICIO 3
# Calcula el puntaje final segun tiempo e intentos restantes
# Formula: tiempo_restante * 10 + intentos_restantes * 20
def calcular_puntaje(tiempo_restante, intentos_restantes):
    puntaje_total=round((tiempo_restante*10)+(intentos_restantes*20), 2)
    
    return puntaje_total

# Ejercicio Adicional
# Revela una letra oculta al azar en la pista cada vez que el jugador falla
# Si la pista ya tiene solo un '_', no se revela mas nada

def actualizar_pista(pista, palabra):
    pista_actualizada = pista
    
    
    # Intenta revelar una letra hasta que la pista cambie
    while pista == pista_actualizada and pista.count('_') > 1:
        for i in range(0,len(pista)):
            rand_bin = randint(0, 1)
            # Intenta revelar una letra hasta que la pista cambie
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