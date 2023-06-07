# Пункт A
def remove_exclamation_marks(s):
    return s.replace("!", "")

# Пункт B
def remove_last_em(s):
    if s.endswith("!"):
        return s[:-1]
    else:
        return s

# Пункт C
def remove_word_with_one_em(s):
    words = s.split()
    filtered_words = [word for word in words if word.count("!") != 1]
    return " ".join(filtered_words)
# Пункт A
s = "Hi! Hello!"
result = remove_exclamation_marks(s)
print(result)  # "Hi Hello"

s = ""
result = remove_exclamation_marks(s)
print(result)  # ""

s = "Oh, no!!!"
result = remove_exclamation_marks(s)
print(result)  # "Oh, no"

# Пункт B
s = "Hi!"
result = remove_last_em(s)
print(result)  # "Hi"

s = "Hi!!!"
result = remove_last_em(s)
print(result)  # "Hi!!"

s = "!Hi"
result = remove_last_em(s)
print(result)  # "!Hi"

# Пункт C
s = "Hi!"
result = remove_word_with_one_em(s)
print(result)  # ""

s = "Hi! Hi!"
result = remove_word_with_one_em(s)
print(result)  # ""

s = "Hi! Hi! Hi!"
result = remove_word_with_one_em(s)
print(result)  # ""

s = "Hi Hi! Hi!"
result = remove_word_with_one_em(s)
print(result)  # "Hi"

s = "Hi! !Hi Hi!"
result = remove_word_with_one_em(s)
print(result)  # ""

s = "Hi! Hi!! Hi!"
result = remove_word_with_one_em(s)
print(result)  # "Hi!!"

s = "Hi! !Hi! Hi!"
result = remove_word_with_one_em(s)
print(result)  # "!Hi!"