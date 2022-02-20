from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.loader import ItemLoader
from itemloaders.processors import MapCompose
from bookstoscrape.items import BookItem


class BookSpider(CrawlSpider):
    name = 'book'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']

    rules = (
        Rule(LinkExtractor(
            restrict_xpaths='(//ul[@class="nav nav-list"]/li/ul/li)'),
            callback='parse_item',
            follow=True),

        Rule(LinkExtractor(
            deny=('books.toscrape.com/catalogue/page*'),
            restrict_xpaths='//li[@class="next"]'),
            callback='parse_item',
            follow=True)
    )

    def parse_item(self, response):
        """ This function parses books from categories pages

        @url http://books.toscrape.com
        @returns items 1 20
        @scrapes title price
        @scrapes image_url details_page_url
        """
        for item in response.xpath('//article'):
            book_loader = ItemLoader(
                item=BookItem(),
                response=response,
            )
            book_loader.add_value('title', item.xpath('./h3/a/@title').get())

            book_loader.add_value('price', item.xpath(
                './div/p[@class="price_color"]/text()').get(),
                MapCompose(lambda i: i.replace(',', ''), float), re='[,.0-9]+')

            book_loader.add_value('image_url', response.urljoin(item.xpath(
                './div[@class="image_container"]/a/img/@src').get()))

            book_loader.add_value('details_page_url', response.urljoin(
                item.xpath(
                    './div[@class="image_container"]/a/@href').get()))

            yield book_loader.load_item()
