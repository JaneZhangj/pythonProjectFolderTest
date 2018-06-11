import requests
import json


def request_get_xml_demo():
    """
    requests的get方法演示，不带参数，返回的是html/XML
    """
    url = 'http://www.baidu.com'
    res = requests.get(url)
    print(res.url)
    print(res.status_code)


def requests_get_json_demo():
    """
    request的获取json的方法
    :return:
    """
    url = 'https://api.github.com/events'
    res = requests.get(url)
    print(res.url)
    print(res.status_code)

    res_str = res.text
    res_list = json.loads(res_str)
    print(len(res_list))
    for my_dict in res_list:
        id = my_dict['id']
        print(id)


if __name__ == '__main__':
    # request_get_xml_demo()
    requests_get_json_demo()
