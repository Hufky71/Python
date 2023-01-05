guess = 0
tries = 0
limit = 1

while guess != 6 and tries < limit:
  guess = int(input("Guess the number:  "))
  tries += 1

print("You got it in", tries, "tries!") if guess == 6 else print("You ran out of tries!")