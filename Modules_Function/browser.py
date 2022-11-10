import webbrowser

# # 打开一个网站
# webbrowser.open("https://www.python.org/", new=1)
#
# help(webbrowser)
# 下面未成功
# chrome = webbrowser.get('/usr/bin/google-chrome %s').open_new_tab("https://www.python.org/")
safari = webbrowser.get(using='safari')
safari.open("https://www.python.org/")
# for i in range(10):
#     print(1, 2, 3, sep=';', end=' ')


