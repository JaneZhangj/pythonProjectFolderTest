import re

def hump2underline(hunp_str):
    '''
    驼峰形式字符串转成下划线形式
    :param hunp_str: 驼峰形式字符串
    :return: 字母全小写的下划线形式字符串
    '''
    # 匹配正则，匹配小写字母和大写字母的分界位置
    p = re.compile(r'([a-z]|\d)([A-Z])')
    # 使用正则分组的后向引用
    sub = re.sub(p, r'\1_\2', hunp_str).lower()
    return sub

def underline2hump(underline_str):
    '''
    下划线形式字符串转成驼峰形式
    :param underline_str: 下划线形式字符串
    :return: 驼峰形式字符串
    '''
    # 使用匿名函数
    sub = re.sub(r'(_\w)', lambda x: x.group(1)[1].upper(), underline_str)
    return sub


def test_hump2underline():
    # 供测试用的一些驼峰命名形式的字符串
    attr1 = 'PersonNamePattern'
    attr2 = 'IPv6Address'
    attr3 = 'personDetailInfo'
    attr4 = 'CCTV'
    attr5 = 'CCTVAddress'
    attr6 = 'name'
    attrs = [attr1, attr2, attr3, attr4, attr5, attr6]

    # 遍历attrs进行匹配和转换，把驼峰形式的字符串转成下划线形式
    for attr in attrs:
        sub = hump2underline(attr)
        print(sub)


def test_underline2hump():
    attr1 = 'person_name_pattern'
    attr2 = 'ipv6_address'
    attr3 = 'person_detail_info'
    attr4 = 'cctv'
    attr5 = 'cctvaddress'
    attr6 = 'name'
    attrs = [attr1, attr2, attr3, attr4, attr5, attr6]

    for attr in attrs:
        sub = underline2hump(attr)
        print(sub)


if __name__ == '__main__':
    test_hump2underline()
    test_underline2hump()
