# 函数range() ，打印从第一个值到第二个值中间的数

## 打印1-5之间的数
for value in range(1, 5):
    print(value)

print()

## 打印0-6之间的数
for value_1 in range(0, 6):
    print(value_1)

# 使用range()创建数字列表，嵌套list函数去转换为列表
numbers = list(range(1, 5))
print(numbers)

# 使用函数range()时，指定步长n，即打印出的每两个值之间的间隔，或者理解为从初始值一直加n
## eg：只打印1-10之间的偶数
even_number = list(range(2, 10, 2))
print(even_number)

# 解析：创建一个空列表，然后把1-10赋值给value，再将value的平方值 赋值给square，再把square追加在squares列表中
squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
print(squares)
## 也可以，，省略square变量
squares_1 = []
for value in range(1, 11):
    squares_1.append(value ** 2)
print(squares_1)

# 对数字列表执行简单的统计计算
digits = [1, 2, 3, 4, 5]
print(min(digits))
print(max(digits))
print(sum(digits))

# 4.3.4 列表解析  （将for循环合在一行代码内）
squares_2 = [value_1 ** 2 for value_1 in range(1, 11)]
print(squares_2)
# eg:
test = [aa /2 for aa in range(1, 5)]
print(test)
