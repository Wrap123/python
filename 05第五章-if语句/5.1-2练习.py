# 练习5-1 条件测试
car = 'subaru'
print("Is car == 'subaru'? I predict True.")

num = 10
num_1 = 5
print(num_1 == 10)
num_2 = 8
print(num_2 < num)
num_3 = 10
print(num_3 == num)
print(num_3 >= num)
num_4 = 22
print(num_4 > num)
print(num_4 >= num)
print(num_4 == num)
print(num_4 != num)

# 练习5-2 更多条件测试
print()
## 1）
string_1 = 'aaa'
print('bbb' == string_1)
print('bbb' != string_1)
## 2)
string_2 = 'CCC'
print('ccc' == string_2)
print('ccc' == string_2.lower())
## 3)
#### 略，5-1练习中测试过
## 4）
string_3 = 'AAA'
if (string_3.lower() == string_2) and (string_3 != string_2):
    print("Successful!")
if (string_3.lower() == string_2) or (string_3 != string_2):
    print("Fail!")
## 5-6)
num_list = [1, 2, 3, 4]
print(5 in num_list)
print(2 in num_list)
print(7 not in num_list)
