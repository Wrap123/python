# 列表和字典互相嵌套使用
# 示例
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