# 使用sort()方法对列表永久排序
cars = ['bmw', 'audi', 'toyota', 'subaru']
## 按字母顺序排列
cars.sort()
print(cars)
## 按字母顺序的相反的顺序排列
cars.sort(reverse=True)
print(cars)

# 使用函数sorted()对列表进行临时排序
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("\nHere is the orginal list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list again:")
print(cars)
print(sorted(cars, reverse=True))

# 倒着打印列表（是直接将列表倒过来，不是按顺序）
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.reverse()
print(f"\n{cars}")
# reverse方法是永久修改，再调用一次就可以恢复
cars.reverse()
print(cars)

# 确定列表的长度 -- 即查询有几个元素
cars = ['bmw', 'audi', 'toyota', 'subaru']
print()
print(len(cars))