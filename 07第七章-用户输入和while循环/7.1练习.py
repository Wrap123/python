# input() 用户输入函数，这里python会解读输入的内容为字符串
name = input("Please enter your name: ")
print(f"\nHello, {name}!")

# 提示超过一行时
promt = "If you tell us who you are, we can personalizee the mess you see." \
        "\nWhat is your first name?"
name = input(promt)
print(f"\nHello, {name}!")
print(type(name))

# 使用int()来转换格式，获取数值输入,输入数字之外的，转换失败会执行报错
age = input("How old are you? ")
age = int(age)
print(type(age))
if age >= 18:
    print("Welcome to my home!")
else:
    print("Sorry,you're not 18 years old,so you can't come into my home!")

# 求模运算，求两数相除后的余数
# 格式：a % b  代表a除以b，如果是4除以2，那么余数为0，如果是4除以3，那么余数为1
# 可以用来判断这个数字是奇数还是偶数
number = input("Enter a number: ")
number = int(number)
if number % 2 == 0:
    print(f"The number {number} is even.")
else:
    print(f"The number {number} is odd.")

# 动手试一试
# 7-1 汽车租赁
car = input("Please tell me what kind of car you want to rent?")
print(f"Let me see if I can find you a {car.title()}.")

# 7-2 餐馆定位
people_num = input("May I have your number, please?")
people_num = int(people_num)
if people_num > 8:
    print("I'm sorry, there are no tables available.")
else:
    print("Oh, we have a table.")

# 7-3 10的整数倍
num = input("Please random input a number:")
num = int(num)
if num % 10 == 0:
    print("是整数倍")
else:
    print("不是整数倍")
