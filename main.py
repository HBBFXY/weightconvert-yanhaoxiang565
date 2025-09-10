# 获取用户输入的重量及单位
weight_input = input()
# 提取数字部分和单位部分
num = float(weight_input[:-2])
unit = weight_input[-2:]
# 定义转换系数
kg_to_pd = 2.2046
if unit == "kg":
    # 千克转磅
    result = num * kg_to_pd
    print(f"对应的英制重量为{result:.3f}磅")
elif unit == "pd":
    # 磅转千克
    result = num / kg_to_pd
    print(f"对应的公制重量为{result:.3f}公斤")

