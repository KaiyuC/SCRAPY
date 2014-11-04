# encoding:utf-8 
import sys
import MySQLdb
from scrapy.spider import Spider
from scrapy.selector import Selector
from fish.items import FishItem

if sys.getdefaultencoding() != 'utf-8':
  reload(sys)
  sys.setdefaultencoding('utf-8')

class PigSpider(Spider):

  name = "pig" 
  allowed_domains = ['baidu.com']
  start_urls = ["http://internet.baidu.com/"]
  def parse(self, response):
    items = []
    sel = Selector(response)
    XPaths = sel.xpath("//*[@id='feeds']/div")
    filename = response.url.split(".")[-2]
    file = open("download/" + filename, "a")
    for XPath in XPaths:
      item = FishItem()
      if XPath.xpath("@id").extract():
        break
      item['title'] = XPath.xpath("h3/a/text()").extract()
      item['href'] = XPath.xpath("h3/a/@href").extract()
      item['abstract'] = XPath.xpath("div/p/text()").extract()
      item['origin'] = XPath.xpath("div/span[1]/text()").extract()
      item['time'] = XPath.xpath("div/span[2]/text()").extract()
      items.append(item)
    return items
