"""动手试一试，练习9-10"""
# 创建模块，在Import_Test.py中进行导入测试


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

