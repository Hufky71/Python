###Sombrero HP ###
def sorting_hat():
    Gryffindor = 0
    Ravenclaw = 0
    Hufflepuff = 0
    Slytherin = 0

    print("No hay nada escondido en tu cabeza, que el Sombrero Seleccionador no pueda ver.Así que pruébame y te diré dónde debes estar.")
    Q1 = input("Do you like Dawn or Dusk?\n 1. Dawn \n 2. Dusk\n Your answer? ")
    Q1 = int(Q1)
    Q2 = input("When I am dead I want people to remind me as:\n1. The Good\n2. The Great\n3. The Wise \n4. The Bold\nYour answer: ")
    Q2 = int(Q2)
    Q3 = input("Which kind of instrument most pleases your ear?\n 1.The violin\n 2.The trumper\n 3.The piano\n 4.The drum\n Your answer: ")
    Q3 = int(Q3)
    ## Asignación de puntos##
    if Q1 == 1:
        Gryffindor += 1
        Ravenclaw += 1
    elif Q1 == 2:
        Hufflepuff += 1
        Slytherin += 1
    else:
        Q1 == "Wrong input"


    if Q2 == 1:
        Hufflepuff += 1
    elif Q2 == 2:
        Slytherin += 1
    elif Q2 == 3:
        Ravenclaw += 1
    elif Q2 == 4:
        Gryffindor += 1
    else:
        Q2 == "Wrong input"
    
    if Q3 == 1:
        Slytherin += 1
    elif Q3 == 2:
        Hufflepuff += 1
    elif Q3 == 3:
        Ravenclaw += 1
    elif Q3 == 4:
        Gryffindor += 1
    else:
        Q3 == "Wrong input"


## Conseguir  Max scores diccionario##

    scores = {
        "Gryffindor": Gryffindor,
        "Hufflepuff": Hufflepuff,
        "Ravenclaw": Ravenclaw,
        "Slytherin": Slytherin
}
    return max(scores, key=scores.get)
    
nombre = input("Dime tu nombre: ")
casa = sorting_hat()

print("El Sombrero dice:  " + nombre + " perteneces a " + casa + "!!!")
 