# if-elif-else结构
# 根据年龄段收费的游乐场
age = 12
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $25.")
else:
    print("Your admission cost is $40.")
# 简化代码
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40
print(f"Your admission cost is ${price}.")

# 使用多个else代码（对65岁以上的半价）
age = 66
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age <= 65:
    price = 40
else:
    price = 20
print(f"Your admission cost is ${price}.")

# 也可以直接将else省略，并不要求if后必须跟else
age = 66
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age <= 65:
    price = 40
elif age >= 65:
    price = 20
print(f"Your admission cost is ${price}.")

# 动手试一试 试题
# 1.外星人颜色
alien_color = "red"
if alien_color in "green":
    print("Congratulations on your 5 points!")
# 2.外星人颜色
if alien_color in "green":
    print("Congratulations on your 5 points!")
else:
    print("You get 10 points.")
# 3.外星人颜色3
if alien_color in "green":
    print("Congratulations on your 5 points!")
elif alien_color in "yellow":
    print("You get 10 points.")
else:
    print("You get 15 points.")
# 4.人生的不同阶段
age = 25
if age < 2:
    print("You are a 婴儿.")
elif (age >= 2) and (age < 4):
    print("You are 幼儿.")
elif (age >= 4) and (age < 13):
    print("You are a 儿童.")
elif (age >= 13) and (age < 20):
    print("You are a 青少年.")
elif (age >= 20) and (age < 65):
    print("You are a 成年人.")
elif age >= 65:
    print("You are a 老梆子.")

# 5.喜欢的水果
favorite_fruits = ['banana', 'apple', 'orange']
if 'apple' in favorite_fruits:
    print("You really like apple")
if 'watermelon' in favorite_fruits:
    print("You really like watermelon")
if 'banana' in favorite_fruits:
    print("You really like banana")
if 'orange' in favorite_fruits:
    print("You really like orange")
if 'Dragon fruit' in favorite_fruits:
    print("You really like Dragon fruit")
