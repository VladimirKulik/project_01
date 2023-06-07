import math
def quarter_of(month):
    if month <= 0 and month > 12:
        return None
    return math.ceil(month/3)
month = 2
quarter = quarter_of(month)
print("Месяц", month, "принадлежит кварталу", quarter)  # Месяц 2 принадлежит кварталу 1

month = 6
quarter = quarter_of(month)
print("Месяц", month, "принадлежит кварталу", quarter)  # Месяц 6 принадлежит кварталу 2

month = 11
quarter = quarter_of(month)
print("Месяц", month, "принадлежит кварталу", quarter)  # Месяц 11 принадлежит кварталу 4