def get_number():
    for num in range(30):
        if num % 2 != 0:
            yield num

def main():
    odd_numbers = list(get_number())  # Преобразуем результат генератора в список

    if len(odd_numbers) < 5:
        print("Недостаточно нечетных чисел в диапазоне.")
        return

    print(f"Первое нечетное число: {odd_numbers[0]}")
    print(f"Пятое нечетное число: {odd_numbers[4]}")
    print(f"Последнее нечетное число: {odd_numbers[-1]}")

main()
