# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3

class BookscrapePipeline:

    def __init__(self):
        self.create_connection()
        self.create_table()
    
    def create_connection(self):
        self.conn = sqlite3.connect("mybooks.db")
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
        self.curr.execute("""insert into books_tb values (?,?,?,?,?)""", (
            item['bookTitle'],
            item['author'],
            item['num_ratings'],
            item['num_reviews'],
            item['num_pages']
        ))
        self.curr.commit()

    def process_item(self, item, spider):
        self.store_db(item)
        return item
