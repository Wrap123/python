# 3-4 嘉宾名单
person = ['张三', '李四', '王五', '马六']
print(person)

# 3-5 修改嘉宾名单
no_come_person = person.pop(0)
message = f"\n{no_come_person} is can not come"
print(message)
## 新增人员
print(person)
person.insert(0, '张三丰')
print(person)
print(f"Welcome {person[0]} to the party!")
print(f"Welcome {person[1]} to the party!")
print(f"Welcome {person[2]} to the party!")
print(f"Thank you {person[3]} for comming to this party!")

# 3-6 添加嘉宾
print("\nOh, i find a bigger dining table, let we go!")
person.insert(0, '新增1')
person.insert(3, '新增2')
person.append('新增3')
print(person)
print(f"Let us welcome {person[0]},{person[1]},{person[2]},{person[3]},{person[4]},{person[5]} and {person[6]} to our "
      f"party!")    # 达到长度限制，再用一个f方法来打印

# 3-7 缩减名单
print("\nBecause no lag table，so i only invite two people.")
person.pop(0)
person.pop()
person.pop()
person.pop()
person.pop()
print(f"New staff list:{person}")
print(f"Hello, {person[0]} and {person[1]}, you are still here!")
## 删除名单
del person[0: 2]
print(person)