import random

options = ["камък", "ножица", "хартия"]

player_score = 0
computer_score = 0

print("Играта започна! Първи до 3 победи.")

while player_score < 3 and computer_score < 3:
    player = input("Изберете между (камък/ножица/хартия): ").lower()

    if player not in options:
        print("Грешка! Моля, въведете правилен избор.")
        continue  

    computer = random.choice(options)
    print("Компютърът избра:", computer)

    if player == computer:
        print("Равенство!")
    elif (player == "камък" and computer == "ножица") or \
         (player == "ножица" and computer == "хартия") or \
         (player == "хартия" and computer == "камък"):
        print("Ти печелиш този рунд!")
        player_score += 1
    else:
        print("Компютърът печели този рунд!")
        computer_score += 1

    print(f"Точки: Ти {player_score} – Компютър {computer_score}\n")

if player_score == 3:
    print("Поздравления! Ти спечели играта!")
else:
    print("Компютърът спечели. Успех следващия път!")





