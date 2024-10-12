#append()可将元素添加到列表的末尾，且不影响表内其他元素。
motorcycles = ["honda","yamaha","suzuki"]
print(motorcycles)
motorcycles = []
motorcycles.append("honda")
motorcycles.append("yamaha")
motorcycles.append("suzuki")
print(motorcycles)
motorcycles.append("ducati")
print(motorcycles)