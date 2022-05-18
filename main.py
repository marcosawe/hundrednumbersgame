from random import randint

def guessNumber(x):
    random_number = randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Adivinhe o número de 0 a {x} "))
        if guess < random_number:
            print("O número digitado está muito abaixo")
        if guess > random_number:
            print("O número digitado está muito acima")
    print("Parabeeeens, você acertou o número!!! :)")

guessNumber(100)