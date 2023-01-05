### Sombrero ###

def sorting_hat():
    """Simulate the sorting hat from Harry Potter"""
    # inicializar los puntajes de cada casa a cero
    gryffindor = 0
    hufflepuff = 0
    ravenclaw = 0
    slytherin = 0

    print("On a scale from 1 to 5, how brave are you?")
    bravery = int(input("Enter a number: "))
    print("On a scale from 1 to 5, how intelligent are you?")
    intelligence = int(input("Enter a number: "))
    print("On a scale from 1 to 5, how kind are you?")
    kindness = int(input("Enter a number: "))
    print("On a scale from 1 to 5, how cunning are you?")
    cunning = int(input("Enter a number: "))

    # asignar puntos a cada casa
    if bravery > 3:
        gryffindor += 1
    if intelligence > 3:
        ravenclaw += 1
    if kindness > 3:
        hufflepuff += 1
    if cunning > 3:
        slytherin += 1

    # determinar la casa con el mayor puntaje
    scores = {
        "Gryffindor": gryffindor,
        "Hufflepuff": hufflepuff,
        "Ravenclaw": ravenclaw,
        "Slytherin": slytherin
    }
    return max(scores, key=scores.get)

name = input("Enter your name: ")
house = sorting_hat()
print(name + " has been sorted into " + house + ".")