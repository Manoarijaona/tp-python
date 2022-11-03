import random

user_name = input("Donne ton pseudo de gamer: ")
print("")
print(f"Salut {user_name}, tu es plutôt un:\n")
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