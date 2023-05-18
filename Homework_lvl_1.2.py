import random
import datetime

my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]

# Пункт A
random_songs = random.sample(my_favorite_songs, 3)
total_time = sum(song[1] for song in random_songs)
total_time_str = str(datetime.timedelta(minutes=total_time))
print(f"Три песни звучат {total_time_str}")

# Пункт B
my_favorite_songs_dict = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}
random_songs_dict = dict(random.sample(my_favorite_songs_dict.items(), 3))
total_time = sum(random_songs_dict.values())
total_time_str = str(datetime.timedelta(minutes=total_time))
print(f"Три песни звучат {total_time_str}")

# Пункт C
random_songs_list = [[song, round(random.uniform(2, 5), 2)] for song in my_favorite_songs]
random_songs = random.sample(random_songs_list, 3)
total_time = sum(song[1] for song in random_songs)
total_time_str = str(datetime.timedelta(minutes=total_time))
print(f"Три случайные песни звучат {total_time_str}")

# Пункт D
time_str = "4:45" # пример строки с временем в формате минуты:секунды
time_delta = datetime.datetime.strptime(time_str, "%M:%S") - datetime.datetime(1900, 1, 1)
time_in_seconds = time_delta.total_seconds()
print(f"Время в секундах: {time_in_seconds}")
time_in_minutes = time_in_seconds / 60
time_in_minutes_str = str(datetime.timedelta(minutes=time_in_minutes))
print(f"Время в формате ММ:СС: {time_in_minutes_str}")