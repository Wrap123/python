# 7.3.1 在列表之间移动元素
# eg：一个列表内包含新注册但没验证过的网站用户，使用while循环验证用户后，将验证过的用户放在另外一张表中
# 首先，创建一个待验证的用户列表，和一个用于存储验证过用户的空列表
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
# 验证每个用户，直到没有未验证用户为止
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f"\nVerifying user: {current_user.title()}")
    confirmed_users.append(current_user)

# 显示所有已验证的用户
    print("The following users have been confirmed:")
    for confirmed_user in confirmed_users:
        print(confirmed_user.title())

# 7.3.2 循环删除列表内相同的元素
pets = ['dog', 'cat', 'dog', 'rabbit', 'cat', 'dog']
print(pets)  # 删除前打印一下
while 'cat' in pets:
    pets.remove('cat')
print(pets)

# 使用用户输入来填充字典
#   创建一个调查程序，询问调查者的名字和回答
responses = {}
polling_active = True   # 设置一个flag标志
while polling_active:
    # 提示输入被调查者的名字和回答
    name = input("\nWhat's your name?")
    response = input("Which mountain would you like to climb someday?")
    # 将回答存储在字典中
    responses[name] = response
    # 看看是否还有人要参与调查
    repeat = input("Would you like to let another person respond ? (yes/ no) ")
    if repeat == 'no':
        polling_active = False
# 调查结果，显示结果
print(responses)
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name.title()} would like to climb {response}.")

# 动手试一试
# 练习7-8 熟食店
sandwich_orders = ['aaa', 'bbb', 'ccc']
finished_sandwiches = []
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"I made your {sandwich} sandwich.")
    finished_sandwiches.append(sandwich)
    if len(sandwich_orders) == 0:
        print("Hello, all the sandwiches are ready")

# 练习7-9 一个产品卖完了，这就用ccc卖完了吧，删除列表内所有的ccc元素
sandwich_orders = ['aaa', 'bbb', 'ccc', 'ddd', 'ccc', 'vvv', 'ccc']
print(f"原本的列表：{sandwich_orders}")
print("The ccc in this list will soon be gone")
while 'ccc' in sandwich_orders:
    sandwich_orders.remove('ccc')
print(f"最后的列表：{sandwich_orders}")

# 练习7-10 梦想的度假圣地
dream_info = {}
dream_active = True
while dream_active:
    name = input("What's your name?")
    age = input("How old are you?")
    place = input("If you could visit one place in the world, where would you go?")
    dream_info[name] = [age, place]
    repeat = input("Would you like to let another person respond ? (yes/ no) ")
    if repeat == 'no':
        dream_active = False
print(dream_info)
for name, info in dream_info.items():
    print(f"{name.title()} is {info[0]} years old,and she is like {info[1]}.")

# 终于搞完，目前自己写代码最长最复杂的一次~
# end....2023年2月24日00:36
