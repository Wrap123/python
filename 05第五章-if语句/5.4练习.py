# 检查特殊元素
# 打印披萨配料，要求：用for循环打印列表内元素，在其中一个元素的时候，另外打印其他内容
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print(f"Adding {requested_topping}")
print("\nFinished making your pizza!\n")

# 确定列表不是空的
# 当列表为空，不赋值时
requested_toppings = []
if requested_toppings:
    print("This is list with data")
    for requested_topping in requested_toppings:
        print(f"The data is {requested_topping}.")
else:
    print("This is an empty list.")

# 动手试一试
# 5-8 包含5个用户的列表，每次用户的时候，都打印一条消息，给admin用户的消息内容和其他的不一样，单独打印
staffs = ['admin', 'byz', 'abc', 'def', 'hjk']
for staff in staffs:
    if staff == 'admin':
        print(f"Hello {staff}, would you like to see a status report?")
    else:
        print(f"Hello {staff}, thank you for logging in again.")
# 5-9 添加if语句，检查用户列表是否为空
staffs = []
if staffs:
    for staff in staffs:
        if staff == 'admin':
            print(f"Hello {staff}, would you like to see a status report?")
        else:
            print(f"Hello {staff}, thank you for logging in again.")
else:
    print("\nWe need to find some users!")
# 5-10 检查用户名，模拟网站确保每个用户名都是独一无二的
current_users = ['Aa', 'BB', 'CC', 'dd', 'ee']
new_users = ['11', 'bb', '22', 'cc', '33']
test = [current_user.lower() for current_user in current_users]
print(test)
for new_user in new_users:
    if new_user.lower() in [current_user.lower() for current_user in current_users]:
        print(f"The name {new_user} has already been used, please tey something else.")
    else:
        print(f"The name {new_user} can be used.")

# 5-11 序数
# 打印每个数字对应的序数
nums = list(range(1, 10))
print(nums)
for num in nums:
    print(num)
    if num == 1:
        print("1st")
    elif num == 2:
        print("2nd")
    elif num == 3:
        print("3rd")
    else:
        print(f"{num}th")