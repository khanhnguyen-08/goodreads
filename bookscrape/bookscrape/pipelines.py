# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo

class BookscrapePipeline:

    def __init__(self):
        # MongoDB connection
        self.conn = pymongo.MongoClient(
            'localhost',
            27017
        )
        db = self.conn['books']
        self.collection = db['books_tb']

    def process_item(self, item, spider):

        # set default values for each feature
        item.setdefault('title', 'Null')
        item.setdefault('author', 'Null')
        item.setdefault('num_ratings', 'Null')
        item.setdefault('num_reviews', 'Null')
        item.setdefault('avg_rating', 'Null')
        item.setdefault('num_pages', 'Null')
        item.setdefault('language', 'Null')
        item.setdefault('publish_date', 'Null')
        item.setdefault('first_publish_date', 'Null')
        item.setdefault('series', 'Null')
        item.setdefault('characters', 'Null')
        item.setdefault('places', 'Null')
        item.setdefault('awards', 'Null')
        item.setdefault('genres', 'Null')
        item.setdefault('isbn13', 'Null')
        item.setdefault('isbn', 'Null')
        item.setdefault('rated_5', 'Null')
        item.setdefault('rated_4', 'Null')
        item.setdefault('rated_3', 'Null')
        item.setdefault('rated_2', 'Null')
        item.setdefault('rated_1', 'Null')
        item.setdefault('description', 'Null')

        self.collection.insert(dict(item))
        # return item

