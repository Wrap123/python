"""
Python 提供了如下 3 种函数，它们都可以帮我们实现读取文件中数据的操作：
    read() 函数：逐个字节或者字符读取文件中的内容；
    readline() 函数：逐行读取文件中的内容；
    readlines() 函数：一次性读取文件中多行内容。
"""

# 使用下列open()方法打开文件，不会自动close，会一直占着句柄，可在windows资源管理器中的句柄中根据打开文件名搜索
# 这种情况，打开的文件也没办法被删除
"""导入这个函数是为了执行'pause'命令，chcp是为了cmd的显示字符编码从默认的GBK改为UTF-8，可显示中文"""
# import os
# os.system('chcp 65001')
#
# while True:
#     content = open('pi_digits.txt', encoding='gbk')
#     info = content.read()
#     n = 0
#     for text in info:
#         n += 1
#         print(text)
#     os.system('pause')
#     break

# 这种with关键字的方式会在open打开文件后，自动执行close（这里要注意：不管windows地址还是Linux地址，路径中都为/）
file_path = 'E:/python/study/010第十章-文件和异常/pi_digits.txt'
with open(file_path) as file_object:
    contents = file_object.read()
print(contents)

with open(file_path) as file_object:
    for line in file_object:
        print(line.rstrip())   # 加上rstrip()方法，可以去掉右侧空行，否则每一行都会有一个换行符，print时也会算作一行

# 使用with关键字时，open返回的文件只能在with内用，可以把返回内容存储在一个列表内，可以让外部调用
with open(file_path) as file_object:
    lines = file_object.readlines()
for line in lines:
    print(line.rstrip())

pi_string = ''
for line in lines:
    pi_string += line.strip()   # 去掉所有空格
print(pi_string)
print(len(pi_string))
print(type(pi_string))
# 因为是小数，转为浮点型
float_pi = float(pi_string)
print(type(float_pi))

# 圆周率包含生日吗
file_path = 'E:/python/study/010第十章-文件和异常/pi_million_digits.txt'
with open(file_path) as file_object:
    lines = file_object.readlines()
pi_string = ''
for line in lines:
    pi_string += line.strip()
print(f"{pi_string[:52]}...")

birthday = input("Enter your birthday, in the form yymmdd:")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")

# 动手试一试
# 练习10-1 python学习笔记
# 因为文件内是中文，且当前python代码是在Windows内运行，所以默认编码是gbk，那么要在open时指定编码为utf-8才可以正常显示
testfile_path = "E:/python/study/010第十章-文件和异常/learning_python.txt"
with open(testfile_path, encoding='utf-8') as testfile:
    read_file_1 = testfile.read()
    print(read_file_1)

with open(testfile_path, encoding='utf-8') as testfile:
    for line in testfile:
        print(line.rstrip())

read_file = []
with open(testfile_path, encoding='utf-8') as testfile:
    read_file_3 = testfile.readlines()
    for file in read_file_3:
        read_file.append(file.strip())

print(read_file)

# 练习10-2 python改为C
with open(testfile_path, encoding='utf-8') as testfile:
    read_file_1 = testfile.read()
    print(f"{read_file_1.replace('python', 'C')}")
