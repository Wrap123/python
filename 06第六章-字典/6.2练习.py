# 练习
alien_0 = {'color': 'green', 'point': 5}
new_points = alien_0['point']
print(f"You just earned {new_points} points!")

# 新增键值对
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# 修改字典中的值
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(alien_0)
# 修改speed速度为fast
alien_0['speed'] = 'fast'
# 向右移动外星人
# 根据当前速度确定将外星人向右移动多远
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # 或者fast，移动很快，增量为3
    x_increment = 3
# 新位置为旧位置加移动距离
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New x_position: {alien_0['x_position']}")

# 删除键值对，del语句
# 必须指定字典名和要删除的键
alien_0 = {'color': 'green', 'points': 5}
print(f"\n{alien_0}")
del alien_0['points']
print(alien_0)

# 换行字典
aa = {
    'bb': 2,
    'cc': 1,
}
print(aa)

# 使用get()来访问值
'''
使用格式  get('key1', 'key2')
key1：参数一用于指定键，必填项
key2：指定键不存在时返回的值，可选项，不填写时返回为None
作用：如果指定获取的键不存在，直接['']访问会报错，使用get()访问可以指定在获取键值不存在时，返回一个设置的默认值
'''
alien_0 = {'color': 'green', 'speed': 'slow'}
# 使用[]直接获取值，会报错KeyError
# print(alien_0['points'])
# 使用get()获取值
print(alien_0.get('points', 'No point value assigned'))
print(alien_0.get('points',))

# 动手试一试
# 练习 6-1 使用一个字段存储一个人的信息
miss_person = {'first_name': 'z', 'last_name': 'mx', 'age': '25', 'city': 'henan'}
message = f"\nShe is {miss_person['first_name']}{miss_person['last_name']},she comes from {miss_person['city']}," \
          f"and she is {miss_person['age']} years old.\n"
print(message)

# 6-2 喜欢的数
friends_favorite_num = {
    'John': 2,
    'Mari': 6,
    'Tom': 8,
    'Jerry': 5,
    'Me': 9,
}
for friends in friends_favorite_num.keys():
    if friends.lower() == 'john':
        print(f"John is favorite number is {friends_favorite_num['John']}.")
    elif friends.lower() == 'mari':
        print(f"Mari is favorite number is {friends_favorite_num['Mari']}.")
    elif friends.lower() == 'tom':
        print(f"Tom is favorite number is {friends_favorite_num['Tom']}.")
    elif friends.lower() == 'jerry':
        print(f"Jerry is favorite number is {friends_favorite_num['Jerry']}.")
    else:
        print(f"My favorite number is {friends_favorite_num['Me']}.")

# 练习6-3 词汇表
data = {
    '列表': '存储对象的对象',
    'python': '一个编程语言',
    'linux': '操作系统',
    '字典': '键值存储的数据结构',
    '元组': '其内的数据不会被改变'
}
print(data)
# 学完下一节后的回顾练习
for name, info in data.items():
    print(f"{name} is a {info}")