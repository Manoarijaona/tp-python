import random

mystery_number = random.randint(1, 100)
initial_number = 0
score = 10
while mystery_number != initial_number:
    input_number = int(input("Entrez un nombre entre 1 et 100: "))
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
