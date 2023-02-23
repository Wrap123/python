# 简介：for循环用于对于集合中的每个元素都执行一个代码块，而while循环则不断运行，直到指定的条件不满足为止
current_number = 1
while current_number <= 5:
    print(current_number)
    # current_number += 1 是 current_number = current_number + 1 的简写
    current_number += 1

# 让用户选择何时退出循环，while和input搭配使用
prompt = "\nTell me somethings, and I will repeat it back to you:" \
        "\nEnter 'quit' to end the progarm."
message = ""
while message != 'quit':
    message = input(prompt)
    # 添加一行，让退出时，不输出quit
    if message != 'quit':
        print(message)

# 标志（flag）：true时程序运行，false时停止
# 设置一个标志，用来判断程序是否处于活动状态。当某一个事件异常时，都可以设置标志为false，使其循环停止
# 设置标志的方式，就是简化了while语句，不需要再做任何比较，只要设置变量为true或者false即可
active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)

# 使用break退出循环
prompt = "\nPlease enter the name of a city you hava visited." \
         "\n(Enter 'quit' when you are finished.)"
while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}.")

# 在循环中使用continue
# 求10以内的奇数（不被2整除的数）
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)

# 避免无限循环
# 每个while循环都必须有停止运行的途径，避免一直执行下去
x = 1
while x < 5:
    print(x)
    # 例如不加 x += 1就会一直执行1……1下去
    x += 1

# 动手试一试
# 练习7-4 披萨配料
pizza_message = "\nPlease enter a pizza topping:" \
                "\n(Enter 'quit' when you want to finished.)"
active = True
while active:
    pizza = input(pizza_message)
    if pizza == 'quit':
        active = False
    else:
        print(f"We will add the {pizza} in the pizza.")

# 练习7-5 电影票
age_message = "\nPlease tell me your ages,this will affect the cost of your ticket:" \
              "\nIf you want to quit,you can enter 'quit' !"
active = True
while active:
    age = input(age_message)
    if age == 'quit':
        # break
        active = False
    elif int(age) > 12:
        print("Hello, 12 yuan for you.")
    elif int(age) < 3:
        print("Hello baby,you are free.")
    elif (int(age) > 3) and (int(age) < 12):
        print("Hello, 10 yuan for you.")

# 练习7-7 无限循环
n = 2
while n < 5:
    print("I love you❤")
    n += 1  # 注释掉这行就是无限循环了
