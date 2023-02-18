magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

# 循环输出并打印附加消息
'''
小提示：
    for循环中，print()方法前有缩进的，是对列表内所有元素值都遍历执行一遍
    而没有缩进的，代表只执行一次，不会重复执行
    for语句后的“:”号不要忘了加
'''
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")
print("Thank you, everyone. That was a great magic show!\n")


# 练习4-1
pizzas = ['aaa', 'bbb', 'ccc']
for pizza in pizzas:
    print(f"I like {pizza} pizza.")
print("\nI really love pizza!")

# 练习4-2
animals = ['dog', 'cat', 'bird']
for animal in animals:
    print(animal)
    print(f"{animal.title()} would make a great pet.")
print("\nAny of these animals would make a great pet!")

