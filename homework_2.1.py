def minimum(arr):
    min_num = arr[0]  # Инициализируем переменную min_num первым элементом списка
    for num in arr:
        if num < min_num:
            min_num = num
    return min_num

def maximum(arr):
    max_num = arr[0]  # Инициализируем переменную max_num первым элементом списка
    for num in arr:
        if num > max_num:
            max_num = num
    return max_num

arr = [4,6,2,1,9,63,-134,566]]
min_val = minimum(arr)
max_val = maximum(arr)
print("min =", min_val)  # min = -110
print("max =", max_val)  # max = 56