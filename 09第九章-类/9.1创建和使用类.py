"""
面向对象编程
编写表示现实世界中的事物和情景的类，定义一大类对象都有的通用行为，基于这些类来创建对象
"""

# 创建Dog类


class Dog:
    """一次模拟小狗的简单尝试。"""

    def __init__(self, name, age):
        """初始化属性name和age。"""
        self.name = name
        self.age = age

    def sit(self):
        """模拟小狗收到命令时蹲下"""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """模拟小狗收到命令时打滚。"""
        print(f"{self.name} rolled over!")

# 根据类创建实例


my_dog = Dog('Willie', 6)
print(f"My dog's name is {my_dog.name},and it's {my_dog.age} years old.")

# 调用方法
my_dog.sit()
my_dog.roll_over()

# 动手试一试
# 练习9-1 餐馆


class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"There is a restaurant here,"
              f"it's {self.cuisine_type} cuisine,and it's name is {self.restaurant_name}.\n")

    def open_restaurant(self):
        print(f"The {self.restaurant_name} restaurant is open now.\n")


restaurant = Restaurant('YingKeLai', 'Sichuan')
print(f"\nThe restaurant name is {restaurant.restaurant_name}")
print(f"The restaurant's cuisine is {restaurant.cuisine_type}")
restaurant.describe_restaurant()
restaurant.open_restaurant()

# 练习9-2 三家餐馆
restaurant_2 = Restaurant('AAA', 'Sichuan')
restaurant_2.describe_restaurant()

restaurant_3 = Restaurant('BBB', 'Sichuan')
restaurant_3.describe_restaurant()

restaurant_4 = Restaurant('CCC', 'Sichuan')
restaurant_4.describe_restaurant()


# 练习9-3 用户


class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print(f"This girl's name is {self.first_name}{self.last_name}.")

    def greet_user(self):
        print(f"Hello Mr.{self.first_name}, Welcome to my house.\n")


user_1 = User('L', 'ucy')
user_1.describe_user()
user_1.greet_user()

user_2 = User('M', 'ari')
user_2.describe_user()
user_2.greet_user()

user_3 = User('K', 'ath')
user_3.describe_user()
user_3.greet_user()
