# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import mysql.connector

class BookscrapePipeline:

    def __init__(self):
        self.create_connection()
        self.create_table()
    
    def create_connection(self):
        self.conn = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            passwd = 'Mysql05gd!',
            database = 'mybooks'
        )
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS books_tb""")
        self.curr.execute("""create table books_tb(
                            id text,
                            title text,
                            author text,
                            num_ratings text,
                            num_reviews text,
                            num_pages text,
                            avg_rating text,
                            language text,
                            publish_date text,
                            first_publish_date text,
                            series text,
                            characters text,
                            places text,
                            awards text,
                            genres text,
                            isbn13 text,
                            isbn text,
                            rated_5 text,
                            rated_4 text,
                            rated_3 text,
                            rated_2 text,
                            rated_1 text
                            )""")
    def store_db(self, item):
        self.curr.execute("""INSERT INTO books_tb VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
                            (item['bookId'][0],
                            item['title'][0],
                            item['author'],
                            item['num_ratings'][0],
                            item['num_reviews'][0],
                            item['num_pages'][0],
                            item['avg_rating'][0],
                            item['language'][0],
                            item['publish_date'][0],
                            item['first_publish_date'][0],
                            item['series'][0],
                            item['characters'][0],
                            item['places'][0],
                            item['awards'][0],
                            item['genres'][0],
                            item['isbn13'][0],
                            item['isbn'][0],
                            item['rated_5'][0],
                            item['rated_4'][0],
                            item['rated_3'][0],
                            item['rated_2'][0],
                            item['rated_1'][0]
                            ))
        self.conn.commit()

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

        self.store_db(item)
        # print(item['bookId'],item['title'], item['author'], item['num_ratings'],
        #     item['num_reviews'], item['num_pages'], item['avg_rating'], item['language'], item['publish_date'],
        #     item['first_publish_date'], item['series'], item['characters'], item['places'],
        #     item['awards'], item['genres'], item['isbn13'], item['isbn'], item['ratings'])

        # print("5*: "+str(item['rated_5'][0])+"\n4*: "+ str(item['rated_4'][0]) +"\n3*: "+ str(item['rated_3'][0]) +"\n2*: "+ str(item['rated_2'][0]) +"\n1*: "+ str(item['rated_1'][0]))

        # return item

