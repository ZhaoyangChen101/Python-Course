text = """Education is not the learning of facts
but the training of the mind to think

– Albert Einstein"""

prepositions = {"as", "but", "by", "down", "for", "in", "of", "on", "to", "with"}

text_set = set(text.split())  # 如果默认就是any whitespaces，这里甚至回车也会分开。
print(text_set)
preps_used = text_set.intersection(prepositions)

