xiaoming = {"name": "xiaoming","age": 18,"gender": True,"height": 1.75,"weight": 80}

# 取值
print(xiaoming["name"])

# 增加
xiaoming["class"] = 1
# 修改
xiaoming["class"] = 2
# 删除
xiaoming.pop("class")

print(xiaoming)
