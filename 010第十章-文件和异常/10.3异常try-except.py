# 处理代码写错时，python返回的异常问题，使用try-expert代码块
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")

# 使用异常时，抛出错误后继续执行,处理ZeroDivisionError报错（是在除以0的时候，python内不允许被除数是0）
print("Give me two number, and I'll divide them.")
print("Enter 'q' to quit.")
while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by zero!")
    else:
        print(answer)
        break

# 处理打开不存在文本时的报错FileNotFoundError
filename = 'alice.txt'
try:
    with open(filename, encoding='utf-8') as f:
        f.read()
        print(f)
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist.")

# 分析文本
# split()方法可以把字符串按指定分隔符分开以列表的形式存储，默认是空格，其他分割符可以在()内输入类似'n'
title = "Alice in Wonderland"
print(title.split())

# 动手试一试
# 练习10-6 加法运算    练习10-7 加法计算器
print("\nGive me two number, and I'll add them.")
print("Enter 'q' to quit.")

# int('知乎')    如果int操作字符串的时候回报错ValueError，要避免这个

while True:
    first_number = input("First number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) + int(second_number)
    except ValueError:
        print("Please enter correct number.")
    else:
        print(answer)
        break

# 练习10-8 猫和狗  练习10-9 当文件不存在时静默
cats_file = 'ca1ts.txt'
dogs_file = 'dogs.txt'
try:
    with open(cats_file, encoding='utf-8') as cats:
        print(cats.read())
    with open(dogs_file, encoding='utf-8') as dogs:
        print(dogs.read())
except FileNotFoundError:
    # print("\nPlease make sure your file exists")
    pass    # 出现这个错误时直接pass跳过

# 练习10-10  常见单词
book_name = 'moby_dick.txt'     # 《白鲸》
with open(book_name, encoding='utf-8') as book:
    content = book.read()

# 把文件内容以空格为分隔存在列表内
words = content.split()
print(words)
# 计算全部有多少个字母
print(len(words))
print(content.count('the'))
# 计算字母全部小写后，含有 'the' 单词的数量，可能包括了 'then' 和 'these'
print(content.lower().count('the'))
# 计算字母全部小写后， 'the '单词的数量
print(content.lower().count('the '))
