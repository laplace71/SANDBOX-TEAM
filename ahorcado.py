import random
import os

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_ahorcado(intentos):
    etapas = [  # estado final: cabeza, torso, ambos brazos, y ambas piernas (0 intentos)
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # cabeza, torso, ambos brazos, y una pierna (1 intento)
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # cabeza, torso, y ambos brazos (2 intentos)
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # cabeza, torso, y un brazo (3 intentos)
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # cabeza y torso (4 intentos)
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # cabeza (5 intentos)
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # estado inicial (6 intentos)
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return etapas[intentos]

def jugar():
    palabras = ['python', 'programacion', 'computadora', 'teclado', 'desarrollo', 'software', 'algoritmo', 'tecsup', 'variable', 'sintaxis']
    palabra = random.choice(palabras).upper()
    letras_por_adivinar = set(palabra)
    letras_adivinadas = set()
    intentos = 6

    limpiar_pantalla()
    print("¡Bienvenido al juego del AHORCADO!")
    
    while len(letras_por_adivinar) > 0 and intentos > 0:
        print(mostrar_ahorcado(intentos))
        
        # Mostrar el estado actual de la palabra
        palabra_lista = [letra if letra in letras_adivinadas else '_' for letra in palabra]
        print("Palabra: ", " ".join(palabra_lista))
        
        # Mostrar letras ya usadas
        if letras_adivinadas:
            print("Letras intentadas:", " ".join(sorted(letras_adivinadas)))
        
        print(f"Intentos restantes: {intentos}")
        
        # Obtener entrada del usuario
        adivinanza = input("Adivina una letra: ").upper()
        
        limpiar_pantalla() # Limpiamos para mantener la consola ordenada
        
        if len(adivinanza) != 1 or not adivinanza.isalpha():
            print("Por favor, ingresa solo una letra válida.")
            continue
            
        if adivinanza in letras_adivinadas:
            print(f"Ya adivinaste la letra '{adivinanza}'. Intenta con otra.")
        elif adivinanza in letras_por_adivinar:
            print(f"¡Bien hecho! La letra '{adivinanza}' está en la palabra.")
            letras_adivinadas.add(adivinanza)
            letras_por_adivinar.remove(adivinanza)
        else:
            print(f"La letra '{adivinanza}' no está en la palabra.")
            letras_adivinadas.add(adivinanza)
            intentos -= 1
            
    # Resultado final
    if intentos == 0:
        print(mostrar_ahorcado(intentos))
        print(f"¡Has perdido! La palabra era: {palabra}")
    else:
        print(mostrar_ahorcado(intentos))
        print(f"¡Felicidades! Adivinaste la palabra: {palabra} :D")

if __name__ == "__main__":
    jugar()
