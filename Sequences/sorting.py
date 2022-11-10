# sorted function can be used for iterables
# note the difference between sorted and sort
# sorted是function，sort是method
# sorted需要将结果赋给新的list，而sort是inplace sorting
pangram = "The quick brown fox jumps over the lazy dog"

letters = sorted(pangram)
print(letters)  # letters are repeated accordingly
print(pangram)

numbers = [2.3, 4.5, 8.7, 3.1, 9.2, 1.6]
sorted_numbers = sorted(numbers)
print(sorted_numbers)
print(numbers)

# another_sorted_numbers = numbers.sort() # return none
numbers.sort()
print(numbers)
#print(another_sorted_numbers)

missing_letter = sorted("The quick brown fox jumped over the lazy dog",
                        key=str.casefold)
# 后面的这个key表示大小写不影响，记得key里面casefold没有括号。所以sorted默认是将大写摆在前面。
print(missing_letter)

names = ["Graham",
         "John",
         "terry",
         "eric",
         "Terry",
         "michael"
         ]
names.sort(key=str.casefold)
print(names)

