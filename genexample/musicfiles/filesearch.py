import os
import fnmatch


def find_albums(root, artist_name):
    for path, directories, files in os.walk(root):
        caps_name = artist_name.upper()
        # fnmatch.filter -> 只会得到list中和artist_name相匹配的name。
        # 还可以模糊查询也！比如Black*，就能模糊查询所有Black开头的。
        # for artist in fnmatch.filter(directories, artist_name):

        # 下面这种情况可以解决大小写的问题。但是对于case-sensitive的linux system还是不行
        # for artist in fnmatch.filter((d.upper() for d in directories), caps_name):

        # 下面就可以也应用在case sensitive的linux系统中了。我的理解是：
        # 只是拿来比较，却不是将directories全部变为大写的
        # 此处依然是返回的原本的文件名称。
        for artist in (d for d in directories if fnmatch.fnmatch(d.upper(), caps_name)):
            subdir = os.path.join(path, artist)
            # print(f"\t\tartist:{artist}")
            for album_path, albums, _ in os.walk(subdir):
                for album in albums:
                    yield os.path.join(album_path, album), album


def find_songs(albums):
    for album in albums:
        # os.listdir ->
        # Return a list containing the names of the files in the directory.
        for song in os.listdir(album[0]):   # we want the path, not the name of the album
            yield song


album_list = find_albums("music", "Black*")
song_list = find_songs(album_list)

# for a in album_list:
#     print(a)

for s in song_list:
    print(s)
