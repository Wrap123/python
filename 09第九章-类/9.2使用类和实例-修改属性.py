# 动手试一试
"""
1、修改实例属性
2、直接修改属性
3、用方法修改实例属性
"""
# 练习9-4 就餐人数
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"There is a restaurant here,"
              f"it's {self.cuisine_type} cuisine,and it's name is {self.restaurant_name}.\n")

    def open_restaurant(self):
        print(f"The {self.restaurant_name} restaurant is open now.\n")

    def set_number_served(self, num):
        self.number_served = num

    def increment_number_served(self, increment_num):
        self.number_served += increment_num


# 新增number_served属性，修改后再打印
restaurant = Restaurant('AAA', 'BBB')
restaurant.number_served = 123
print(f"{restaurant.restaurant_name} {restaurant.cuisine_type} {restaurant.number_served}")

# 调用设置就餐人数的set_number_served方法后，再打印值
restaurant.set_number_served(10)
print(f"{restaurant.number_served}")

# 调用增量增加就餐人数的increment_number_served方法后，再打印值
restaurant.increment_number_served(50)
print(f"{restaurant.number_served}")


# 练习9-5 尝试登陆次数
class User:
    def __init__(self, first_name, last_name, login_attempts):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = login_attempts

    def describe_user(self):
        print(f"This girl's name is {self.first_name}{self.last_name}.")

    def greet_user(self):
        print(f"Hello Mr.{self.first_name}, Welcome to my house.\n")

    def increment_login_attempts(self):
        self.login_attempts += 1
        print(self.login_attempts)

    def reset_login_attempts(self):
        self.login_attempts = 0
        print(self.login_attempts)


# 根据类创建实例
user = User('B', 'C', 100)

# 每调用一次，数字会加1并打印
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()

# 重置数字为0
user.reset_login_attempts()
