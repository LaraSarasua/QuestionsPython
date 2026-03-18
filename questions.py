import random

prog = [
    "python",
    "programa",
    "variable",
    "funcion",
    "bucle",
    "cadena",
    "entero",
    "lista",
]

bandas = [
    "metallica",
    "deftones",
    "paramore",
    "tool",
    "superheaven",
]

paises = [
    "argentina",
    "peru",
    "mexico",
    "brasil",
    "chile",
]

categorias = {
    "programacion" : prog,
    "bandas de musica" : bandas,
    "paises" : paises
}

guessed = []
attempts = 6
score = 0

print("¡Bienvenido al Ahorcado!")
print()

print("Categorias disponibles: ")
for clave in categorias:
    print("-", clave)

print()

categoria_elegida = input("Elegi la categoria con la que queres jugar: ")

word = random.choice(categorias[categoria_elegida])

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
        score += 6
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
        score -= 1
        print("Esa letra no está en la palabra.")
    print()
else:
    print(f"¡Perdiste! La palabra era: {word}")
    score = 0

print(f"Puntaje final: {score}")