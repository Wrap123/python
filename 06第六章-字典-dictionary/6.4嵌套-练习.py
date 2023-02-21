# 列表和字典互相嵌套使用
# 列表内嵌套字典（可存储多条信息）
aliens = []
# 循环创建30个外星人字典
for alien_number in range(30):
    new_alien = {'color': 'green', 'point': 5, 'speed': 'slow'}
    aliens.append(new_alien)
# 判断前三个的外星人颜色并修改其键值信息
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['point'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['point'] = 15
# 打印前5个
for alien in aliens[:5]:
    print(alien)
# 汇总外星人总数
print(f"\nTotal number of aliens: {len(aliens)}")

# 字典内嵌套列表（一个键可以对应多个值）
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'shell']
}
for name, languages in favorite_languages.items():
    if len(languages) == 1:
        print(f"{name.title()}'s favorite languages is:")
    else:
        print(f"{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")

# 字典中嵌套字典
users = {
    'john': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'tom': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}
for username, userinfo in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{userinfo['first']} {userinfo['last']}"
    location = userinfo['location']

    print(f"Full_name: {full_name}")
    print(f"Location: {location}")

# 动手试一试
# 6-7 人们
people = [
    {'name': 'john', 'age': 18},
    {'name': 'tom', 'age': 20},
    {'name': 'mari', 'age': 19},
]
for users in people:
    print(f"\nName: {users['name']}")
    print(f"Age: {users['age']}")

# 6-8 宠物
animal_dog_dictionary = {
    'type': 'dog',
    'master': 'john',
}
animal_cat_dictionary = {
    'type': 'cat',
    'master': 'mari',
}

animal_list = []
aa = "去掉这行，就会弹出列表设计太冗余，提示可以直接在空列表内填值，but我就要这样写，练习嘛"
animal_list.append(animal_cat_dictionary)
animal_list.append(animal_dog_dictionary)
print(animal_list)
for message in animal_list:
    print(f"Type: {message['type']}")
    print(f"Master: {message['master']}")

# 6-9 喜欢的地方
favorite_places = {
    'john': ['hn', 'sh'],
    'tom': ['bj', 'smx'],
}
for name, place in favorite_places.items():
    print(f"{name.title()} is like {place[0]} and {place[1]}.")

# 6-10 喜欢的数
friends_favorite_num = {
    'John': [2, 3],
    'Mari': [6, 5],
    'Tom': [8, 0],
    'Jerry': [5, 7],
}
for name, number in friends_favorite_num.items():
    print(f"\n{name.title()}'s favorite number is:")
    for num in number:
        print(f"\t{num}")

# 6-11 城市
cities = {
    'henan': {
        'country': 'china',
        'population': '10000000',
        'fact': 'poor',
    },
    'shanghai': {
        'country': 'china',
        'population': '5000000',
        'fact': 'money',
    },
}
for city, info in cities.items():
    print(f"\nCity: {city.title()}")
    print(f"Country: {info['country'].title()}")
    print(f"Population: {info['population']}")
    print(f"Fact: {info['fact'].title()}")

# ps：越来越难了。。。测试代码越来越长
