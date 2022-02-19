import scrapy


class BookItem(scrapy.Item):
    # Primary Fields
    title = scrapy.Field()
    price = scrapy.Field()
    image_url = scrapy.Field()
    details_page_url = scrapy.Field()

    # ###### Only used in development phase ######
    # Custom Fields
    # url = scrapy.Field()
    # spider = scrapy.Field()
    # date = scrapy.Field()
