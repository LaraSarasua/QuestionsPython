import random

words = [
    "python",
    "programa",
    "variable",
    "funcion",
    "bucle",
    "cadena",
    "entero",
    "lista",
]


word = random.choice(words)
guessed = []
attempts = 6


print("¡Bienvenido al Ahorcado!")
print()


while attempts > 0:
    # Mostrar progreso: letras adivinadas y guiones para las que faltan
    progress = ""
    for letter in word:
        if letter in guessed:
            progress += letter + " "
        else:
            progress += "_ "
    
    print(progress)
    
    # Verificar si el jugador ya adivinó la palabra completa
    if "_" not in progress:
        print("¡Ganaste!")
        break
    
    print(f"Intentos restantes: {attempts}")
    print(f"Letras usadas: {', '.join(guessed)}")
    
    letter = input("Ingresá una letra: ")

    if len(letter) != 1 or not letter.isalpha(): #la funcion isalpha en python verifica q lo que este dentro de la variable sea si o si una letra del abecedario. 
        print("Entrada incorrecta. Solamente se aceptan letras del abecedario")
        print()
        continue #para que vuelva a "entrar" en el while para que pregunte otra letra ya que la ingresada no fue valida.

    if letter in guessed:
        print("Ya usaste esa letra.")
    elif letter in word:
        guessed.append(letter)
        print("¡Bien! Esa letra está en la palabra.")
    else:
        guessed.append(letter)
        attempts -= 1
        print("Esa letra no está en la palabra.")
    print()
else:
    print(f"¡Perdiste! La palabra era: {word}")