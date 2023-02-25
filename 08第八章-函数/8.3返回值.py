# 返回值，使用return语句将函数返回的值返回到调用函数的代码行

# 8.3.2让实参变成可选的（非必填项）
def get_formatted(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()


musician = get_formatted('john', 'hooker', 'lee')
print(musician)

musician = get_formatted('john', 'hooker')
print(musician)

# 8.3.3返回字典


def build_person(fist_name, last_name, age=None):
    """返回一个字典，其中包含有关一个人的信息"""
    person = {'fist': {fist_name}, 'last': {last_name}}
    if age:
        person['age'] = age
    return person


musician = build_person('jimi', 'hendrix')
print(musician)

musician = build_person('jimi', 'hendrix', '23')
print(musician)

# 8.3.4 结合使用while循环


def get_formatted_name(first_name, last_name):
    """返回整洁的姓名"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()


while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit.)")

    f_name = input("First name:")
    if f_name == 'q':
        break
    l_name = input("Last name:")
    if l_name == 'q':
        break
    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}")


# 动手试一试
# 练习8-6 城市名
def city_country(city_name, county_name):
    full_name = f"\"{city_name}, {county_name}\""
    return full_name.title()


musician = city_country('santiago', 'chile')
print(musician)

# 练习8-7 专辑


def make_album(singer_name, album_name, song_num=None):
    albums_info = {'singer_name': singer_name, 'album_name': album_name}
    if song_num:
        albums_info['song_number'] = song_num
    return albums_info


musician = make_album('周杰伦', '稻花香')
print(musician)
musician = make_album('张杰', '逆战', '3')
print(musician)


# 练习8-8 用户的专辑


def make_album(singer_name, album_name, song_num=None):
    albums_info = {'singer_name': singer_name, 'album_name': album_name}
    if song_num:
        albums_info['song_number'] = song_num
    return albums_info


while True:
    print("\nPlease enter your favorite singer and his or her album")
    print("If you want to quit, you can enter 'q' on any time")
    s_name = input("Singer name:")
    if s_name == 'q':
        break
    a_name = input("Album name:")
    if a_name == 'q':
        break

    album_info = make_album(s_name, a_name)
    print(album_info)
