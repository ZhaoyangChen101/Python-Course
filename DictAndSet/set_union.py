# farm_animals = {'sleep', 'hen', 'cow', 'horse', 'goat'}
# wild_animals = {'lion', 'elephant', 'tiger', 'goat', 'panther', 'horse'}
#
# all_animals_1 = farm_animals.union(wild_animals)
# print(all_animals_1)
#
# all_animals_2 = wild_animals.union(farm_animals)
# print(all_animals_2)
#
# all_animals_3 = wild_animals | farm_animals
# print(all_animals_3)

from prescription_data import adverse_interactions

meds_to_watch = set()
# for interaction in adverse_interactions:
#
#     # meds_to_watch.add(interaction)
#     # 试了下不可用add，因为set只能添加hashable type，set并非hashable，故不能添加。
#     # 但是set union set然后形成一个大的set的，是okay的，故此处用union。
#     # meds_to_watch = meds_to_watch.union(interaction)
#     # 与union等效的写法：
#     # meds_to_watch = meds_to_watch | interaction
#
#     # update只是modify原本的set，adding elements from other sets.
#     # meds_to_watch.update(interaction)
#     # .update(*other)
#     # update的等价写法：
#     meds_to_watch |= interaction

# 因为update(*other)该方法接受若干sets等iterable,下面一句等价上面的循环。
meds_to_watch.update(*adverse_interactions)
# meds_to_watch.update(adverse_interactions) 不是说接受任何形式的iterable的嘛，这句不行，上句行。
# 原因是这样的，iterable接受，只是在方法内部遍历的时候，想象for循环，[{},{},...{}]
# 这里的element是set，就不行，因为set是unhashable，不能放在set里面
# 小结：关于set的这些方法对于带入的iterable的要求是：里面的elements是hashable的，
# 我理解的就是immutable objects。


print(sorted(meds_to_watch))
print(*sorted(meds_to_watch), sep='\n')
