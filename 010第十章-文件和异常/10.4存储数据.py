# 使用json来存储数据，json_dump写入和json_load读取
import json
numbers = [1, 2, 3, 4, 5]
filename = 'numbers.json'
with open(filename, 'w') as f:
    json.dump(numbers, f)

with open(filename) as f:
    content = f.read()
    print(content)

# 使用json.load将json文件内容读取到内存中，赋值给变量
with open(filename) as f:
    number = json.load(f)
print(number)

# 动手试一试
# 练习10-11 喜欢的数
favorite_numbers = input("Please tell me your favorite numbers: ")
file_name = 'number_test.txt'
with open(file_name, 'w') as f:
    json.dump(favorite_numbers, f)

with open(file_name) as f:
    num = json.load(f)
    print(f"I know your favorite number! It's {num}")

# 练习10-12 记住喜欢的数
new_file_name = 'favorite_number.txt'
try:
    with open(new_file_name) as f:
        num = json.load(f)
        print(f"\nI know your favorite number! It's {num}")
except FileNotFoundError:
    favorite_number = input("\nPlease tell me your favorite numbers: ")
    with open(new_file_name, 'w') as f:
        json.dump(favorite_number, f)


# 练习10-13 验证用户
def get_stored_number():
    """如果存储了用户名，就获取它。"""
    username_file = 'username.json'
    try:
        with open(username_file) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """提示用户输入用户名"""
    username = input("What's your name? ")
    username_file = 'username.json'
    with open(username_file, 'w') as f:
        json.dump(username, f)
    return username


def greet_user():
    """问候用户，并指出其名字。"""
    username = get_stored_number()
    while True:
        enter_name = input(f"\nPlease confirm your name is {username.title()}(Yes/No): ")
        if enter_name == 'Yes':
            print(f"Welcome back, {username}")
            break
        elif enter_name == 'No':
            username = get_new_username()
            print(f"We'll remember you when you come back, {username}")
            break
        else:
            print("Please enter Yes or No!")


greet_user()