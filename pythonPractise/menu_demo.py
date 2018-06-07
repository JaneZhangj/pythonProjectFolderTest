def menu_choose(num1, num2, option):
    """
    菜单选择四则运算函数
    :return:
    """
    result = 0
    if option == 1:
         result = num1 + num2
    if option ==2:
        result = num1 - num2
    if option == 3:
         result = num1 * num2
    if option == 4:
         result = num1 / num2
    print("运算结果为：" + '\n')
    print(result)


if __name__ == '__main__':
    print("1、加法运算" + '   ' + "2、减法运算" + '   '"3、乘法运算" + '   '"4、除法运算" + '   ')
    print("请输入想做操作的两个数：" + '\n')
    a = int(input())
    b = int(input())
    c = int(input("请输入想做的运算操作：" + '\n'))
    menu_choose(a, b, c)
