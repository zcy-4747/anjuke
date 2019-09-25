# !/usr/bin/python
# -*- coding:utf-8 -*-
# author:joel 18-6-5

import random
import re
import time
import pymongo
import requests


client = pymongo.MongoClient('localhost', 27017)
# # 激活Mongodb
woaiwojia_sh = client['woaiwojia_sh']
# # 给数据库命名
woaiwojia_Dates_sh = woaiwojia_sh['woaiwojia_Dates_sh']

# """
# 13014 按每页30个 共有434页
# """


start_url = 'https://m.5i5j.com/sh/zufang/index-baoshanqu-n{}'
# 只添加'x-requested-with' 可能获取不到json数据，可以直接把整个请求头加上
headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'max-age=0',
    'cookie': 'PHPSESSID=g8s730jie4tlhi9o68trfskvc4; yfx_c_g_u_id_10000001=_ck19010213052218931818993447338; yfx_mr_n_10000001=baidu%3A%3Amarket_type_ppzq%3A%3A%3A%3A%3A%3A%3A%3A%3A%3A%25E6%25A0%2587%25E9%25A2%2598%3A%3Abj.5i5j.com%3A%3A%3A%3A%3A%3A%25E5%25B7%25A6%25E4%25BE%25A7%25E6%25A0%2587%25E9%25A2%2598%3A%3A%25E6%25A0%2587%25E9%25A2%2598%3A%3A160%3A%3Apmf_from_adv%3A%3Abj.5i5j.com%2F; yfx_mr_f_n_10000001=baidu%3A%3Amarket_type_ppzq%3A%3A%3A%3A%3A%3A%3A%3A%3A%3A%25E6%25A0%2587%25E9%25A2%2598%3A%3Abj.5i5j.com%3A%3A%3A%3A%3A%3A%25E5%25B7%25A6%25E4%25BE%25A7%25E6%25A0%2587%25E9%25A2%2598%3A%3A%25E6%25A0%2587%25E9%25A2%2598%3A%3A160%3A%3Apmf_from_adv%3A%3Abj.5i5j.com%2F; yfx_key_10000001=; _ga=GA1.2.1797379118.1546405523; _gid=GA1.2.2075208290.1546405523; Hm_lvt_94ed3d23572054a86ed341d64b267ec6=1546405524; _Jo0OQK=16F68CB7BCA391B90B75F00710F4BB844C9DD8183610B48AFB501ED29BA07AEEF965EA425ABAEDCD6184E3887013A2EFE6F4184B7177FEE38CA47E86A79957A9AC2185939B4256E961CE797D4FCFA22AA8EE797D4FCFA22AA8EA35FE3B83147D6AE4C815B8EE842241AGJ1Z1ew==; zufang_BROWSES=42236503; yfx_f_l_v_t_10000001=f_t_1546405521969__r_t_1546405521969__v_t_1546415891471__r_c_0; domain=cd; ershoufang_BROWSES=35264716; _gat=1; Hm_lpvt_94ed3d23572054a86ed341d64b267ec6=1546417291',
    'pragma': 'no-cache',
    'referer': 'https://m.5i5j.com/sh/zufang/index',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}
proxy = {
    'http': 'http://alice:123456@120.78.166.84:6666',
    # 'https': 'http://alice:123456@120.78.166.84:6666'
}

def gethouselist():
    """ 5i5j 上海租房 """
    for page in range(1, 38):
        print("-----------------------" + str(page) + "------------------")
        # r = requests.get(start_url.format(page), headers=headers)
        r = requests.get(start_url.format(page), headers=headers, proxies=proxy)
        result = r.json()
        houses = result['houses']
        # print(r.json())
        for i in range(0, len(houses)):
            # print(houses[i]['_source']['housesid'])
            # house_id = houses[i]['_source']['housesid']
            data ={
            "house_url":  'https://m.5i5j.com/sh/zufang/{}.html'.format(houses[i]['_source']['housesid']),
            "house_jpg ": houses[i]['_source']['imgurl'],
            "标题 ": houses[i]['_source']['housetitle'],
            "类型 ": houses[i]['_source']['bedroom_cn'] + houses[i]['_source']['livingroom_cn'] + \
                         houses[i]['_source']['toilet_cn'],
            "面积":  houses[i]['_source']['area'],
           " 朝向 ": houses[i]['_source']['heading'],
            "楼层 ": houses[i]['_source']['floorPositionStr'] + '/' + str(houses[i]['_source']['houseallfloor']),
            "装修 ": houses[i]['_source']['decoratelevel'],
            "地址": str(houses[i]['_source']['sqname']) + ' ' + str(houses[i]['_source']['communityname']),
            "发放时间":houses[i]['_source']['firstuptimestr'],
            "价格 ": houses[i]['_source']['price'],
            "出租方式 ":houses[i]['_source']['rentmodename'],
            "支付形式 ": houses[i]['_source']['pay'],
            "房子所在地区 ": houses[i]['_source']['qyname'],
            "房子亮点 ":','.join(houses[i]['_source']['tagwall']),
            "地铁路线 ": ','.join(houses[i]['_source']['subwaylines']),
            "距离地铁距离 ": houses[i]['_source']['traffic'],
            "房源质量 ":houses[i]['_source']['house_quality']}
            # print(house_id, house_url, house_jpg, house_title, house_type, house_buildarea, house_heading,
            #       house_floor, house_decoratelevel, house_place, house_firstuptime, house_price, house_renttype,
            #       house_paytype, house_area, house_tags, house_subwaylines, house_traffic, house_quality)
            woaiwojia_Dates_sh.insert_one(data)
            print(data)
        time.sleep(random.randint(0, 2))


if __name__ == '__main__':
    """ 上海 """
    gethouselist()
