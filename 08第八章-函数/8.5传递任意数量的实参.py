# 在函数的形参前加一个*，就可以实现一个形参，传递任意数量的实参
#   但是实参是会被放在一个元组内，不管有几个实参
# 例如
def make_pizza(*toppings):
    """测试打印顾客点的所有配料（看看是什么格式）"""
    print(toppings)
    """概述要制作的披萨"""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")


make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

# 任意数量实参的*形参要放在所有形参的最后，但是有默认值的形参也要放在最后，那么谁前谁后呢？


def make_food(time, kind='rice', *seasonings):
    print(f"She want to eat {kind},I need to be ready to cook at {time} o'clock.")
    print("We need this seasoning:")
    for seasoning in seasonings:
        print(f"- {seasoning}")


make_food('11', 'bread', 'salt', 'vinegar')
# 得出结论：任意数形参必须放最后
# 要注意的是：即便配置了默认值形参，调用的时候默认值形参的实参也是不能少，
# 因为少了之后，后边几个原本想归属于任意数量实参的值，其中一个会变为默认值形参的值
# 就算写关键字实参也不行，因为关键字实参要放在所有实参后边，但是放在后边就又和任意数量实参冲突了

# 8.5.2 使用任意数量的关键字实参
#   使用“**形参”的格式，创建一个空字典，会将所有的实参都放在这个字典内


def build_profile(first, last, **user_info):
    """创建一个空字典（**userinfo），其中包含我们知道的有关用户的一切"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
print(f"\n{user_profile}")

# 动手试一试
# 练习8-12 三明治


def make_sandwich(*ingredients):
    print("\nThis sandwich contains the following ingredient: ")
    for ingredient in ingredients:
        print(f"- {ingredient.title()}")


make_sandwich('bread', 'ham', 'lettuce')
make_sandwich('aaa', 'bbb')

# 练习8-13 用户简介


def build_profile(first, last, **user_info):
    """创建一个空字典（**userinfo），其中包含我们知道的有关用户的一切"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


my_info = build_profile('Bao', 'YaozU', age='18', money='none')
print(my_info)

# 练习8-14 汽车


def car_info(manufacturers, model, **other_info):
    other_info['manufacturer'] = manufacturers
    other_info['model_number'] = model
    return other_info


car = car_info('subaru', 'outback', color='blue', tow_package=True)
print(car)
