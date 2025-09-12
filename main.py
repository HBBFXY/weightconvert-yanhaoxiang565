weight = input().strip()
unit = weight[-2:].lower()
num_part = weight[:-2]

try:
    num = float(num_part)
    if unit == "kg":
        pound = num * 2.2046
        print(f"对应的英制重量为{pound:.3f}磅")
    elif unit == "pd":
        kilogram = num / 2.2046
        print(f"对应的公制重量为{kilogram:.3f}公斤")
    else:
        print("输入格式错误")
except (ValueError, IndexError):
    print("输入格式错误")
