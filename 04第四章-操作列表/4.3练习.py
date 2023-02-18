# 练习4-3：数到20，使用一个for循环打印数1~20（含）
for num in range(1,21):
    print(num)


# 练习4-4：一百万，创建一个包函数1~100 0000的列表，再使用for循环给打印出来，如果输出时间太长，可以ctrl+c打断
num_2 = []
for value in range(1, 100001):
    num_2.append(value)
print(num_2)

# 练习4-5：一百万求和，使用min和max函数确认上一个列表是否是从1开始到1000000结束，最后用sum函数求和
print(min(num_2))
print(max(num_2))
print(sum(num_2))

# 练习4-6：打印1-20之内的奇数，用for循环打印
num_3 = []
for value_2 in range(1, 21, 2):
    num_3.append(value_2)
print(num_3)
## 不用for循环，可以这样
num_4 = list(range(1, 21, 2))
print(num_4)
## 或者
num_5 = [value_3 * 1 for value_3 in range(1, 21, 2)]
print(num_5)

# 练习4-7：创建3~30之间能被3整除的数，用for循环打印
num_6 = []
for value_4 in range(3, 31, 3):
    num_6.append(value_4)
print(num_6)
## 或者
num_7 = list(range(3, 31, 3))
for n in num_7:
    print(n)

# 练习4-8：立方，一个数乘三次为立方，例如2的立方为2 ** 3，创建一个列表，包含1~10的立方，用for循环打印
num_8 = []
for value_5 in range(1, 11):
    num_8_1 = value_5 ** 3
    print(num_8_1)
    num_8.append(num_8_1)
print(num_8)

# 练习4-9：用列表解析的方式去实现4-8
num_9 = [value_6 ** 3 for value_6 in range(1, 11)]
print(num_9)
for i in num_9:
    print(i)


