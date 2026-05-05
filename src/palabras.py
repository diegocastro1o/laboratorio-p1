import requests
import random

PALABRAS_FALLBACK = [
    "python",
    "computadora",
    "teclado",
    "pantalla",
    "programacion",
    "variable",
    "funcion",
    "bucle",
    "condicion",
    "archivo",
    "servidor",
    "cliente",
    "red",
    "datos",
    "algoritmo",
    "memoria",
    "proceso",
    "sistema",
    "software",
    "hardware"
]


def obtener_palabra():
    try:
        response = requests.get("https://random-word-api.herokuapp.com/word?lang=es", timeout=5)
        return response.json()[0].lower()
    except:
        return PALABRAS_FALLBACK[random.randint(0, len(PALABRAS_FALLBACK) - 1)]
