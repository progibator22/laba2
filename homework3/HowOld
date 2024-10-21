from datetime import datetime

def calculate_age():
    while True:
        birth_date_str = input("Введите вашу дату рождения в формате день/месяц/год: ")
        
        try:
            birth_date = datetime.strptime(birth_date_str, "%d/%m/%Y")
            today = datetime.today()
            
            if birth_date > today:
                print("Дата рождения не может быть в будущем. Попробуйте еще раз.")
                continue
            
            break
        except ValueError:
            print("Неправильный формат даты. Убедитесь, что дата введена в формате день/месяц/год и существует.")

    age = today.year - birth_date.year
    
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1
    
    return age

user_age = calculate_age()
print(f"Ваш возраст: {user_age}")
