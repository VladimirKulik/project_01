my_favorite_songs = 'Waste a Moment, Staying\' Alive, A Sorta Fairytale, Start Me Up, New Salvation'

# Первый трек
first_song = my_favorite_songs[:my_favorite_songs.index(',')]
print(first_song)

# Последний трек
last_song = my_favorite_songs[my_favorite_songs.rindex(',') + 2:]
print(last_song)

# Второй трек
second_song = my_favorite_songs[my_favorite_songs.index(',') + 2:]
second_song = second_song[:second_song.index(',')]
print(second_song)

# Второй трек с конца
second_last_song = my_favorite_songs[:my_favorite_songs.rindex(',')]
second_last_song = second_last_song[second_last_song.rindex(',') + 2:]
print(second_last_song)