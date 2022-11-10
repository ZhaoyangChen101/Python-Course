import sqlite3

try:
    import tkinter
except ImportError:  # python2
    import Tkinter as tkinter

# conn = sqlite3.connect("music.sqlite")


class Scrollbox(tkinter.Listbox):

    def __init__(self, window, **kwargs):
        # tkinter.Listbox.__init__(self, window, **kwargs)  # python2
        super().__init__(window, **kwargs)

        self.scrollbar = tkinter.Scrollbar(window, orient=tkinter.VERTICAL, command=self.yview)

    def grid(self, row, column, sticky='nsw', rowspan=1, columnspan=1, **kwargs):
        # tkinter.Listbox.grid(self, row=row, column=column, sticky=sticky, rowspan=rowspan,
        # **kwargs) # python2
        super().grid(row=row, column=column, sticky=sticky, rowspan=rowspan, columnspan=columnspan, **kwargs)
        self.scrollbar.grid(row=row, column=column, sticky='nse', rowspan=rowspan)
        self['yscrollcommand'] = self.scrollbar.set


class DataListBox(Scrollbox):

    def __init__(self, window, connection, table, field, sort_order=(), **kwargs):
        # Scrollbox.__init__(self, window, **kwargs)  #python2
        super().__init__(window, **kwargs)

        self.linked_box = None
        self.link_field = None
        self.link_value = None

        self.cursor = connection.cursor()
        self.table = table
        self.field = field

        self.bind('<<ListboxSelect>>', self.on_select)

        self.sql_select = "SELECT " + self.field + ", _id" + " FROM " + self.table
        if sort_order:
            self.sql_sort = " ORDER BY " + ",".join(sort_order)
        else:
            self.sql_sort = " ORDER BY " + self.field

    def clear(self):
        self.delete(0, tkinter.END)

    def link(self, widget, link_field):
        self.linked_box = widget
        widget.link_field = link_field

    def requery(self, link_value=None):
        self.link_value = link_value  # store the id, so we know the "master" record we're populated from.
        if link_value and self.link_field:
            sql = self.sql_select + " WHERE " + self.link_field + "=?" + self.sql_sort
            print(sql)  # TODO delete this line
            self.cursor.execute(sql, (link_value,))
        else:
            print(self.sql_select + self.sql_sort)  # TODO delete this line 此处是拿来判断的，太重要了，我就写错了
            self.cursor.execute(self.sql_select + self.sql_sort)
        # clear the listbox contents before re-loading
        self.clear()
        for value in self.cursor:
            self.insert(tkinter.END, value[0])

        if self.linked_box:
            self.linked_box.clear()

    def on_select(self, event):
        if self.linked_box:
            print(self is event.widget)  # TODO delete this line
            index = int(self.curselection()[0])
            # lb = event.widget
            # index = lb.curselection()[0]
            value = self.get(index),  # 难怪这里有一个逗号，就是表示是一个tuple

            # get the ID from the database row
            # make sure we're getting the correct one, by including the link_value if appropriate
            # 当将function转换为方法的时候，就必须得注意变量不要使用全局变量，使用类内部的变量
            if self.link_value:
                value = value[0], self.link_value
                sql_where = " WHERE " + self.field + "=? AND " + self.link_field + "=?"
            else:
                sql_where = " WHERE " + self.field + "=?"
            link_id = self.cursor.execute(self.sql_select + sql_where, value).fetchone()[1]
            # SELECT name, _id FROM albums WHERE name='Greatest Hits'
            # 此处是根据名字来找id，所以以后遇到这种情况就一定要注意——
            # 名字不是唯一的，所以找到的id是所有id的第一个。
            self.linked_box.requery(link_id)

        # # get the artist ID from the database row
        # artist_id = conn.execute("SELECT artists._id FROM artists WHERE artists.name=?", artist_name).fetchone()
        # # fetchone返回的是一个tuple
        # alist = []
        # for row in conn.execute("SELECT albums.name FROM albums WHERE albums.artist=? ORDER BY albums.name", artist_id):
        #     alist.append(row[0])
        # albumLV.set(tuple(alist))
        # songLV.set(("Choose an album",))


# def get_songs(event):
#     lb = event.widget
#     index = int(lb.curselection()[0])
#     album_name = lb.get(index),
#
#     # get the artist ID from the database album
#     album_id = conn.execute("SELECT albums._id FROM albums WHERE albums.name=?", album_name).fetchone()
#     alist = []
#     for x in conn.execute("SELECT songs.title FROM songs WHERE songs.album=? ORDER BY songs.track", album_id):
#         alist.append(x[0])
#         songLV.set(tuple(alist))

if __name__ == "__main__":
    conn = sqlite3.connect("music.sqlite")

    main_window = tkinter.Tk()
    main_window.title("Music DB Browser")
    main_window.geometry("1024x768")

    main_window.columnconfigure(0, weight=2)
    main_window.columnconfigure(1, weight=2)
    main_window.columnconfigure(2, weight=2)
    main_window.columnconfigure(3, weight=1)  # space column on right

    main_window.rowconfigure(0, weight=1)
    main_window.rowconfigure(1, weight=5)
    main_window.rowconfigure(2, weight=5)
    main_window.rowconfigure(3, weight=1)

    # ====== labels ======
    tkinter.Label(main_window, text="Artists").grid(row=0, column=0)
    tkinter.Label(main_window, text="Albums").grid(row=0, column=1)
    tkinter.Label(main_window, text="Songs").grid(row=0, column=2)

    # ====== artist Listbox ======
    artist_list = DataListBox(main_window, conn, "artists", "name")
    artist_list.grid(row=1, column=0, sticky='nsew', rowspan=2, padx=(30, 0))
    artist_list.config(border=2, relief='sunken')
    #
    # artist_scroll = tkinter.Scrollbar(main_window, orient=tkinter.VERTICAL, command=artist_list.yview)
    # artist_scroll.grid(row=1, column=0, sticky='nse', rowspan=2)
    # artist_list['yscrollcommand'] = artist_scroll.set

    artist_list.requery()
    # for artist in conn.execute("SELECT artists.name FROM artists ORDER BY artists.name"):
    #     artist_list.insert(tkinter.END, artist[0])
    # artist_list.bind('<<ListboxSelect>>', get_albums)

    # ====== albums Listbox ======
    albumLV = tkinter.Variable(main_window)
    # tkinter variable要使用set方法进行赋值，这里是输入了一个tuple。
    albumLV.set(("Choose an artist",))
    # 这个variable改变的时候，albumlist的内容就会相应改变——因为listvariable。见mainloop下面一行，在改变之后album的listbox内容显示相应变化。
    album_list = DataListBox(main_window, conn, "albums", "name", sort_order=("name",))
    # album_list.requery(12)
    album_list.grid(row=1, column=1, sticky='nsew', padx=(30, 0))
    album_list.config(border=2, relief='sunken')

    # album_list.bind('<<ListboxSelect>>', get_songs)
    artist_list.link(album_list, "artist")

    # album_scroll = tkinter.Scrollbar(main_window, orient=tkinter.VERTICAL, command=album_list.yview)
    # album_scroll.grid(row=1, column=1, sticky='nse', rowspan=2)
    # album_list['yscrollcommand'] = album_scroll.set

    # ====== songs Listbox ======
    songLV = tkinter.Variable(main_window)
    songLV.set(("Choose an album",))
    song_list = DataListBox(main_window, conn, "songs", "title", ("track", "title"))
    # song_list.requery()
    song_list.grid(row=1, column=2, sticky="nsew", padx=(30, 0))
    song_list.config(border=2, relief="sunken")

    album_list.link(song_list, "album")
    # ====== mainloop ======
    # albumLV.set((1, 2, 3, 4, 5))  # 这里例子显示，可以将album存储成一个tuple，进行variable的set方法设置。
    # testList = range(0, 100)
    # albumLV.set(tuple(testList))
    main_window.mainloop()
    print("closing database connection")
    conn.close()
