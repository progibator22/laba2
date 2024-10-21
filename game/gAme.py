import random

def get_user_choice():
    choices = ['камень', 'ножницы', 'бумага']
    
    while True:
        user_input = input("Выберите: камень, ножницы или бумага: ").lower()
        if user_input in choices:
            return user_input
        else:
            print("Некорректный ввод. Пожалуйста, выберите камень, ножницы или бумага.")

def get_computer_choice():
    choices = ['камень', 'ножницы', 'бумага']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Ничья!"
    elif (user_choice == 'камень' and computer_choice == 'ножницы') or \
         (user_choice == 'ножницы' and computer_choice == 'бумага') or \
         (user_choice == 'бумага' and computer_choice == 'камень'):
        return "Вы выиграли!"
    else:
        return "Компьютер выиграл!"

def play_game():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    print(f"Вы выбрали: {user_choice}")
    print(f"Компьютер выбрал: {computer_choice}")

    result = determine_winner(user_choice, computer_choice)
    print(result)

# Запуск игры
play_game()
