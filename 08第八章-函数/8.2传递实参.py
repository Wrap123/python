# 通过各种方式，把实参传递给函数的形参

# 位置实参
"""
概念：就和上一节的使用方式一样，最简单朴素的方式，按照实参顺序来定义形参
要注意实参里的内容顺序，别写反了
"""


def describe_pet(animal_type, pet_name):
    """显示宠物的种类和名字信息"""
    print(f"\nI have a {animal_type}.")
    print(f"It's name is {pet_name}.")


# 要空两行来写调用执行代码
describe_pet('hamster', 'harry')

# 关键字实参（这个要指定形参是哪个，用a=b的形式来表示，这种方式不用强制要求形参和实参位置一一对应上）
describe_pet(animal_type='dog', pet_name='willie')
describe_pet(pet_name='willie', animal_type='dog')

# 默认值（在定义函数时，设置一个初始的实参，即为默认值）
# 需要注意的是：设置默认值的形参，要写在最后


def describe_pet(pet_name, animal_type='dog'):
    """显示宠物的种类和名字信息"""
    print(f"\nI have a {animal_type}.")
    print(f"It's name is {pet_name}.")


# 位置传参和关键字传参可以搭配使用，而且就算配置了默认值，如果在调用时又指定了实参，那么以调用时的为准，默认值优先级最低
describe_pet('aaa')
describe_pet('bbb', animal_type='ccc')

# 动手试一试
# 练习8-3 T恤


def make_shirt(size, fond):
    print(f"\nMake a size {size} T-shirt and print '{fond}' on it.")


make_shirt('m', 'I love you!')

# 练习8-4 大号T恤


def make_shirt(size='XXL',fond='I love Python'):
    print(f"\nMake a size {size} T-shirt and print '{fond}' on it.")


make_shirt()
make_shirt('m', 'I love you!')

# 练习8-5 城市


def describe_city(city, country='China'):
    print(f"{city.title()} is in {country.title()}.")


describe_city('henan')
describe_city('beijing')
describe_city('New York', 'american')