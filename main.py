weight = input().strip()
# 提取单位（最后两位）
unit = weight[-2:]
# 提取数值部分
num_part = weight[:-2]

try:
    # 将数值部分转换为浮点数
    num = float(num_part)
    # 千克转磅（单位为kg或KG）
    if unit == "kg" or unit == "KG":
        pound = num * 2.2046
        print(f"对应的英制重量为{pound:.3f}磅")
    # 磅转千克（单位为pd或PD）
    elif unit == "pd" or unit == "PD":
        kilogram = num / 2.2046
        print(f"对应的公制重量为{kilogram:.3f}公斤")
    # 单位不匹配
    else:
        print("输入格式错误")
except (ValueError, IndexError):
    # 数值部分无法转换为浮点数或者输入字符串长度不足等情况
    print("输入格式错误")
