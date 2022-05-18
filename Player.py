from random import randint

def perguntaNumero(x):
    random_number = randint(1,x)
    pergunta = 0
    while pergunta != random_number:
        pergunta = int(input(f"Adivinhe o número de 0 a {x} "))
        if pergunta < random_number:
            print("O número digitado está muito abaixo")
        if pergunta > random_number:
            print("O número digitado está muito acima")
    print("Parabeeeens, você acertou o número!!! :)")

perguntaNumero(100)