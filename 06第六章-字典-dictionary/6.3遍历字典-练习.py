"""
快速过一下本节使用方法
items()：遍历字典中所有信息
keys()：遍历字典中的所有键
values()：遍历字典中的所有值
"""
user_0 = {
    'username': 'fermi',
    'first': 'enrico',
    'last': 'fermi',
}
# 获取用户字典中的所有信息
for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

# 用上一节“喜欢的数”来做测试
friends_favorite_num = {
    'John': 2,
    'Mari': 6,
    'Tom': 8,
    'Jerry': 8,
    'Hub': 9,
}
for name, num in friends_favorite_num.items():
    print(f"{name.title()} is favorite number is {num}.")

# 遍历所有键
for name in friends_favorite_num.keys():
    print(name)
# 遍历所有值
for num in friends_favorite_num.values():
    print(num)

# 可对遍历的键进行排序
for name in sorted(friends_favorite_num.keys()):
    print(f"\n{name.title()}, thank you for taking the poll.")

# 对遍历的键或者值，进行去重，剔除重复项，使用集合(set)
favorite_languages = {
    'John': 'python',
    'Mari': 'C',
    'Tom': 'java',
    'Jerry': 'C',
}
print(f"\nThe following languages hava been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())

# 集合和字典都是用{}来定义的，但是集合内不是键值方式存储，而且不会打印重复值
languages = {'python', 'python', 'java'}
print(languages)

# 动手试一试
# 练习 6-5
Rivers = {
    'nile': 'egypt',
    'HuangHe': 'asia',
    'ChangJiang': 'china'
}
for river, area in Rivers.items():
    print(f"The {river.title()} runs through {area.title()}.")
for area in Rivers.values():
    print(area)

# 6-6
favorite_languages = {
    'John': 'python',
    'Mari': 'C',
}
person = ['mari', 'tom']
for friend in person:
    if friend.title() in favorite_languages.keys():
        print(f"{friend.title()},thank you for filling in.")
    else:
        print(f"Hello {friend.title()}, please fill it out, thank you.")