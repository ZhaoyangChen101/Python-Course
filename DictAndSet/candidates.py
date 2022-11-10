required_skills = ['python', 'github', 'linux']
candidates = {
    'anna': {'java', 'linux', 'windows', 'github', 'python', 'full stack'},
    'bob': {'github', 'linux', 'python'},
    'carol': {'linux', 'javascript', 'html', 'python', 'github'},
    'daniel': {'pascal', 'java', 'c++', 'github'},
    'ekani': {'html', 'css', 'github', 'python', 'linux'},
    'fenna': {'linux', 'pascal', 'java', 'c', 'lisp', 'modula-2', 'perl', 'github'},
}

interviewees = set()
for candidate, skills in candidates.items():
    # if skills.issuperset(required_skills):
    # 这里又是来提示你的：you can pass any iterables to set methods.
    if skills > set(required_skills):
        interviewees.add(candidate)

print(interviewees)

# 反思：set的操作，union, intersection, difference, symmetric_difference, isdisjoint()
# issuperset(), issubset()，都能来表现逻辑关系。
