# We need an empty dictionary, to store and display the letter frequencies.
word_count = {}

# Text string
text = "Later in the course, you'll see how to use the collections Counter class."

# Your code goes here ...
for character in text:
    word = character.casefold()
    word_count[word] = word_count.setdefault(word, 0) + 1

# Printing the dictionary
for letter, count in sorted(word_count.items()):
    print(letter, count)
