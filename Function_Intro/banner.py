def banner_text(text: str = " ", screen_width: int = 80) -> None:
    # """
    # Print a string of a width of `screen_width`, where `text` is put at center.
    #
    # If `text` equals to `*`, print `*` for `screen_width` times.
    #
    # Otherwise, print a string of a width of `screen_width` with 2 `*` both at
    # the beginning and the end and with `text` at the center.
    #
    # :param text:
    # :param screen_width:
    # :return: None
    # :raises ValueError: If the length of `text` is beyond `screen_width` - 4.
    # """
    """ Print a string centred, with ** either side.

    :param text: The string to print
        An asterisk (*) will result in a row of asterisks.
        The default will print a blank line, with a ** border
        the left and right edges.
    :param screen_width: The overall width to print within
        (including the 4 spaces for the ** on either side).
    :raises ValueError: if the supplied string is too long to fit.
    """
    # if no annotations, there are no whitespaces for default values for these parameters
    # screen_width = 60
    if len(text) > screen_width - 4:
        # print("EEK!!", 60)
        # print("THE TEXT IS TOO LONG TO FIT IN THE SPECIFIED WIDTH", 60)
        raise ValueError("String {0} is larger than specified width {1}"
                         .format(text, screen_width))
    if text == "*":
        print("*" * screen_width)
    else:
        # 这里学到了一个str.center(width)的用法，将str放置在中间。
        centred_text = text.center(screen_width - 4)
        output_string = "**{0}**".format(centred_text)
        print(output_string)


banner_text("*", 60)
banner_text("Always look on the bright side of your life!", 60)
banner_text(screen_width=60)
# banner_text(,60) 这种情况会报错，为了表示60是输入的哪一个变量，就需要keyword来表明了
banner_text("There is something you should never forget", 60)
banner_text("That is to laugh and smile, dance and sing ^v^ ", 60)
banner_text("Believe that you are healthy, wealthy, and lucky", 60)
banner_text("I earn 1 million euros each year and I am happy", 60)
banner_text("I get admitted to thesis topic offered by Fraunhofer Institute of IMWS", 60)
banner_text("I get admitted to doctor program of TUM and EPFL", 60)
banner_text("I accept the unlimited wisdom", 60)
banner_text("*", 60)

# result = banner_text("Nothing is returned.", 60)
# print(result)  # None
#
# numbers = [4, 2, 7, 5, 8, 3]
# print(numbers.sort())  # None

# 小结：学到了一个新的快捷键：cmd + delete删除整行
# 两个常见exception error：TypeError和ValueError
# 如果自己没有写exception，遇到了exception可以前往built in exception网页查看异常的种类
# pycharm使用新知识：edit-find-replace-replace all
# positional or keyword parameters
# get the habit of documenting before you write your function
# so that you will have a clearer idea of what it is going to do.
# a bit of thought is always a good thing


