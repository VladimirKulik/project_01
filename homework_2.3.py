def switch_it_up(number):
    if number < 0 or number > 9:
        return None
    words = {
        0: 'Zero',
        1: 'One',
        2: 'Two',
        3: 'Three',
        4: 'Four',
        5: 'Five',
        6: 'Six',
        7: 'Seven',
        8: 'Eight',
        9: 'Nine'
    }
    return words[number]
number = 1
word = switch_it_up(number)
print("Цифра", number, "на английском:", word)  # Цифра 1 на английском: One

number = 3
word = switch_it_up(number)
print("Цифра", number, "на английском:", word)  # Цифра 3 на английском: Three

number = 10000
word = switch_it_up(number)
print("Цифра", number, "на английском:", word)  # Цифра 10000 на английском: None