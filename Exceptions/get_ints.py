import sys


def getint(prompt):
    while True:
        try:
            number = int(input(prompt))
            return number
        except EOFError:
            sys.exit(1)
        # except ValueError:
        # except Exception:  # ValueError的父类
        # # 虽然这样没问题，但还是要具体，因为可以具体问题具体分析，不会一刀切。
        except:  # all exceptions
            print("Invalid number entered, please try again.")
        finally:  # finally的意思是无论异常有没有出现都会执行。
            print("The finally clause always executes.")

# x = int(input("Enter a number: "))


first_num = getint("Please enter the first number ")
second_num = getint("Please enter the second number ")

try:
    print("{} divided by {} is {}".format(first_num, second_num, first_num / second_num))
except ZeroDivisionError:
    print("You cannot divide by zero.")
    sys.exit(2)
else:  # 未捕捉到异常，即程序正常运行，则运行else板块，和for while + else的else用法一致。
    print("Division performed successfully.")


