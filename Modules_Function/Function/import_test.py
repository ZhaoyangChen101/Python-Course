import blackjack
# from blackjack import *

# g = sorted(globals())
# # 全局的方法和名字都有，不仅限于名字。
# # 此时就没有名字前有下划线的方法_deal_card了。
#
# for x in g:
#     print(x)

# print(__name__)  # __main__
#
# blackjack._deal_card(blackjack.dealer_card_frame)
# _deal_card(dealer_card_frame)
# # 因为python没有private, protected的用法，所以module内的所有都是公开的
#
# blackjack.play()

# 在blackjack __name = '__main__' 加上之后，下方语句无法运行了。
# blackjack._deal_card(blackjack.dealer_card_frame)
# blackjack.play()

# _有一个小用处，tuple unpack的时候，用以"忽略"不重要的元素
personal_details = ("Zhaoyang", 24, "China")
name, _, country = personal_details
print(name, country)





