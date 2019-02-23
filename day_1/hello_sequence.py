# coding:utf-8

# 根据年份，记录生肖

zodiac = "鼠牛虎兔龙蛇马羊猴鸡狗猪"

zodiac2 = "猴鸡狗猪鼠牛虎兔龙蛇马羊"

# print(zodiac[0])
# print(zodiac[0:4])
# print(zodiac[-1])

year = 2020

print(zodiac2[year%12])