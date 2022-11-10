morning = {'Java', 'C', 'Ruby', 'Lisp', 'C#'}
afternoon = {'Python', 'C#', 'Java', 'C', 'Ruby'}

possible_courses = morning ^ afternoon
print(1, possible_courses, sep=": ")
morning ^= afternoon
print(2, morning, sep=": ")
morning = {'Java', 'C', 'Ruby', 'Lisp', 'C#'}
morning.symmetric_difference_update(afternoon)
print(3, morning, sep=": ")

print()

# 当是list时，只需要将其中一个变为set，来调用sd方法，方法输入值为list是okay的。
morning = ['Java', 'C', 'Ruby', 'Lisp', 'C#']
afternoon = ['Python', 'C#', 'Java', 'C', 'Ruby']

# possible_courses = set(morning) ^ set(afternoon)
possible_courses = set(morning).symmetric_difference(afternoon)
print(possible_courses)


