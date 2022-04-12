# ！ /c/Users/liudi-hj.HF/AppData/Local/Microsoft/WindowsApps/python3

import test_tools

while True:
    # 显示名片管理系统菜单
    # test_tools.show()
    action_str = input("请输入您要选择的功能：")
    if action_str in ["1", "2", "3"]:
        if action_str == "1":
            print("您选择的功能是【新建名片】")
            test_tools.new_card()
        elif action_str == "2":
            print("您选择的功能是【显示名片】")
            test_tools.show_all()
        elif action_str == "3":
            print("您选择的功能是【查询名片】")
            test_tools.show_one()
    elif action_str == "":
        print("请您输入选项后在试")
    elif action_str == "0":
        print("欢迎您下次使用【名片系统】，再见！")
        break
    else:
        print("您输入的选项错误，请您重新输入")
