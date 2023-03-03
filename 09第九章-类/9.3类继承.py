# 先定义一个父类
class Car:
    """一次模拟汽车的简单尝试"""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self,mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


# 根据上边的类，创建类，上边类为父类（超类），下边的为子类
class ElectricCar(Car):
    """电动汽车的独特之处"""
    def __init__(self, make, model, year):
        """初始化父类的属性（相当于把父类的属性和方法都拷贝到这里了）"""
        super().__init__(make, model, year)


# 调用子类,创建实例
my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())


# 当类中的细节越来越多，可以将类中的一部分提取出来，作为一个独立的类，然后通过实例用作属性的方式去调用
# 创建一个类，用作给电车ElectricCar的属性
class Battery:
    """一次模拟电动汽车电瓶的简单常识。"""
    def __init__(self, battery_size=75):
        """初始化电瓶的属性，设置默认值为75"""
        self.battery_size = battery_size

    def describe_battery(self):
        """打印一条描述电瓶容量的信息"""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """打印一套消息，指出电瓶车的续航里程。"""
        if self.battery_size == 75:
            mileage = 260
        elif self.battery_size == 100:
            mileage = 315
        else:
            mileage = None
        print(f"This car can go about {mileage} miles on a full charge.")


# 这里为了区分演示，拷贝上边的电车子类下来，实际操作中就直接把Battery方法放在ElectricCar上边，然后加一条属性
class ElectricCar(Car):
    """电动汽车的独特之处"""
    def __init__(self, make, model, year):
        """初始化父类的属性（相当于把父类的属性和方法都拷贝到这里了）"""
        super().__init__(make, model, year)
        """新增一个battery的类信息作为属性"""
        self.battery = Battery()


# 调用子类,创建实例
my_tesla = ElectricCar('tesla', 'model s', 2019)
print(f"\n{my_tesla.get_descriptive_name()}")
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()