# 输出0-100
# i = 0
# while i <= 100:
#     print(i)
#     i += 1

# 求1-100的和
i = 0
o = 0
while i < 101:
    o += i
    i += 1
print(o)


# 请输入一组整数，由小到大输出
numm = input("请输入一组整数")
numm = [numm]
print(numm.sort())
