from nested_data import albums

# constant在python中是大写表示，写好了就不要改了，虽然可以改。
SONGS_LIST_INDEX = 3
SONG_TITLE_INDEX = 1
while True:
    print("Please choose your album (invalid choice exists):")
    for index, (title, artist, year, songs) in enumerate(albums):
        print("{}: {}"
              .format(index + 1, title))
    # for index, value in enumerate(albums):
    #     title, artist, year, songs = value
    #     print(index, title, artist, year, songs)
    choice = int(input())
    if 1 <= choice <= len(albums):
        songs_list = albums[choice - 1][SONGS_LIST_INDEX]
    else:
        break

    print("Please choose your song:")
    for index, (track_number, song) in enumerate(songs_list):
        print("{}: {}".format(index + 1, song))

    song_choice = int(input())
    if 1 <= song_choice <= len(songs_list):
        title = songs_list[song_choice - 1][SONG_TITLE_INDEX]
        print("Playing '{}'".format(title))  # 复习：cmd+shift+up向上移动

    print("=" * 40)
