#pop()在括号中输入对应的索引即可删除对应的元素，当括号内无索引时默认删除最后一个元素。pop（）所删除的值可以再次使用，而del语句不可以。
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
popped_motorcycles = motorcycles.pop(1)
print(motorcycles)
print(popped_motorcycles)