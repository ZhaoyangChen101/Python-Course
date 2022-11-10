from enemy import Enemy, Troll, Vampire, VampireKing

dracula = VampireKing("Dracula")
print(dracula)
dracula.take_damage(12)
print(dracula)



# ugly_troll = Troll("Pug")
# print("Ugly troll - {}".format(ugly_troll))
#
# another_troll = Troll("Ug")
# print("Another troll - {}".format(another_troll), end="")
# another_troll.take_damage(18)
# print(another_troll)
#
# brother = Troll("Urg")
# print(brother)
#
# ugly_troll.grunt()
# another_troll.grunt()
# brother.grunt()
#
# vamp = Vampire("Vlad")
# print(vamp)
# vamp.take_damage(5)
# print(vamp)
#
# print("-" * 40)
# another_troll.take_damage(30)
# print(another_troll)
#
# # while vamp.alive:
# #     vamp.take_damage(1)
#
# vamp._lives = 0
# vamp._hit_points = 1
# print(vamp)




# random_player = Enemy('Basic enemy', 12, 1)
# print(random_player)
#
# random_player.take_damage(4)
# print(random_player)
#
# random_player.take_damage(8)
# print(random_player)
#
# random_player.take_damage(9)
# print(random_player)


# from player import Player
# # 虽然这种写法不推荐，但是只是在此是会更方便的。
#
# tim = Player("Tim")
# print(tim.name)
# print(tim.lives)
# tim.lives -= 1
# print(tim)
#
# tim.lives -= 1
# print(tim)
#
# tim.lives -= 1
# print(tim)
#
# tim.lives -= 1
# print(tim)
#
# tim.level = 2
# print(tim)
#
# tim.level = 5
# print(tim)
#
# tim.level = 3
# print(tim)
#
# tim.score = 500
# print(tim)

# print(tim.get_name())
# tim.set_lives(300)
