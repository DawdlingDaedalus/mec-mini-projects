import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes_start_urls"

    start_urls = [
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/',
        'http://quotes.toscrape.com/page/3/'
    ]

    def parse(self, response):
        page = response.url.split("/")[-2]
        print("oddball...")
        print(response)
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
