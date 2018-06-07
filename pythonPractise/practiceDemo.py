def file_io_demo():
    # 写文件
    str_temp = ''
    input_file = open('filepackage\input.txt', mode='r', encoding='utf-8')
    for line in input_file.readlines():
        str_temp += line
    print(str_temp)
    # 读取结果写入文件
    output_file = open('filepackage\output.txt', mode='w', encoding='utf-8')
    output_file.writelines(str_temp)
    for i in range(50):
        output_file.writelines(str(i) + '\n')
    output_file.writelines("这是输出到文件的操作")

    input_file.close()
    output_file.close()


def egg_tric():
    # 鸡蛋拿取函数
    x = range(50000)
    for egg_total in x:
        if (egg_total % 4) != 1:
            continue
        if (egg_total % 5) != 4:
            continue
        if (egg_total % 6) != 3:
            continue
        if (egg_total % 7) != 5:
            continue
        if (egg_total % 8) != 1:
            continue
        if (egg_total % 9) != 0:
            continue
        print(egg_total)
        break
    # 将结果输入到文件中保存
    output_file = open('filepackage\output.txt', mode='w', encoding='utf-8')
    output_file.writelines('最小符合条件鸡蛋数' + '\n')
    output_file.writelines(str(egg_total))
    output_file.close()


if __name__ == '__main__':
    # file_io_demo()
    # str = 'helloworld'
    # for item in str:
    #     print(item)
    egg_tric()
    print("测试添加4444")
