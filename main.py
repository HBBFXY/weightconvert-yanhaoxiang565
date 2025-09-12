weight = input().strip()
unit = weight[-2:].lower()
num_part = weight[:-2]
try:
    num = float(num_part)
    if unit == "kg":
        pound = num * 2.2046
        print("对应的英制重量为{:.3f}磅".format(pound))
    elif unit == "pd":
        kilogram = num / 2.2046
        print("对应的公制重量为{:.3f}公斤".format(kilogram))
    else:
        print("输入格式错误")
except (ValueError, IndexError):
    print("输入格式错误")
