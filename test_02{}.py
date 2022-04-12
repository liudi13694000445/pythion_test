# xiaoming = {"name": "xiaoming",
#             "age": 18,
#             "gender": True}
# # 获取长度
# print(len(xiaoming))
# # 合并字典
# # xiaoming.update(xiaohong)
# # 清空
# # xiaoming.clear()
# print(xiaoming.items())
# print(xiaoming.keys())
# print(xiaoming.values())
#
# print(xiaoming)





xiaoming = {"name":"xiaoming",
            "gender": True,
            "mobile": 1328132233}

for i in xiaoming:
    print(i, xiaoming[i])

for k in xiaoming:
    print("%s - %s" %(k,xiaoming[k]))