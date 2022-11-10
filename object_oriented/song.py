class Song:
    """class to represent a song

    Attributes:
        title (str): The title of the song
        artist (str): The name of the song's creator
        duration (int): The duration of the song in seconds. May be zero.
    """

    def __init__(self, title, artist, duration=0):
        """ Song init method

        Args:
            name (str): Initialises the `title` attribute
            artist (Artist): An Artist object representing the `duration` attribute.
            duration (Optional[int]): Initial value for the `duration` attribute.
                will default to zero if not specified.
        """
        self.title = title
        self.artist = artist
        self.duration = duration

    def get_title(self):
        return self.title

    name = property(get_title)


class Album:
    """ Class to represent an Album, using its track list

    Attributes:
        name(str): The name of the album.
        year (int): The year the album was released.
        artist (str): The name of the artist responsible for the album. If not specified,
            the artist will default to an artist with the name `Various Artist`
        tracks (List[Song]): A list of the songs on the album.

    Methods:
        addSongs: Used to add a new song to the album's track list.
    """

    def __init__(self, name, year, artist=None):
        self.name = name
        self.year = year
        if artist is None:
            self.artist = "Various artist"
        else:
            self.artist = artist

        self.tracks = []

    def add_song(self, song, position=None):
        """ Adds a song to the track list

        :param song: The title of a song to add.
        :param position: (Optional[int]) If specified, the song will be added to that position
            in the track list - inserting it between other songs if necessary.
            Otherwise, the song will be added to the end of the list.
        :return:
        """
        song_found = find_object(song, self.tracks)
        if song_found is None:
            song_found = Song(song, self.artist)
            if position is None:
                self.tracks.append(song_found)
            else:
                self.tracks.insert(position, song_found)


class Artist:
    """Basic class to store artist details.

    Attributes:
        name (str): The name of the artist.
        albums (List[Album]): A list of the albums by this artist.
            The list includes only those albums in this collection,
            it is not an exhaustive list of the artist's published albums.

    Methods:
        add_album: Used to add a new album to the artist's albums list.
    """

    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album):
        """Add a new album to the list.

        Args:
            album (Album): Album object to add to the list.
                If the album is already present, it will not be added again (although this is yet to be implemented)
        """
        self.albums.append(album)

    def add_song(self, name, year, title):
        """Add a new song to the collection of albums

        This method will add the song to an album in the collection.
        A new album will be created in the collection if it doesn't exist.

        Args:
            name (str): The name of the album
            year (int): The year the album was released
            title (str): The title of the song
        """
        album_found = find_object(name, self.albums)
        if album_found is None:
            print(name + " not found")
            album_found = Album(name, year, self.name)
            self.add_album(album_found)
        else:
            print("Found album " + name)

        album_found.add_song(title)


def find_object(field, object_list):
    """Check `object_list` to see if an object with a `name` attribute equal to `field` exists, return it if so"""
    for item in object_list:
        if item.name == field:
            return item
    return None


def load_data():
    # new_artist = None
    # new_album = None
    artist_list = []

    with open("albums.txt", "r") as albums:
        for line in albums:
            # data row should consist of (artist, album, year, song)
            artist_field, album_field, year_field, song_field = tuple(line.strip("\n").split("\t"))
            year_field = int(year_field)
            print("{}:{}:{}:{}".format(artist_field, album_field, year_field, song_field))

            new_artist = find_object(artist_field, artist_list)
            if new_artist is None:
                new_artist = Artist(artist_field)
                artist_list.append(new_artist)
            new_artist.add_song(album_field, year_field, song_field)

        #     if new_artist is None:
        #         new_artist = Artist(artist_field)
        #         artist_list.append(new_artist)
        #     elif new_artist.name != artist_field:
        #         # we've just read details for a new artist
        #         # retrieve the artist object if there is one,
        #         # otherwise create a new artist object and add it to the artist list.
        #         new_artist = find_object(artist_field, artist_list)
        #         if new_artist is None:
        #             new_artist = Artist(artist_field)
        #             artist_list.append(new_artist)
        #         new_album = None
        #
        #     if new_album is None:
        #         new_album = Album(album_field, year_field, new_artist)
        #         new_artist.add_album(new_album)
        #     elif new_album.name != album_field:
        #         # We've just read a new album for the current artist
        #         # retrieve the album object if there is one,
        #         # otherwise create a new album object and add it to the album list.
        #         new_album = find_object(album_field, new_artist.albums)
        #         if new_album is None:
        #             new_album = Album(album_field, year_field, new_artist)
        #             new_artist.add_album(new_album)
        #
        #     # create new song object and add it to the current album's collection
        #     new_song = Song(song_field, new_artist)
        #     new_album.add_song(new_song)
        #
        # # 在这种方式下，readline结束，所有行对象都添加了，不需要额外的步骤了。
        # # # after read the last line of the text file, we will have an artist and album that haven't been stored -
        # # # process them now
        # # if new_artist is not None:
        # #     if new_album is not None:
        # #         new_artist.add_album(new_album)
        # #     artist_list.append(new_artist)

    return artist_list


def create_checkfile(artist_list):
    """Create a check file from the object data for comparison with the original file"""
    with open("checkfile.txt", "w") as checkfile:
        for new_artist in artist_list:
            for new_album in new_artist.albums:
                for new_song in new_album.tracks:
                    print("{0.name}\t{1.name}\t{1.year}\t{2.title}".format(new_artist, new_album, new_song),
                          file=checkfile)


if __name__ == "__main__":
    artists = load_data()
    print("There are {} artists".format(len(artists)))
    create_checkfile(artists)
# help(Album)


# help(Song)
# help(Song.__inti__)
# print(Song.__doc__)  # print only doc strings of the object -> here, just description of the class
# print(Song.__inti__.__doc__)  # method doc strings
# 小结：.__doc__和help等价。
# another way to set doc string which however, won't work in python 2.
# Song.__inti__.__doc__ = """ Song init method
#
#         Args:
#             title (str): Initialises the `title` attribute
#             artist (Artist): An Artist object representing the `duration` attribute.
#             duration (Optional[int]): Initial value for the `duration` attribute.
#                 will default to zero if not specified.
#         """

