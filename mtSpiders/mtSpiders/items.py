# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MtspidersItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    shop_id = scrapy.Field()
    name = scrapy.Field()
    wm_poi_score = scrapy.Field()
    address = scrapy.Field()
    avg_delivery_time = scrapy.Field()
    min_price_tip = scrapy.Field()
    month_sales_tip = scrapy.Field()
    shipping_fee_tip = scrapy.Field()
    shipping_time = scrapy.Field()
    friend_status = scrapy.Field()
    phone = scrapy.Field()
    bulletin = scrapy.Field()
    province = scrapy.Field()
    city = scrapy.Field()
    country = scrapy.Field()
    longitude = scrapy.Field()
    latitude = scrapy.Field()
    is_brand = scrapy.Field()
    page = scrapy.Field()
