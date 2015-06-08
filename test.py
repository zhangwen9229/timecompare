# -*-coding:utf-8 -*-
import os
key = "ss    "
print(key)

print(key.strip(" "))

dict_test = dict(key="5",key1="6")

print(dict_test.get("key3"))
data = [
            {"title": "test_221", "description": "test_des", "image": "test_image", "url": "test_url"},
            {"title": "test_222", "description": "test_des", "image": "test_image", "url": "test_url"}
        ]
pic_data = filter(lambda m: m.get("title") == "test_221", data)

print(pic_data[0])
print(len(pic_data))

import time


def make_time(time_str):
    u"""
    将字符串转成时间
    :param time_str:时间格式 %Y-%m-%d %H:%M:%S' 如：2015-05-10 06:26:50
    :return:
    """
    return time.mktime(time.strptime(time_str, '%Y-%m-%d %H:%M:%S'))

articles = [{'timeoutOn': "2015-05-10 06:26:50"},
            {'timeoutOn': "2015-05-09 06:26:50"}]

print(make_time(articles[0]["timeoutOn"]))
print(make_time(articles[1]["timeoutOn"]))
articles.sort(
    lambda x, y: cmp(make_time(x["timeoutOn"]), make_time(y["timeoutOn"])))
print(articles)
