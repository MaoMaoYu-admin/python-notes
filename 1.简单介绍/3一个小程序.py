#温度转换

#具体理解参照4.py

#接受一个温度的输入，判断温度标准
#换算为另一个标准
#输出结果
#摄氏度C，华氏度F
#C=(F-32)/1.8
#F=C*1.8+32

T = input("输入带符号的温度值：")
if T[-1]in['F','f']:
    C = (eval(T[0:1])-32)/1.8
    print(str(C)+"℃")
elif T[-1]in['C','c']:
    F = (eval(T[0:1]))*1.8+32
    print(str(F)+"F")
else:
    print("格式错误")
