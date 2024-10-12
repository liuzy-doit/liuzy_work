#del语句会改变原列表，三元列表用del语句删除一个元素后，再次删除【2】时就会报错，就是因为此时列表只剩下两元素了。并且del语句会将值彻底删除，后续无法使用。
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
del motorcycles[2]
print(motorcycles)