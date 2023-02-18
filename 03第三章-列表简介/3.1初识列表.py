# 列表是一系列按铁定顺序排列的元素组成
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

# 访问列表元素,打印第一个元素（python中，第一个元素是从0开始的，即索引为0）
## 显示第一个元素值
print(bicycles[0])
print(bicycles[1].title())

## 显示最后一个元素值（倒数第二个是-2，以此类推）
print(bicycles[-1])

# 提取列表内元素，使用f方法创建一条消息
message = f"My first bicycles is {bicycles[1]}."
print(message)

# 练习
name = ['ZhangSan', 'LiSi', 'WangWu', 'MaLiu']
print(name)
print(name[0])
## 祝福短语
wish1 = f"I hope {name[0]} will be happy every day!"
print(wish1)
wish2 = f"I hope {name[1]} will be happy every day!"
print(wish2)

## 常用的交通工具
transportation = ['bus', 'subway', 'car', 'plane']
commute = f"I often take the {transportation[1]} to work."
print(commute)

## 喜欢的颜色
colors = ['blue', 'green', 'yellow', 'red']
favorite_color = f"{colors[0].title()} is my favorite color."
print(favorite_color)