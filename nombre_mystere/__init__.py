import random
name = input("Donne ton pseudo de gamer: ")
print(f"Salut {name}, tu es plutôt un:\n")
print("1- Noob")
print("2- Petit joueur")
print("3- Pro gamer")
level = int(input())

if level == 1:
    mystery_number = random.randint(1, 20)
    max_number = 20
elif level == 2:
    mystery_number = random.randint(1, 100)
    max_number = 100
elif level == 3:
    mystery_number = random.randint(1, 1000)
    max_number = 1000

initial_number = 0
score = 10
while mystery_number != initial_number:
    input_number = int(input(f"Entrez un nombre entre 1 et {max_number}: "))
    if mystery_number > input_number:
        print(f"Le nombre mystère est supérieur à {input_number}")
        initial_number = input_number
        score -= 1
    elif mystery_number < input_number:
        print(f"Le nombre mystère est inférieur à {input_number}")
        initial_number = input_number
        score -= 1
    else:
        if mystery_number == input_number:
            break

print("Bravo, vous avez trouvé le nombre mystère!!")
print(f"Votre score est de {score}")
