
from random import randint

def computer_guess(x):
    baixo = 1
    alto = x 
    feedback = ""
    while feedback != "C":
        if baixo != alto:
            numero = randint(baixo,alto)
        else:
            numero = baixo
        feedback = input(f'O número,{numero}, está muito alto (A) ou muito abaixo (B), ou está correta? (C) ')
        if feedback == "A":
            alto =  numero - 1
        elif feedback == "B": 
            baixo = numero + 1
    print(f"AEEEE! O computador acertou o seu número, {numero}, corretamente! ")

computer_guess(100000000)