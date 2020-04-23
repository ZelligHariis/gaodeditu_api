#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
key = '951b60a07574968b827be9fe5a77a45b'


# In[2]:


#地理编码API 方法:GET
#address为结构化地址信息:省份＋城市＋区县＋城镇＋乡村＋街道＋门牌号码
#可选参数 city

def dilibianma_api(address=str):
    key_last = '&key=' + key
    address_last = 'address=' + address
    bianma_url = 'https://restapi.amap.com/v3/geocode/geo?' + address_last + key_last
    r = requests.get(bianma_url)
    return r.json()

#测试函数(南京大学为例)
dilibianma_api(address='南京大学')


# In[3]:


#路径规划API 方法:GET
#北京市东城区正义路2号:116.413384,39.910925
#北京地坛公园:116.421358,39.959903
#origin为出发地，destination为目的地

def lujinguihua_api(origin=str,destination=str):
    key_last = '&key=' + key
    destination_last = '&destination=' + destination
    origin_last = 'origin=' + origin
    lujin_url = 'https://restapi.amap.com/v3/direction/walking?' + origin_last + destination_last + key_last
    r = requests.get(lujin_url)
    return r.json()

#测试函数
lujinguihua_api(origin='116.413384,39.910925',destination='116.421358,39.959903')


# In[4]:


#行政区域查询API 方法:GET
#城市地理编码的高德官方下载地址：https://lbs.amap.com/api/webservice/download
#南京市 adcode:320100  citycode:025
#keyword为查询关键字（行政区名称、citycode、adcode）


def xingzhengquyuchaxun_api(keywords=str,subdistrict=str):
    key_last = '&key=' + key
    subdistrict_last = '&subdistrict=' + subdistrict
    keywords_last = 'keywords=' + keywords
    xingzheng_url = 'https://restapi.amap.com/v3/config/district?' + keywords_last + subdistrict_last + key_last
    r = requests.get(xingzheng_url)
    return r.json()

#测试函数，以南京为例
xingzhengquyuchaxun_api(keywords = '320100', subdistrict = '1')


# In[5]:


#搜索POI API 方法:GET
#keywords：多个关键字用“|”分割，types：分类代码 或 汉字（若用汉字，请严格按照附件之中的汉字填写）
#这里选取了南京餐饮服务为例

def sousuopoi_api(keyword=str,types=str):
    types_last = '&types=' + types
    keyword_last = 'keywords=' + keyword
    key_last = '&key=' + key
    poi_url = 'https://restapi.amap.com/v3/place/text?' + keyword_last + types_last + key_last + '&citylimit=true'
    r = requests.get(poi_url)
    return r.json()

sousuopoi_api(keyword="南京大学",types='餐饮相关')


# In[6]:


#ip查询 API 方法:GET

def ipchaxun_api(ip=str):
    key_last = '&key=' + key
    ip_last = "ip_last=" + ip
    ip_url = 'https://restapi.amap.com/v3/ip?' + ip_last + key_last
    r = requests.get(ip_url)
    return r.json()

ipchaxun_api(ip='210.21.79.245')


# In[7]:


# 静态地图 API 方法:GET

def jingtaimap_api(location=str,zoom=int):
    zoom_last = "&zoom=" + str(zoom)
    location_last = "location=" + location
    key_last = '&key=' + key
    map_url = "https://restapi.amap.com/v3/staticmap?" + location_last + zoom_last + key_last
    r = requests.get(map_url)
    return r.url

jingtaimap_api(location="32.0712290800,118.7999725300",zoom=16)


# In[8]:


# 天气查询 API   方法:GET

def tianqichaxun_api(city=int):
    city_last = "city=" + str(city)
    key_last = '&key=' + key
    tianqi_url = 'https://restapi.amap.com/v3/weather/weatherInfo?' + city_last + key_last
    r = requests.get(tianqi_url)
    return r.json()

tianqichaxun_api(city=320100)


# In[9]:


# 输入提示 API  方法:GET

def shurutishi_api(keywords=str,city=int):
    key_last = '&key=' + key
    keywords_last = "keywords=" + keywords
    city_last = "&city=" + str(city)
    data = "&citylimit=true"
    shuru_url = 'https://restapi.amap.com/v3/assistant/inputtips?' + keywords_last + data + city_last + key_last 
    r = requests.get(shuru_url)
    return r.json()

shurutishi_api(keywords='美食',city=320100)


# In[15]:


def jiaotong_api(rectangle=str,level=int):
    rectangle_last = "rectangle=" + rectangle
    key_last = '&key=' + key
    level_last = "&level=" + str(level)
    jiaotong_url = "https://restapi.amap.com/v3/traffic/status/rectangle?" + rectangle_last + level_last + key_last
    r = requests.get(jiaotong_url)
    return r.json()

jiaotong_api(rectangle="116.351147,39.966309;116.357134,39.968727",level=3)


# In[24]:


import json
def dili_api(name=str,center=str,radius=int,valid_time=None,repeat="Mon,Tues,Wed,Thur,Fri,Sat,Sun"):
    headers = {
        "content-type":"application/json"
    }
    body= {
        "name": name,
        "center": center,
        "radius": str(radius),
        "enable": "true",
        "valid_time": valid_time,
        "repeat": repeat,
        }
    key_last = 'key=' + key
    dili_url = "https://restapi.amap.com/v4/geofence/meta?" + key_last
    r = requests.post(dili_url,data=json.dumps(body),headers=headers)
    return r.json()

dili_api("Lking","115.672126,38.817129",1000)


# In[ ]:




