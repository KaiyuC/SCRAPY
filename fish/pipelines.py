# encoding:utf-8
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import MySQLdb
import MySQLdb.cursors 
from scrapy import log 
from twisted.enterprise import adbapi  

class FishPipeline(object):

    def __init__(self):
      self.dbpool = adbapi.ConnectionPool('MySQLdb',  
        host = '192.168.1.237',
        db = 'kyee_python',  
        user = 'fb',  
        passwd = '123',  
        cursorclass = MySQLdb.cursors.DictCursor,  
        charset = 'utf8',  
        use_unicode = False  
      )
    def process_item(self, item, spider):
      query = self.dbpool.runInteraction(self.do_insert, item)
      return item
      
    def do_insert(self, db, item):
      insertSql = " INSERT INTO `baidu_news` SET `atitle` = '%s', `aabstract` = '%s', `ahref` = '%s', `afrom` = '%s', `atime` = '%s' " %(item['title'][0], item['abstract'][0], item['href'][0], item['origin'][0], item['time'][0])
      db.execute(insertSql)
      print "================" + item['title'][0]  + "=================="
      pass

