#weightConvert.py
weight_str=input().strip()
if weight_str.endswith("kg"):
    kg_value=float(weight_str[:-2])
    pound=kg_value*2.2046
    print("对应的英制重量为{: .3f}磅".format(pound))
elif weight_str.endswith("pd"):
    pd_value=float(weight_str[:-2])
    kilogram=pd_value/2.2046
    print("对应的公制重量为{: .3f}公斤".format(kilogram))
else:
    print("输入格式错误")
