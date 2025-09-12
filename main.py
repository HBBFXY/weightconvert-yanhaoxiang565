weight_str = input().strip()
lower_weight_str = weight_str.lower()
if lower_weight_str.endswith("kg"):
    num_part = lower_weight_str[:-2]
    if num_part:
        kg_value = float(num_part)
        pound = kg_value * 2.2046
        print("对应的英制重量为{:.3f}磅".format(pound))
    else:
        print("输入格式错误")
elif lower_weight_str.endswith("pd"):
    num_part = lower_weight_str[:-2]
    if num_part:
        pd_value = float(num_part)
        kilogram = pd_value / 2.2046
        print("对应的公制重量为{:.3f}公斤".format(kilogram))
    else:
        print("输入格式错误")
else:
    print("输入格式错误")
