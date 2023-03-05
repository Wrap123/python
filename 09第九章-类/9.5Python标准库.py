# 导入随机数模块
import random
# print(random.randint(1, 6))


# 动手试一试
# 练习9-13 骰子
class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        print(random.randint(1, self.sides))


dice_num = Die()
dice_num.roll_die()
# 创建一个10面和20面的骰子，分别掷10次
n = 1
while n <= 10:
    dice_num = Die(10)
    dice_num.roll_die()
    n += 1

n = 1
while n <= 10:
    dice_num = Die(20)
    dice_num.roll_die()
    n += 1

# 练习9-14 彩票
info_pool = ['111', '222', '333', '444', '555', '666', '77', '88', '99', '0', 'a', 'b', 'c', 'd', 'e']
prize_pool = []
for i in range(4):
    num = random.choice(info_pool)
    prize_pool.append(num)
print(f"When you have these numbers, you win the lottery:{prize_pool}")

# 练习9-15  彩票分析
# 确定中奖数字，创建一个存储每次随机数的列表，不断随机选择数，直到中奖为止。再打印一条消息说明中奖数字和循环了多少次
prize_pool = ['222', '666', 'a', 'c']
my_ticket = []
while True:
    num = random.choice(info_pool)
    # for num in nums:   因为这个玩意，搞个死循环出来了，，，排查了好一会
    my_ticket.append(num)
    if num in prize_pool:
        # print(nums)
        print(f"\nCongratulations, your num is {num},you won the lottery")
        break
    else:
        print("Sorry,come on next time")
sum_num = len(my_ticket)
print(f"This time we have {sum_num} executions")

