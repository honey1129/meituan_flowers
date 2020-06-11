# -*- coding: utf-8 -*-
import scrapy
import time
import base64,zlib
import json
from ..items import MtspidersItem
import pandas
import copy
import urllib.parse

class MtSpider(scrapy.Spider):
    name = 'mt'
    log_token = "h2ZzWAdfyjr7PkehQNUbCo4_CYUAAAAAkwoAAOM2u9IO6COrXN728ScGesWfQ8C7Y_6Ty0J7-AItg2RhrHNbBw-UPw3W2NheX9xeeg"
    visitid = "6efbd485-d25d-41f3-9b82-b3b31f0aea88"
    shop_list_url = 'https://wx-shangou.meituan.com/wxapp/v1/poi/channelpage?ui=394001276&region_id=1000110100&region_version=1588561785586'
    shop_info_url  = 'https://wx-shangou.meituan.com/wxapp/v1/poi/food?ui=394001276&region_id=1000110100&region_version=1588561785586 '
    shop_headers = {
        "Host": "wx-shangou.meituan.com",
        "Connection": "keep-alive",
        "charset": "utf-8",
        "uuid": "64ef05ca-db2c-4a9f-ae68-5d5c071493fc",
        "content-type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; SM-N960F Build/JLS36C; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.136 Mobile Safari/537.36 MicroMessenger/7.0.12.1620(0x27000C50) Process/appbrand0 NetType/WIFI Language/zh_CN ABI/arm32",
        "Accept-Encoding": "gzip,compress,br,deflate",
        "wm-ctype": "sg_wxapp",
        "Referer": "https://servicewechat.com/wx2c348cf579062e56/270/page-frame.html",
    }
    shop_list_data = {
            "page_index": "%s",
            "req_time": "%s",
            "waimai_sign": "/",
            "wm_latitude": "%s",
            "wm_longitude": "%s",
            "wm_actual_longitude": "0",
            "wm_actual_latitude": "0",
            "wm_appversion": "5.7.0",
            "wm_ctype": "wxapp",
            "wm_dtype": "OPPO R11 Plus",
            "wm_dversion": "7.0.12",
            "userToken":log_token,
            "wm_logintoken": log_token,
            "wm_uuid": "64ef05ca-db2c-4a9f-ae68-5d5c071493fc",
            "wm_visitid": visitid,
            "userid": "394001276",
            "user_id": "394001276",
            "lch": "1089",
            "open_id": "oOpUI0QHTPQHdnJf-wgeLuv_uJmI",
            "uuid": "64ef05ca-db2c-4a9f-ae68-5d5c071493fc",
            "platform": "13",
            "partner": "214",
            "riskLeve": "71",
            "category_type": "102529",
            "second_category_type": "102567",
            "_token": "",
    }
    shop_info_data = {
        "req_time":"%s",
        "waimai_sign": "/",
        "wm_poi_id":"%s",
        "wm_longitude": "%s",
        "wm_latitude": "%s",
        "wm_actual_longitude": "0",
        "wm_actual_latitude": "0",
        "wm_appversion": "5.7.0",
        "wm_ctype": "wxapp",
        "wm_dtype": "OPPO R11 Plus",
        "wm_dversion": "7.0.12",
        "wm_uuid": "64ef05ca-db2c-4a9f-ae68-5d5c071493fc",
        "wm_visitid": visitid,
        "lch": "1089",
        "open_id": "oOpUI0QHTPQHdnJf-wgeLuv_uJmI",
        "uuid": "64ef05ca-db2c-4a9f-ae68-5d5c071493fc",
        "platform": "13",
        "partner": "214",
        "riskLeve": "71",
        "_token": "",
    }
    def error(self):
        print("出错")

    def encode_first_shop_token(self,a_ts,latitude,longitude):
        def encode_first_shop_sign(a_ts,latitude,longitude):
            en_first_shop_list_data = copy.deepcopy(self.shop_list_data)
            en_first_shop_list_data.pop("_token")
            en_first_shop_list_data.pop("page_index")
            sign_string = urllib.parse.unquote(urllib.parse.urlencode(en_first_shop_list_data))
            sign = sign_string % (str(a_ts),str(latitude), str(longitude))
            encode = sign.encode()
            compress = zlib.compress(encode)
            b_encode = base64.b64encode(compress)
            shop_sign = str(b_encode, encoding='utf-8')
            return shop_sign
        token_dict = {
            'rId': 100016,
            'ts': a_ts,
            'cts': a_ts + 100 * 1000,
            'brVD': [450, 800],
            'brR': [[900, 1600], [900, 1600], 24, 24],
            'bI': ["sub_shangou/sg/pages/channel-page/channel-page", "pages/index/index"],
            'mT': [],
            'kT': [],
            'aT': [],
            'tT': [],
            'sign': encode_first_shop_sign(a_ts,latitude,longitude)}
        encode = str(token_dict).encode()
        compress = zlib.compress(encode)
        b_encode = base64.b64encode(compress)
        token = str(b_encode, encoding='utf-8')
        return token

    def encode_shop_token(self,a_ts,page,latitude,longitude):
        def encode_shop_sign(a_ts,page,latitude,longitude):
            en_shop_list_data = copy.deepcopy(self.shop_list_data)
            en_shop_list_data.pop("_token")
            sign_string = urllib.parse.unquote(urllib.parse.urlencode(en_shop_list_data))
            sign = sign_string % (str(page),str(a_ts),str(latitude), str(longitude))
            encode = sign.encode()
            compress = zlib.compress(encode)
            b_encode = base64.b64encode(compress)
            shop_sign = str(b_encode, encoding='utf-8')
            return shop_sign
        token_dict = {
            'rId': 100016,
            'ts': a_ts,
            'cts': a_ts + 100 * 1000,
            'brVD': [450, 800],
            'brR': [[900, 1600], [900, 1600], 24, 24],
            'bI': ["sub_shangou/sg/pages/channel-page/channel-page", "pages/index/index"],
            'mT': [],
            'kT': [],
            'aT': [],
            'tT': [],
            'sign': encode_shop_sign(a_ts,page,latitude,longitude)}
        encode = str(token_dict).encode()
        compress = zlib.compress(encode)
        b_encode = base64.b64encode(compress)
        token = str(b_encode, encoding='utf-8')
        return token
    # 定义base64商家详情页token值编码
    def encode_shop_info_token(self,a_ts,poi_id,latitude,longitude):
        def encode_info_sign(a_ts, poi_id, latitude, longitude):
            en_shop_info_data = copy.deepcopy(self.shop_info_data)
            en_shop_info_data.pop("_token")
            sign_string = urllib.parse.unquote(urllib.parse.urlencode(self.shop_info_data))
            sign = sign_string % (str(a_ts), str(latitude), str(longitude), str(poi_id))
            # 二进制编码
            encode = sign.encode()
            # 二进制压缩
            compress = zlib.compress(encode)
            # base64编码
            b_encode = base64.b64encode(compress)
            # 转为字符串
            info_sign = str(b_encode, encoding='utf-8')
            return info_sign
        token_dict = {
            'rId': 100016,
            'ts': a_ts,
            'cts': a_ts + 100 * 1000,
            'brVD': [450, 800],
            'brR': [[900, 1600], [900, 1600], 24, 24],
            'bI': ["sub_shangou/sg/pages/channel-page/channel-page", "pages/index/index"],
            'mT': [],
            'kT': [],
            'aT': [],
            'tT': [],
            'sign': encode_info_sign(a_ts,latitude,longitude,poi_id,)}
        encode = str(token_dict).encode()
        compress = zlib.compress(encode)
        b_encode = base64.b64encode(compress)
        token = str(b_encode, encoding='utf-8')
        return token

    #重写父类方法
    def start_requests(self):
        geo_data = json.load(open(r'C:\Users\honey\PycharmProject\mtSpiders\mtSpiders\spiders\geoinfo-all.json', 'r', encoding='utf-8'))
        for city in geo_data[4]["districts"]:
            for country in city["districts"]:
                item = MtspidersItem()
                item['page'] = "0"
                item['province'] = geo_data[4]['name']
                item['city'] = city['name']
                item['country'] = country["name"]
                coordinate_list = country["center"].split(",")
                item['longitude'] = str(int(float(coordinate_list[0])*1000000))
                item['latitude'] = str(int(float(coordinate_list[1])*1000000))
                shop_first_list_data = copy.deepcopy(self.shop_list_data)
                shop_first_list_data.pop('page_index')
                shop_first_list_data['req_time'] = str(int(time.time() * 1000))
                shop_first_list_data['wm_longitude'] = item['longitude']
                shop_first_list_data['wm_latitude'] = item['latitude']
                shop_first_list_data['_token'] = self.encode_first_shop_token(int(shop_first_list_data['req_time']),item['latitude'],item['longitude'])
                print("开始爬取"+item['province']+item['city']+item['country']+"的第0页商家信息")
                yield scrapy.FormRequest(url=self.shop_list_url,formdata=shop_first_list_data, headers= self.shop_headers,callback=self.parse,dont_filter = True,meta={'item': copy.deepcopy(item)},errback=self.error)

    #定义列表页解析
    def parse(self, response):
        poilist_data = json.loads(response.text)
        poilist = poilist_data['data']['poilist']
        poi_has_next_page = poilist_data['data']['poi_has_next_page']
        item = response.meta['item']
        if poilist_data['msg'] == "成功":
            for poi in poilist:
                item['shop_id'] = str(poi['id'])
                item['name'] = poi['name']
                item['wm_poi_score'] = str(poi['wm_poi_score'])
                item['address'] = poi['address']
                item['is_brand'] = poi['poi_type_icon_type']
                if item['is_brand'] == 2:
                    item['is_brand'] = "是"
                else:
                    item['is_brand'] = "否"
                item['avg_delivery_time'] = poi['avg_delivery_time']
                item['min_price_tip'] = poi['min_price_tip']
                item['month_sales_tip'] = poi['month_sales_tip']
                item['shipping_fee_tip'] = poi['shipping_fee_tip']
                item['shipping_time'] = poi['shipping_time']
                shop_info_data = copy.deepcopy(self.shop_info_data)
                shop_info_data["req_time"] = str(int(time.time() * 1000))
                shop_info_data["wm_longitude"] = item['longitude']
                shop_info_data["wm_latitude"] = item['latitude']
                shop_info_data["wm_poi_id"] = item['shop_id']
                shop_info_data["_token"] = self.encode_shop_info_token(int(shop_info_data["req_time"]),item['latitude'],item['longitude'],item['shop_id'])
                print("开始爬取第"+item['page']+"页的"+item['province']+item['city']+item['country']+"的%s商家信息" % item['shop_id'])
                yield scrapy.FormRequest(url=self.shop_info_url,formdata=shop_info_data, headers=self.shop_headers,callback=self.info_parse,meta={'item': copy.deepcopy(item)},dont_filter = True,errback=self.error)
                # poi_has_next_page = requests.post(url=self.shop_list_url, data=shop_list_data,headers = self.shop_headers,verify= False).json()['data']['poi_has_next_page']
            if poi_has_next_page:
                item['page'] = str(int(item['page']) + 1)
                shop_list_data = copy.deepcopy(self.shop_list_data)
                shop_list_data['req_time'] = str(int(time.time() * 1000))
                shop_list_data['wm_longitude'] = item['longitude']
                shop_list_data['wm_latitude'] = item['latitude']
                shop_list_data['page_index'] = item['page']
                shop_list_data['_token'] = self.encode_shop_token(int(shop_list_data['req_time']), item['page'],
                                                                  item['latitude'], item['longitude'])
                print("开始爬取" + item['province'] + item['city'] + item['country'] + "的第%s页商家信息" % item['page'])
                yield scrapy.FormRequest(url=self.shop_list_url, formdata=shop_list_data, headers=self.shop_headers,
                                         callback=self.parse, dont_filter=True, meta={'item': copy.deepcopy(item)},
                                         errback=self.error)
        else:
            print("此次请求出错！")


    #定义详情页解析
    def info_parse(self,response):
        info =json.loads(response.text)
        if info['msg'] == "成功":
            info_data = info['data']
            item = response.meta['item']
            try:
                item['friend_status'] = info_data['friend_status']
            except:
                item['friend_status'] = " "
            else:
                item['friend_status'] = info_data['friend_status']
            try:
                item['phone'] = info_data['poi_info']['phone_list'][0] if len(info_data['poi_info']['phone_list'])== 1 else '、'.join(info_data['poi_info']['phone_list'])
            except:
                item['phone'] = " "
            else:
                item['phone'] = info_data['poi_info']['phone_list'][0] if len(info_data['poi_info']['phone_list'])== 1 else '、'.join(info_data['poi_info']['phone_list'])
            # item['bulletin'] = info_data['poi_info']['bulletin']
            print("第"+item['page']+"页的"+item['province']+item['city']+item['country']+"的%s商家数据已经爬取完成" % item['shop_id'])
            yield item
        else:
            print("此次请求出错！")



