weight = input().strip()
# 提取单位（最后两位）
unit = weight[-2:]
# 提取数值部分
num_part = weight[:-2]

try:
    num = float(num_part)
    # 严格匹配单位为"kg"（千克）或"PD"（磅）
    if unit == "kg":
        pound = num * 2.2046
        print("对应的英制重量为{:.3f}磅".format(pound))
    elif unit == "PD":
        kilogram = num / 2.2046
        print("对应的公制重量为{:.3f}公斤".format(kilogram))
    else:
        print("输入格式错误")
except (ValueError, IndexError):
    print("输入格式错误")
