month = input("Введите номер месяца: ")

if month.isdigit():
    month = int(month)
    if 1 <= month <= 12:
        days = 31
        if month == 4 or month == 6 or month == 9 or month == 11:
            days = 30
        elif month == 2:
            days = 28
        print(f"Вы ввели {month} месяц: {days} дней")
    else:
        print("Такого месяца нет!")
else:
    print("Вы ввели не число!")