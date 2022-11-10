# interpolation works in python2 and it can be obsoleted
# but it is useful to learn because there are online codes in python2
# and you may be involved in projects in python2
# you shouldn't use these in python 3 code.
age = 24
print("My age is %d years" % age)

major = "years"
minor = "months"
# 对比python3 的format replacement fields，python2就没有那么多的弹性，必须是逐一替代值。
print("My age is %d %s, %d %s" % (age, major, 6, minor))
print("Pi is about %f" % (22 / 7))
print("Pi is about %60.50f" % (22 / 7))
# %x for number in hexadecimal, %o for octal, and %e for scientific notation

