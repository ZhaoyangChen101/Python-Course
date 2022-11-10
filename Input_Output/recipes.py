import shelve

# blt = ["bacon", "lettuce", "tomato", "bread"]
# beans_on_toast = ["beans", "bread"]
# scrambled_eggs = ["eggs", "butter", "milk"]
soup = ["tin of soup"]
# pasta = ["pasta", "cheese"]

# with shelve.open('recipes') as recipes:
with shelve.open('recipes', writeback=True) as recipes:
    # recipes["blt"] = blt
    # recipes["beans on toast"] = beans_on_toast
    # recipes["scrambled eggs"] = scrambled_eggs
    # recipes["pasta"] = pasta
    # recipes["soup"] = soup

    # recipes["blt"].append("butter")
    # recipes["pasta"].append("tomato")
    # # 此处append 并没有成功，因为只是在memory中的list的copy版本进行了更改，但是并没有
    # # 触发write back out again的动作，所以没有成功。

    # temp_list = recipes["blt"]
    # temp_list.append("butter")
    # recipes["blt"] = temp_list
    #
    # temp_list = recipes["pasta"]
    # temp_list.append("tomato")
    # recipes["pasta"] = temp_list
    # # 这样就成功了，必须要reassign，另一种是writeback=True

    # recipes["soup"].append("croutons")  # 在writeback=True之后就能成功写好。
    # wirteback是Python会将对象缓存在内存中，直到你关闭shelve，或者使用sync方法的时候，
    # 才会对disk进行写的操作，来更新shelve。
    # 所以这个方法的缺点在于：当数据很大的时候，对内存的占用比较大。
    # sync在写入硬盘的时候，也会清空内存的缓存。
    # sync会被自动调用，当shelve关闭的时候。但是你也可以在任何地点时间使用，当你想要更新数据文件的时候。

    recipes["soup"] = soup  # 这个成功。
    # recipes.sync()
    soup.append("cream")  # 这个失败。哪怕有writeback，因为sync会清空缓存。
    # 这里会改变soup，但是recipe的读取的缓存数据没有了，因此对于recipe没有任何改变。
    # 如果把.sync取消，则是可以成功的，因为那个recipe指向soup的指针还在缓存中，随遇soup的更改，可以该改变recipe。
    # recipes["soup"].append("cream")  #这个就成功了。

    for snack in recipes:
        print(snack, recipes[snack])
    print(soup)