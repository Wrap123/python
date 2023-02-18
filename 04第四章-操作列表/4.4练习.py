# 练习4-10：切片
my_foods = ['pizza', 'falafel', 'carrot cake', 'cannoli', 'ice cream']
print(my_foods)
## 分片打印前三个
print("\nThe first three items in the list are:")
print(my_foods[:3])
## 分片打印中间三个（.capitalize方法是将一句话的首写字母大写）
print("three items from the middle of the list are:".capitalize())
print(my_foods[1:4])
## 分片打印末尾三个
print("the last three items in the list are:".capitalize())
print(my_foods[-3:])

# 练习4-11：你的披萨，我的披萨
print()
pizzas = ['aaa', 'bbb', 'ccc']
friend_pizzas = pizzas[:]
pizzas.insert(0, 'AAA')
friend_pizzas.append('ddd')
print("My favorite pizzas are:")
for my_pizzas in pizzas:
    print(my_pizzas)

print("My friend's favorite pizzas are:")
for his_pizzas in friend_pizzas:
    print(his_pizzas)

# 练习4-12：使用多个循环
foods = ['pizza', 'falafel', 'carrot cake']
for my_foods in foods:
    print(f"I like {my_foods}")
for two_foods in foods[:2]:
    print(f"This {two_foods} is one of the best food")
