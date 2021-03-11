# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo

class BookscrapePipeline:

    def __init__(self):
        self.conn = pymongo.MongoClient(
            'localhost',
            27017
        )
        db = self.conn['books']
        self.collection = db['books_tb']

    def process_item(self, item, spider):
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

        self.collection.insert(dict(item))
        # print("5*: "+str(item['rated_5'][0])+"\n4*: "+ str(item['rated_4'][0]) +"\n3*: "+ str(item['rated_3'][0]) +"\n2*: "+ str(item['rated_2'][0]) +"\n1*: "+ str(item['rated_1'][0]))
        return item

