import scrapy
from scrapy.crawler import CrawlerProcess


class QuotesSpider(scrapy.Spider):
    name = "toscrape-xpath-wrong"

    start_urls = ['https://quotes.toscrape.com/page/1/']

    def parse(self, response):
        # Why is this returning only the first quote div of each page 10 times?
        for quote in response.xpath('/html/body/div/div[2]/div[1]/div'):
            yield {
                'text': quote.xpath('//span[@class="text"]/text()').get(),
                'author': quote.xpath('//small[@class="author"]/text()').get(),
                'tags': quote.xpath('//div[@class="tags"]/a[@class="tag"]/text()').getall(),
            }

        next_page = response.xpath(
            '//*[contains(concat( " ", @class, " " ), concat( " ", "next", " " ))]//a/@href').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)


# to debug in vs code::::

# process = CrawlerProcess(settings={
#     "FEEDS": {
#         "items.json": {"format": "json"},
#     },
# })
#
# process.crawl(QuotesSpider)
# process.start()


# other attempts::::

# response.xpath('descendant::div[@class="quote"]')
# response.xpath('descendan-or-self::div[@class="quote"]')
# response.xpath('//div[@class="quote"]')
# response.xpath('//div[@class="quote"]').getall()    <<< BROKE IT
#  Selector Object Reponse from the .css query:
#   response.xpath("descendant-or-self::div[@class and contains(concat(' ', normalize-space(@class), ' '), ' quote ')]")
