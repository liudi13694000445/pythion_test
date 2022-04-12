card_list = []


def show():  # 显示名片
    print("欢迎使用【名片管理系统】\n"
          "1、新建名片\n"
          "2、显示名片\n"
          "3、查询名片\n"
          "0、退出系统")
    print("*"*50)


def new_card():
    print("新增名片")
    name_str = input("请输入名片姓名：")
    age_str = input("请输入名片性别：")
    mobile_str = input("请输入名片电话：")
    mail_str = input("请输入名片邮箱：")
    card_dict = {"name": name_str, "age": age_str, "mobile": mobile_str, "mail": mail_str}
    card_list.append(card_dict)
    # print(card_list)
    print("添加【 %s 】的名片成功" % name_str)


def show_all():
    print("显示全部名片")
    if len(card_list) == 0:
        print("当前没有名牌你，请先新建一个名片")
        return
    print("姓名\t\t性别\t\t电话\t\t邮箱")
    for all_name in card_list:
        n = all_name["name"]
        a = all_name["age"]
        mo = all_name["mobile"]
        ma = all_name["mail"]
        print("%s\t\t%s\t\t%s\t\t%s" % (n, a, mo, ma))


def show_one():
    print("查询名片")
    find_name = input("请输入您要查询的名片姓名：")
    for card_dict in card_list:
        if card_dict["name"] == find_name:
            print("姓名\t\t性别\t\t电话\t\t邮箱")
            print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"], card_dict["age"], card_dict["mobile"], card_dict["mail"]))

            deal_card(card_dict)
            break
    else:
        print("抱歉！没有找到%s的名片" % find_name)


def deal_card(find_name):
    print(find_name)
    action_str = input("请输入要执行的操作（1修改，2删除，0返回）：")
    if action_str == "1":
        find_name["name"] = input_info(find_name["name"], "姓名")
        find_name["age"] = input_info(find_name["age"], "年龄")
        find_name["mobile"] = input_info(find_name["mobile"], "电话")
        find_name["mail"] = input_info(find_name["mail"], "邮箱")
        print("修改名片成功")
    elif action_str == "2":
        card_list.remove(find_name)
        print("删除名片成功")


def input_info(dict_value, tit_message):
    """

    :param dict_value:原有值
    :param tit_message:输入的新值
    :return:如果输入内容就返回内容，否则返回原有的值
    """
    # 提示用户输入内容
    result_str = input(tit_message)
    # 针对用户的输入进行判断，如果输入了内容，直接返回结果
    if len(result_str) > 0:
        return result_str
    # 如果mei有输入，直接返回字典中原有的值
    else:
        return dict_value
