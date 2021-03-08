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
                            title text,
                            author text,
                            num_ratings text,
                            num_reviews text,
                            num_pages text 
                            )""")
    def store_db(self, item):
        self.curr.execute("""insert into books_tb values (%s,%s,%s,%s,%s)""", (
            item['bookTitle'],
            item['author'],
            item['num_ratings'],
            item['num_reviews'],
            item['num_pages']
        ))
        self.conn.commit()

    def process_item(self, item, spider):
        # self.store_db(item)
        print(item)
        return item
