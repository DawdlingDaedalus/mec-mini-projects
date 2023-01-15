import scrapy


class QuotesSpider(scrapy.Spider):
    name = "toscrape-xpath"

    start_urls = ['https://quotes.toscrape.com/page/1/']

    def parse(self, response):

        for x in range(10):
            yield {
                'text': response.xpath('/html/body/div/div[2]/div[1]/div[' + str(x+1) + ']//span[@class="text"]/text()').get(),
                'author': response.xpath('/html/body/div/div[2]/div[1]/div[' + str(x+1) + ']//small[@class="author"]/text()').get(),
                'tags': response.xpath('/html/body/div/div[2]/div[1]/div[' + str(x+1) + ']//div[@class="tags"]/a[@class="tag"]/text()').getall(),
            }

        next_page = response.xpath(
            '//*[contains(concat( " ", @class, " " ), concat( " ", "next", " " ))]//a/@href').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
