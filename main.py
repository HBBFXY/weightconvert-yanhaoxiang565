weight_input=input()
if weight_input[-2:] in ["kg","KG"]: 
    pound=(eval(weight_input[0:-2]))*2.2046
    print("对应的英制重量为{:.3f}磅".format(pound))
elif weight_input[-2:] in ["pd","PD"]:
    kilogram=(eval(weight_input[0:-2]))*0.4535
    print("对应的公制重量为{:.3f}公斤".format(kilogram))
else:
    print("输入格式错误")
