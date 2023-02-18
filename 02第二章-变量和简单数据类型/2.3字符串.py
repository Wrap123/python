print("hello world")

# 使用方法修改字符串的大小写
name = 'tom locy'
# 将首写字母大写
print(name.title())
# 将全部字母大写
print(name.upper())
# 将全部字母小写
print(name.lower())

# 在字符串中使用变量
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)
print(f"Hello, {full_name.title()}!")
message = f"Hello, {full_name.title()}"
print(message)

# 注：f字符串是python3.6后引入的，之前版本可以用format()方法
full_name_2 = "{} {}".format(first_name, last_name)
print(full_name_2)

# 或者用”+“号来添加变量
message = "hello world..."
print(message)
print('message is ' + message.title())


# 使用制表符\t或换行符\n来添加空白
print("python")
print("\tpython")
print("Languages: \n\t1:Python\n\t2:C\n\t3:JavaScript")

# 删除空白（rstrip()方法是删除右边空白，lstrip()是左边空白，strip()是两边空白）
favorite_language = ' python '
print(favorite_language)

favorite_language_r = favorite_language.rstrip()
print(favorite_language_r)

favorite_language_l = favorite_language.lstrip()
print(favorite_language_l)

favorite_language_all = favorite_language.strip()
print(favorite_language_all)

