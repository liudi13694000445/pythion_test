gl_list = [1, 2, 5, 3]
gl_list.sort(reverse=True)
print(gl_list)


def print_info(name, title=True, gender=True):
    """

    :param title:
    :param name: 姓名
    :param gender: 性别，默认为男生
    """
    gender_text = "男生"
    if not gender:
        gender_text = "女生"
    print("%s 是 %s" % (name, gender_text))


print_info("小明",True)
print_info("小妹", False)
print_info("老王")
print_info("小美",False)