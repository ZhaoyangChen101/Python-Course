numbers = [1, 45, 31, 16, 60]
# else in a loop
for num in numbers:
    if num % 8 == 0:
        # reject the list
        print("The numbers are unacceptable.")
        break
else:  # 如果loop中执行完成，即没有break，那么就执行接下来的代码。
    print("All numbers are fine")

# else can follow both if or for statements
