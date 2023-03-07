# 打开文件时，可以指定几种模式，相当于Linux中的rwx读写执行权限了
"""
    'w'：写入模式（只写）
    'r': 读取模式（只读）
    'a': 附加模式（追加内容，不覆盖，相当于'>'和'>>'的区别）
    'r+': '读写模式'
"""
# 使用'w'模式写入内容，如果open文件时，文件不存在，则自动创建，如果文件存在，还用'w'模式，那么会清空文件内所有内容再写入的！！！！
filename = 'programming.txt'
with open(filename, 'w') as file_object:
    file_object.write("I love programming.")

with open(filename, 'r') as file_object:
    print(file_object.read())

# 写入多行
# write函数不会在写入的文本末尾添加换行符，如果要换行，需要在写入内容后追加换行符\n
filename = 'programming.txt'
with open(filename, 'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")

with open(filename, 'r') as file_object:
    print(file_object.read())

# 附加到文件（追加）
with open(filename, 'a') as file_object:
    file_object.write("HaHaHaHa\n")

with open(filename, 'r') as file_object:
    print(file_object.read())


# 动手试一试
# 练习10-3 访客
name = input("Enter your name:")
file_name = 'guest.txt'
with open(file_name, 'w') as file_object_1:
    file_object_1.write(name)

with open(file_name, 'r') as file_object_1:
    print(file_object_1.read())

# 练习10-4 访客名单
while True:
    hint = input("Please tell me your name: ")
    print(f"Hello {hint}, Welcome to my city.")
    filename = 'gest_book.txt'
    with open(filename, 'a') as file_object:
        file_object.write(f"{hint} is coming.\n")
    if hint == 'tom':
        break

# 练习10-5 调查
while True:
    cause = input("Why do you like programming?")
    with open('cause.txt', 'a') as file_object:
        file_object.write(f"{cause}\n")
    if cause == 'no':
        break
