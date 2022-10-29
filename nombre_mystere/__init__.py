import random

nombre_mystere = random.randint(1, 20)
nombre_initiale = 0

while nombre_mystere != nombre_initiale:
    nombre_utilisateur = int(input("Entrez un nombre entre 1 et 10: "))
    if nombre_mystere > nombre_utilisateur:
        print(f"Le nombre mystère est supérieur à {nombre_utilisateur}")
        nombre_initiale = nombre_utilisateur

    elif nombre_mystere < nombre_utilisateur:
        print(f"Le nombre mystère est inférieur à {nombre_utilisateur}")
        nombre_initiale = nombre_utilisateur

    else:
        if nombre_mystere == nombre_utilisateur:
            break

print("Bravo, vous avez trouvé le nombre mystère!!")

