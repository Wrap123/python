# 3-8
# 城市列表
city = ['chongqing', 'xizang', 'zhuhai', 'suzhou', 'bali']
print(city)
# 临时正序排列
print(sorted(city))
print(city)
# 临时倒序排列
print(sorted(city, reverse=True))
print(city)

# 列表颠倒排列，不按字母顺序
city.reverse()
print(city)
city.reverse()
print(city)

# 按字母排列，永久排序
city.sort()
print(city)
city.sort(reverse=True)
print(city)

# 3-9
person = ['张三丰', '李四', '王五', '马六']
print()
print(person)
print(f"The number is {len(person)}")

print("\n" * 1)

# 3-10 第三章总结，把第三章方法全部练习一遍
''' 总结
本次练习用到的方法有：
    1、append（增加）
    2、insert（插入）
    3、del（删除-删除元素不可用）
    4、remove（删除-根据值删除）
    5、pop（删除-弹出-删除元素可用）
    6、sort（永久排正序，加reverse参数为倒序）
    7、sorted（临时排正序，加reverse参数为倒序）
    8、reverse（倒着打印-不排序）
    9、len（计算列表长度-即计算有几个元素）
'''
friends = ['aa', 'dd', 'cc', 'bb']
print(friends)
## 根据索引位置打印其内元素值
print(friends[0].title())
print(friends[-2])
print(f"{friends[1]} is 24 years old.")


# 列表元素新增//方法：append,insert
print(friends)
friends.append('ee')
print(friends)
print()

friends.insert(0, 'ff')
print(friends)

friends.insert(3, 'gg')
print(friends)

# 列表元素删除//方法：del,remove,pop
print()
del friends[0]
print(friends)

rm_friend = 'gg'
friends.remove(rm_friend)
# 或者 friends.remove('gg')
print(friends)


del_friend = friends.pop(0)
print(del_friend)
print(friends)
print(f"{del_friend.title()} is not my friend.")

# 列表元素修改
print()
friends[3] = 'aa'
print(friends)

# 排序
print()
friends.sort()
print(friends)
friends.sort(reverse=True)
print(friends)

print(sorted(friends))
print(sorted(friends, reverse=True))

print()
friends[2] = 'ee'
print(friends)
friends.reverse()
print(friends)

print(len(friends))

# 测试3.4章节中 查询不存在的索引位置 报错
print(friends[-9])