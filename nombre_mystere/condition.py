from nombre_mystere.level import mystery_number
from nombre_mystere.level import max_number


initial_number = 0
score = 10
while mystery_number != initial_number:
    input_number = int(input(f"Donne un nombre entre 1 et {max_number}: "))
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

print("Gg, tu as enfin trouvé le nombre mystère!!")
print(f"Ton score est de {score}\n")

if 0 <= score <= 4:
    print(" -_-  fais mieux la prochaine fois ")
elif 5 <= score <= 8:
    print("^-^ déjà c'est pas mal")
elif 9 <= score <= 10:
    print("0_0 continue comme ça")
