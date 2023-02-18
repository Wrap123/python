# 切分列表
## 打印列表索引从1~3的元素值
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[1: 3])

## 打印列表索引从0~3的元素值（第一个索引可省略）
print(players[:3])

## 打印列表索引从2到最后的元素值（最后一个索引可省略）
print(players[2:])

# 用负数索引，打印列表最后三个元素值
print(players[-3:])

# 遍历前三名队员，并循环打印
print("Here are the first three players on my team")
for player in players[:3]:
    print(player.title())

# 复制列表（创建可独立修改的副本）
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("\nMy favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)
"""
注：friend_foods = my_foods 这样是完全相等的两个变量，不是复制一个副本，无论修改哪一个列表，另外一个也都会变
"""








