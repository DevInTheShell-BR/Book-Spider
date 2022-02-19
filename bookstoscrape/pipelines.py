# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class BookstoscrapePipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        fields = ['title', 'price', 'image_url', 'details_page_url']
        for field in fields:
            if adapter.get(field):
                adapter[field] = adapter[field][0]

        return item
