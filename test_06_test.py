def print_line(title,num):
    print(title * num)


def jj(i,n):
    """打印多行分隔符
    :param i: 分隔符
    :param n: 分隔符的数量
    """
    row = 1
    while row < 6:
        print_line(i,n)
        row += 1


jj(8,3)


