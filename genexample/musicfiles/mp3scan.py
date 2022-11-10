import os
import fnmatch
import id3reader_p3 as id3reader


# 该程序暂时无法运行也不知道为啥
def find_music(start, extension):
    for path, directories, files in os.walk(start):
        for file in fnmatch.filter(files, '*.{}'.format(extension)):
            absolute_path = os.path.abspath(path)  # create absolute path
            yield os.path.join(absolute_path, file)         # use it in yielded values


my_music_files = find_music('music', 'emp3')

error_list = []
for f in my_music_files:
    try:
        # 此处无法运行，因为是针对mp3（才有tag），emp3只是text，没有tag。
        id3r = id3reader.Reader(f)
        print("Artist: {}, Album: {}, Track: {}, Song: {}".format(
            id3r.get_value('performer'),
            id3r.get_value('album'),
            id3r.get_value('track'),
            id3r.get_value('title')
        ))
    except:  # 一般来讲具体exception要写上，但是这里因为是任何与file相关的exception都要捕捉，故没写。
        error_list.append(f)
    # print(f)

for error_file in error_list:
    print(error_file)