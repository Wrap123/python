# 导入整个模块（也就是把同级目录下的car.py文件导进来）
import car as c   # 和import 函数的模块一样，as可以设置别名
# 导入模块内一个或多个类
from car import Car, ElectricCar

my_car = c.ElectricCar('Audi', 'Q5', 2019)
print(my_car.get_descriptive_name())

my_beetle = Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
