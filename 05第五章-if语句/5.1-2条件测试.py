cars = ['audi', 'bmw', 'subaru', 'toyota']
# 当输出是bmw时，全部大写，否则只是首字母大写
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
"""
交互模式下执行测试
car = 'bmw'
car == 'bmw'
"""
# 检查不相等
requested_topping = 'mushrooms'
if requested_topping != 'anchvoies':
    print("Hold the anchvoies")

# 数值比较
## 小于：<  大于：>  小于等于：<=  大于等于：>=  不等于：!=   等于：==
answer = 18
if answer <= 18:
    print("That is not the correct answer. Please try again!")

# 检查多个条件,使用and 或者or
## 当tom大于18岁，并且为男性时，打印....,当tom小于18，性别未知，打印....
min_age = 18
genders = ('male', 'female')
tom = 22
for gender in genders:
    if (tom >= 18) and (gender == 'male'):
        print("Tom and Maria can get married!")
    elif (tom < 18) or (gender == 'Null'):
        print("No way")
    else:
        print("May be!")

# 检查特定值是否包含在列表中（in）
## 披萨配料
requested_toppings = ['mushrooms', 'onions', 'pineapple']
print()
print('mushrooms' in requested_toppings)
print('pepperoni' in requested_toppings)

# 检查特定值是否不包含在列表内（not in）
## 禁言用户
banned_users = ['andrew', 'carolina', 'tom']
user = 'maria'
if user not in banned_users:
    print(f"{user.title()},you can post a response if you wish.")

"""
布尔值：
通常用于记录条件，它的结果只能是True，或者是False
eg：
游戏是否正在运行
    game_active = True
用户是否可以编辑网站内容
    user_edit = False
ASR配置是否开启
    asr_config = True
"""