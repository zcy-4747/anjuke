from bs4 import BeautifulSoup
import requests
import pymongo
import time
import pandas as pd


time.sleep(1)

# client = pymongo.MongoClient('localhost', 27017)
# # 激活Mongodb
# anjukes = client['anjukes']
# # 给数据库命名
# anjuke_Dates = anjukes['anjuke_Dates']
headers = {
    'User-Agent': 'ozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
}
def get_link_form(page):
    urls = []
    for i in range(page):
        url = "https://zhanjiang.anjuke.com/sale/p"+str(i)+"/"
        wb_data = requests.get(url, headers=headers)
        soup = BeautifulSoup(wb_data.text,'lxml')
        usr_list = soup.select(' div.house-details > div.house-title > a')
        for urlList in usr_list:
            urls.append(urlList.get('href').split('?')[0])
        # return  urls

    print("成功")
    print(len(urls))
    return urls

def get_item_info():
    urls = get_link_form(50)
    try:
        for urla in urls:
            wb_data = requests.get(urla,headers = headers)
            soup = BeautifulSoup(wb_data.text,'lxml')
            data ={
                '标题' : soup.title.text,
                '总价': soup.select('div.basic-info.clearfix > span.light.info-tag > em')[0].get_text().split()[0]+"万",
                '所属小区':soup.select('div.houseInfo-content > a')[0].get_text(),
                '房屋户型':soup.select(" div.houseInfo-content")[1].get_text().replace("\n", "").replace("\t","").replace(" ",""),
                '房屋单价':soup.select("div.houseInfo-content")[2].get_text(),
                '所在位置':soup.select("div.houseInfo-content ")[3].get_text().replace('\n','').replace('－','').replace('\t','')[2::],
                '建筑面积':soup.select("div.houseInfo-content")[4].get_text(),
                '参考首付':soup.select("div.houseInfo-content")[5].get_text().split()[0],
                '建造年代':soup.select("div.houseInfo-content")[6].get_text().split()[0],
                '房屋朝向': soup.select("div.houseInfo-content")[7].get_text(),
                '房屋类型':soup.select("div.houseInfo-content")[9].get_text(),
                '所在楼层': soup.select("div.houseInfo-content")[10].get_text(),
                '装修程度':soup.select("div.houseInfo-content")[11].get_text(),
                '房本年限':soup.select("div.houseInfo-content")[12].get_text(),
                '唯一住房':soup.select("div.houseInfo-content")[13].get_text(),
            }
            # anjuke_Dates.insert_one(data)
            print(data)
    except:
        pass

get_item_info()