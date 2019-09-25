import requests, re
from lxml import etree
import pymongo
import time
time.sleep(4)

client = pymongo.MongoClient('localhost', 27017)
# # 激活Mongodb
woaiwojia = client['woaiwojia']
# # 给数据库命名
woaiwojia_D = woaiwojia['woaiwojia_D']



# 构建代理
proxy = {
    'http': 'http://alice:123456@120.78.166.84:6666',
    'https': 'http://alice:123456@120.78.166.84:6666'
}

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    # "Accept-Language":"zh-CN,zh;q=0.9",
    "Cache-Control": "no-store",
    "Connection": "keep-alive",
    "Cookie": "_Jo0OQK=EA921672E15E2497FE2BA7AC79FF30A6E4EC2CC2BD9634DDA83582231724C9DD6EE1D4FEC658DC169CC917CC56AD98F0BBB1B124C88A37D65B1E68808FC26C54DF3DE8682CA7D10E3B498FB9E3C853EFEE298FB9E3C853EFEE215D8BEE34E43E5C0GJ1Z1aw==; PHPSESSID=g8s730jie4tlhi9o68trfskvc4; yfx_c_g_u_id_10000001=_ck19010213052218931818993447338; yfx_mr_n_10000001=baidu%3A%3Amarket_type_ppzq%3A%3A%3A%3A%3A%3A%3A%3A%3A%3A%25E6%25A0%2587%25E9%25A2%2598%3A%3Abj.5i5j.com%3A%3A%3A%3A%3A%3A%25E5%25B7%25A6%25E4%25BE%25A7%25E6%25A0%2587%25E9%25A2%2598%3A%3A%25E6%25A0%2587%25E9%25A2%2598%3A%3A160%3A%3Apmf_from_adv%3A%3Abj.5i5j.com%2F; yfx_mr_f_n_10000001=baidu%3A%3Amarket_type_ppzq%3A%3A%3A%3A%3A%3A%3A%3A%3A%3A%25E6%25A0%2587%25E9%25A2%2598%3A%3Abj.5i5j.com%3A%3A%3A%3A%3A%3A%25E5%25B7%25A6%25E4%25BE%25A7%25E6%25A0%2587%25E9%25A2%2598%3A%3A%25E6%25A0%2587%25E9%25A2%2598%3A%3A160%3A%3Apmf_from_adv%3A%3Abj.5i5j.com%2F; yfx_key_10000001=; _ga=GA1.2.1797379118.1546405523; _gid=GA1.2.2075208290.1546405523; Hm_lvt_94ed3d23572054a86ed341d64b267ec6=1546405524; zufang_BROWSES=42236503; domain=bj; yfx_f_l_v_t_10000001=f_t_1546405521969__r_t_1546405521969__v_t_1546415891471__r_c_0; _gat=1; Hm_lpvt_94ed3d23572054a86ed341d64b267ec6=1546416144",
    "Host": "bj.5i5j.com",
    # "Upgrade-Insecure-Requests":"1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36",
}

base_url = 'https://bj.5i5j.com/zufang/changpingqu/n%d/'

for i in range(33, 36):
    url = base_url % i
    # url = 'https://bj.5i5j.com/zufang/changpingqu/n1/'
    response = requests.get(url, headers=headers, proxies=proxy)
    hrml_str = response.text
    # hrml_str=response.content
    # print(hrml_str)
    html_ele = etree.HTML(hrml_str)
    # print(url)
    print('正在保存第一页' + str(i) + '.............')
    li_list = html_ele.xpath('//div[@class="list-con-box"]/ul/li')
    print(li_list)
    # with open('woaiwojia.html','wb') as f:
    #     f.write(hrml_str)
    xiangqing_url = 'https://bj.5i5j.com'
    for li_ele in li_list:
        try:
            data = {
                "标题：": li_ele.xpath('./div[2]/h3/a')[0].text,
                "户型": li_ele.xpath('./div[2]/div[1]/p/text()')[0].replace("\n", "").replace("\t","").replace(" ","").split("·")[0],
                "面积": li_ele.xpath('./div[2]/div[1]/p/text()')[0].split("·")[1],
                "朝向": li_ele.xpath('./div[2]/div[1]/p/text()')[0].split("·")[2],
                "楼层": li_ele.xpath('./div[2]/div[1]/p/text()')[0].split("·")[3],
                "装修": li_ele.xpath('./div[2]/div[1]/p/text()')[0].split("·")[4],
                "小区": li_ele.xpath('./div[2]/div[1]/p[2]/a/text()')[0],
                "价格": li_ele.xpath('./div[2]/div[1]/div[1]/p/strong/text()')[0],
            }
            woaiwojia_D.insert_one(data)
            print(data)

        except:
            pass
