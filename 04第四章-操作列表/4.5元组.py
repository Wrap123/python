"""元组(tuple)
概念：列表内元素是可以修改变动的，而不能修改其中元素值的列表叫做“元组”
用法：使用（）来标识，定义元组后，用索引来访问，和访问列表元素一样

注：严格来说，元组是由逗号标识的，括号只是让元组看起来更整洁，如果元组内只包含一个元素，那么后边也要加逗号
"""
# 定义一个大小不会改变的矩形，可以将其长度和宽度存储在一个元组内，保证其大小不会变动
dimensions = (200, 50)
print(dimensions)
print(dimensions[0])
print(dimensions[1])
# dimensions[0] = 100  #不能被修改
# 单元素值的元组，要注意最后加逗号，自动生成的元组可能会出现该情况
my_t = (2,)
print(my_t)

# 遍历元组内所有值（和列表一样）
for i in dimensions:
    print(i)

# 修改元组变量
## 可以给存储元组的变量重新赋值，达到修改的目的
print("\nOriginal dimensions:")
for dimension in dimensions:
    print(dimension)
dimension = (400,100)
print("Modified dimensions:")
for new_dimension in dimensions:
    print(new_dimension)

# 练习
## 4-13：自助餐
simple_foods = ('aaa', 'bbb', 'ccc', 'ddd', 'eee')
print(f"\n{simple_foods}")
### 1)
for food in simple_foods:
    print(food)
### 2)
# simple_foods[0] = 'ff'  # 不能直接修改
### 3）
simple_foods = ('aaa', 'bbb', 'ccc', 'qqq', 'xxx')
print(simple_foods)
for new_foods in simple_foods:
    print(new_foods)
