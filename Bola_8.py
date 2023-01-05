### Bola 8 ###

import random

Name = input("Como le dicen? ")
Question = input(f"{Name} cual es tu pregunta para  la bola 8? ")
choice = random.randint(1,9)
ans1 = "Awevo"
ans2 = "Asi sera"
ans3 = "Simon, puede ser"
ans4 = "No hablo tiki taka, pregunta de nuevo"
ans5 = "No estes chingando"
ans6 = "Ahorita no papa, me estresas"
ans7 = "Nel"
ans8 = "No me suena viej@"
ans9 = "Te diría que si pero...No"

if choice == 1:
    answer = ans1
elif choice == 2:
    answer = ans2
elif choice == 3:
    answer = ans3
elif choice == 4:
    answer = ans4
elif choice == 5:
    answer = ans5
elif choice == 6:
    answer = ans6
elif choice == 7:
    answer = ans7
elif choice == 8:
    answer = ans8
else:
    answer = ans9

print("La bola 8 dice: ", answer)