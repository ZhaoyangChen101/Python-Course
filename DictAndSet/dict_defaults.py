from contents import pantry

chicken_quantity = pantry.setdefault("chicken", 0)
print(f"chicken: {chicken_quantity}")

beans_quantity = pantry.setdefault("beans", 0)
print(f"beans: {beans_quantity}")

# setdefault 和get一样的作用也！只是setdefault在查询到没有的情况下，
# 会将(key, default)插入进去，get只是返回默认值，没有插入的一步，
# 上下两块代码效果对比可知。

ketchup_quantity = pantry.get("ketchup", 0)
print(f"ketchup: {ketchup_quantity}")

z_quantity = pantry.setdefault("zucchini", "eight")
print(f"zucchini: {z_quantity}")

print()
print("`pantry` now contains...")

for key, value in sorted(pantry.items()):
    print(key, value)
