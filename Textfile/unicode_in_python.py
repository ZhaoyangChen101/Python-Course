with open('Jabberwocky.txt', encoding='utf-8') as jabber:   # 不声明r，因为默认就是读。
    for line in jabber:
        print(line.rstrip())   # 再次强调string是immutable的，strip是制造了一个copy。
