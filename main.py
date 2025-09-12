weight = input().strip()
unit = weight[-2:].lower()
num = weight[:-2]
try:
    value = float(num)
    if unit == "kg":
        print(f"对应的英制重量为{value * 2.2046:.3f}磅")
    elif unit == "pd":
        print(f"对应的公制重量为{value / 2.2046:.3f}公斤")
    else:
        print("输入格式错误")
except ValueError:
    print("输入格式错误")
