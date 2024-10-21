import random

def find_multiples():
    while True:
        try:
            x = int(input("Введите число X для поиска кратных чисел: "))
            if x <= 0:
                print("Число X должно быть больше нуля. Попробуйте снова.")
                continue
            break
        except ValueError:
            print("Пожалуйста, введите целое число.")

    random_list = [random.randint(0, 200) for _ in range(10)]
    multiples = list(filter(lambda num: num % x == 0, random_list))

    print(f"Сгенерированные числа: {random_list}")
    print(f"Числа, кратные {x}: {multiples}")

find_multiples()
