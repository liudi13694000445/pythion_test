def multiple_table():
    i = 1
    while i < 10:
        o = 1
        while o <= i:
            print("%d * %d = %d" % (o, i, o * i), end="\t")
            o += 1
        print("")
        i += 1
