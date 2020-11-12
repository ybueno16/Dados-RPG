import random
import time
from termcolor import colored
import sys


def clear_screen():
    import os
    os.system("clear")


for x in colored("Bem Vindo ao simulador de dados de RPG", "red"):
    sys.stdout.write(x)
    sys.stdout.flush()
    time.sleep(0.04)
print()
print()
print()
for x in colored(
        "Este sistema foi desenvolvido pois não havia nada para fazer",
        "green"):
    sys.stdout.write(x)
    sys.stdout.flush()
    time.sleep(0.04)

clear_screen()

dado = int(
    input(
        "Digite o dado desejado: \n\n1. D20\n2. D12\n3. D8\n4. D6\n5. D4\n\n\n"
    ))

if dado == 1:
    print("Voce Escolheu o D20")
    print((
        "O número que caiu foi ",
        random.randrange(1, 21),
    ))
    escolha = str(input("Gostaria de jogar novamente? [s/n] "))
    clear_screen()
    while True:
        if escolha == "n":
            dado = int(
                input(
                    "Digite o dado desejado: \n\n1. D20\n2. D12\n3. D8\n4. D6\n5. D4\n\n\n"
                ))

        if escolha == "s":
            print("O número que caiu foi ", random.randrange(1, 21))
            escolha = str(input("Gostaria de jogar novamente? [s/n] "))
        clear_screen()

if dado == 2:
    print("Voce Escolheu o D12")
    print("O número que caiu foi ", random.randrange(1, 13))
    escolha = str(input("Gostaria de jogar novamente? [s/n] "))
    clear_screen()
    while True:
        if escolha == "n":
            dado = int(
                input(
                    "Digite o dado desejado: \n\n1. D20\n2. D12\n3. D8\n4. D6\n5. D4\n\n\n"
                ))

        if escolha == "s":
            print("O número que caiu foi ", random.randrange(1, 13))
            escolha = str(input("Gostaria de jogar novamente? [s/n] "))
        clear_screen()

if dado == 3:
    print("Voce Escolheu o D8")
    print("O número que caiu foi ", random.randrange(1, 9))
    escolha = str(input("Gostaria de jogar novamente? [s/n] "))
    clear_screen()
    while True:
        if escolha == "n":
            dado = int(
                input(
                    "Digite o dado desejado: \n\n1. D20\n2. D12\n3. D8\n4. D6\n5. D4\n\n\n"
                ))

        if escolha == "s":
            print("O número que caiu foi ", random.randrange(1, 8))
            escolha = str(input("Gostaria de jogar novamente? [s/n] "))
        clear_screen()

if dado == 4:
    print("Voce Escolheu o D6")
    print("O número que caiu foi ", random.randrange(1, 7))
    escolha = str(input("Gostaria de jogar novamente? [s/n] "))
    clear_screen()
    while True:
        if escolha == "n":
            dado = int(
                input(
                    "Digite o dado desejado: \n\n1. D20\n2. D12\n3. D8\n4. D6\n5. D4\n\n\n"
                ))

        if escolha == "s":
            print("O número que caiu foi ", random.randrange(1, 7))
            escolha = str(input("Gostaria de jogar novamente? [s/n] "))
        clear_screen()

if dado == 4:
    print("Voce Escolheu o D4")
    print("O número que caiu foi ", random.randrange(1, 6))
    escolha = str(input("Gostaria de jogar novamente? [s/n] "))
    clear_screen()
    while True:
        if escolha == "n":
            dado = int(
                input(
                    "Digite o dado desejado: \n\n1. D20\n2. D12\n3. D8\n4. D6\n5. D4\n\n\n"
                ))

        if escolha == "s":
            print("O número que caiu foi ", random.randrange(1, 6))
            escolha = str(input("Gostaria de jogar novamente? [s/n] "))
        clear_screen()
