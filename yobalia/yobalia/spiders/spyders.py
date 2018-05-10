# -*- coding: utf-8 -*-
# import sys
# reload(sys)
# sys.setdefaultencoding('utf8')

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spider import CrawlSpider, Rule
from ..items import YobaliaItem

class YobaliaSpider(CrawlSpider):

    name = 'yobalia'
    pagina = 0
    allowed_domains = ['yobalia.com/es/candidato'] 
    start_urls = ['https://www.yobalia.com/es/ofertas-de-empleo/page/1/region/ES-GR',
                  'https://www.yobalia.com/es/ofertas-de-empleo/page/2/region/ES-GR',
                  'https://www.yobalia.com/es/ofertas-de-empleo/page/3/region/ES-GR',
                  'https://www.yobalia.com/es/ofertas-de-empleo/page/4/region/ES-GR',
                  'https://www.yobalia.com/es/ofertas-de-empleo/page/5/region/ES-GR']

#    rules = {
#        Rule(LinkExtractor(allow=(), restrict_xpaths=('//div[@class="pagination margin_top_10 text_right"]/ul/li/a[@href]',)), callback='parse_start_url', follow=True)
#    }

#    def start_requests(self):

#        for u in self.start_urls:
#            yield scrapy.Request(u, callback=self.parse_start_url, dont_filter=True)


    def parse_start_url(self, response):

        for a in response.xpath('//tr[@class="row_deal"]'):
            item = YobaliaItem()
            item['oferta'] = a.xpath('normalize-space(.//td[2]/a/text())').extract_first()
            item['ciudad'] = a.xpath('normalize-space(.//td[2]/div[1]/span[1]/text())').extract_first()
            item['texto'] = a.xpath('normalize-space(.//td[2]/div[2]/text())').extract_first()
            item['jornada'] = a.xpath('normalize-space(.//td[2]/div[3]/span[1]/text())').extract_first()
            yield item



#        next_page = response.xpath('.//div[@class="pagination margin_top_10 text_right"]/ul/li/a/@href').extract()

#        if next_page:
 #           next_href = next_page[0]
  #          print('AAAAAAAAAAAAAA')
   #         print(next_href)
    #        next_page_url = 'https://www.yobalia.com/es/ofertas-de-empleo/page/' + next_href + '/region/ES-GR'
     #       request = scrapy.Request(url=next_page_url)
      #      yield request

