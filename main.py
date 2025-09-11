#weightConvert.py
weight_str=input()
if weight_str[-2:]=="kg":
    pound=float(weight_str[0:-2])*2.2046
    print("对应的英制重量为{:.3f}磅".format(pound))
elif weight_str[-2:]=="pd":
    kilogram=float(weight_str[0:-2])/2.2046
    print("对应的公制重量为{:.3f}公斤".format(kilogram))
else:
    print("输入格式错误“）
    
