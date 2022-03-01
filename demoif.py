money = 1000
s = int(input('请输入取款金额'))
if money>=s:
    money= money-1
    print('取款成功，余额为',money)
    if s>100:
        print('金额大于100')
    elif s<100:
        print('金额小于100')
    else:
        pass
#     pass 什么都不做 ，用在if语句的条件执行体，for-in 语句的循环体，定义函数时的函数体
else:
    print('取款失败')