a_string = "this is \na string split\t\t and tabbed"
print(a_string)

raw_string = r"this is \na string split\t\t and tabbed"
print(raw_string)

b_string = "this is" + chr(10) + "a string split" + chr(9) + chr(9) + "and tabbed"
print(b_string)
# chr(int)是将数字转换为16进制，0~16 -> 0,1,2,3,5,6,7,8,9,a,b,c,d,e,f,10
# 几个特殊值：chr(9) = \t, chr(10) = \n, chr(13) = \r
# / -> forward slash, \ -> backslash

backslash_string = "this is a backslash \followed by some text "
print(backslash_string)
# \f is a page break control character

backslash_string = "this is a backslash \\followed by some text"
print(backslash_string)

# error_string = r"this string ends with \"
# error_string = r"this string ends\with\"
# print(error_string)
# \ is called escape character并且在最末尾，所以上方出现了错误
# 这种情况\在最末尾，不论前方是否有r表明该string为raw string
# 它都会escape掉最末尾的引号
# 结论：只要\在字符串最末尾，都需要使用两个\。

test = "\zab"
print(test)
# 果不其然，a被escape掉了
# 小结：\后面只有特殊符号会被escape掉，特殊的字符会被escape不成为字符而是和\一起形成功能
# \t, \n, \r, \f是功能
# 只是被跳过：\a, \b, \v,\', \" \x+两个字母会成为不同的符号
