split_string = "This string has been\nsplit over\nseveral\nlines"
print(split_string)

tabbed_string = "1\t2\t3\t4\t5"
print(tabbed_string)

print('The pet shop owner said "No, no, \'e\'s uh,...he\'s resting".')
# or
print("The pet shop owner said \"No, no, 'e's uh,...he's resting\".")

print("""The pet owner said "No, no, 'e's uh,..he's resting".""")

another = """This string has been
split over
several
lines"""

print(another)

another2 = """This string has been \
split over \
several \
lines"""
print(another2)

print("""The pet owner said "No, no, \
'e's uh,..he's resting".""")

# what if you want to include backslash
# print("C:\Users\timbuchalka\notes.txt ") # 新知识：鼠标放在代码行然后command+D，该行代码就直接复制过来了。
# two ways to escape backslash, the first one is recommended.
print("C:\\Users\\timbuchalka\\notes.txt ")
print(r"C:\Users\timbuchalka\notes.txt ")
