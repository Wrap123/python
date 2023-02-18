# 摩托车列表
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# 修改列表第一个元素值
motorcycles[0] = 'ducati'
print(motorcycles)

# 附加（append）新的元素值到列表内，追加在末尾
motorcycles.append('ducati')
print(motorcycles)

# 插入（insert）新的元素值到列表内，需指定元素值和索引位置
motorcycles.insert(0, 'honda')
print(motorcycles)

motorcycles.insert(1, 'test')
print(motorcycles)

# 删除列表中元素，需指定元素索引位置
del motorcycles[1]
print(motorcycles)

## 删除指定索引范围的元素值
lis = [1, 2, 3, 4, 5]
print(lis)
del lis[0: 3]
print(lis)

# 使用方法pop()删除元素，弹出列表中最后一个元素，并且可以打印出弹出的元素
popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)

# 如果列表中的摩托车是按购买时间存储的，那么使用pop方法打印一条消息，指出最后购买的是哪款摩托车
last_owned = motorcycles.pop()
message = f"The last motorcycles I owen was a {last_owned.title()}"
print(message)

# 弹出列表中任意位置的元素
first_owned = motorcycles.pop(0)
print(first_owned.title())

## * 小tips；何时使用del和pop：如果列表内的一个元素删除后不再使用，就使用del，如果想删除后还可以继续使用，就用pop

# 根据值删除元素（不知道元素在列表中的索引位置时）
print(motorcycles)
motorcycles.insert(0, 'aaaa')
print(motorcycles)
motorcycles.remove('aaaa')
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")

# 注：remove()方法只能删除第一个指定的值，如果要删除的值在列表内多次出现，就需要使用循环




