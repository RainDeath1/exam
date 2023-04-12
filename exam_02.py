"""
Задание №2

Используйте процедурное программирование:

Игра: камень, ножницы, бумага.

Алгоритм работы пользователя с терминалом может выглядеть следующим образом:
    - Поприветствуйте игрока и попросите ввести его.
    - Получить случайный компьютерный ввод.
    - Проверьте два друг против друга.
    - Спросите, хочет ли игрок снова сыграть.
"""
import random


def get_player_choice():
    player_choice = input("Введите свой выбор: камень, ножницы или бумага? ")
    return player_choice.lower()


def get_computer_choice():
    choices = ["камень", "ножницы", "бумага"]
    computer_choice = random.choice(choices)
    return computer_choice


def compare(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "Ничья"
    elif player_choice == "камень":
        if computer_choice == "ножницы":
            return "Победил игрок!"
        else:
            return "Победил компьютер!"
    elif player_choice == "ножницы":
        if computer_choice == "бумага":
            return "Победил игрок!"
        else:
            return "Победил компьютер!"
    elif player_choice == "бумага":
        if computer_choice == "камень":
            return "Победил игрок!"
        else:
            return "Победил компьютер!"
    else:
        return "Некорректный выбор"


def play_rock_paper_scissoprs():
    print("Добро пожаловать в игру 'Камень, ножницы, бумага'!")
    while True:
        player_choice = get_player_choice()
        computer_choice = get_computer_choice()
        print("Игрок выбрал:", player_choice)
        print("Компьютер выбрал:", computer_choice)
        result = compare(player_choice, computer_choice)
        print(result)
        play_again = input("Хотите сыграть еще раз? (Да/Нет) ")
        if play_again.lower() != "да":
            break


play_rock_paper_scissoprs()
