def print_line(title, num):
    """打印单行

    :param title: 需要打印的分隔符
    :param num: 数量
    """
    print(title * num)


def jj(title, num):
    """打印多行分隔符

    :param num: 数量
    :param title: 分隔符
    """
    row = 1
    while row < 6:
        print_line(title, num)
        row += 1


name = "刘花花"
