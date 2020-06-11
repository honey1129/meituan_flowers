# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import csv
class MtspidersPipeline(object):
    fp = None
    def open_spider(self, spider):
        self.fp = open('flowers_data1.csv', 'w', encoding='utf_8_sig', newline="")
        writer = csv.writer(self.fp)
        writer.writerow(["shop_id","name" ,"wm_poi_score","is_brand","avg_delivery_time","min_price_tip",
                         "month_sales_tip","shipping_fee_tip","shipping_time","friend_status","phone","address","province","city","country","page"])

    def process_item(self, item, spider):
        writer = csv.writer(self.fp)
        writer.writerow( [item['shop_id'],item['name'],item['wm_poi_score'],item['is_brand'], item['avg_delivery_time'], item['min_price_tip'],
                          item['month_sales_tip'],item['shipping_fee_tip'],item['shipping_time'],item['friend_status'], item['phone'],item['address'],item["province"],item["city"],item["country"],item["page"]])

        return item

    def close_spider(self, spider):
        self.fp.close()
