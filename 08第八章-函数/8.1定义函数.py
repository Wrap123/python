# 定义函数，使用关键字def来定义函数
def greet_user(username):
    """显示简单的问候语。"""
    print(f"Hello, {username.title()}!")


greet_user('john')


# 实参和形参
# 形参：是定义函数时的变量，在上边的例子中，”username“就是形参，可以理解为，一个形状，没有实际的东西
# 实参：是调用函数时输入的对应的值，在上边的例子中，“john”就是实参，可以理解为，实际的值

# 动手试一试
# 练习8-1 消息
def display_message():
    print("Start learning functions")


display_message()

# 8-2 喜欢的图书（值得一提的是，定义函数的上下必须要空两行，不然会有格式的错误提示，但是还能正常运行）


def favorite_book(title):
    print(f"One of my favorite books is {title.title()}")


favorite_book('Alice in Wonderland')
