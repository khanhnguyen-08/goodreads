import scrapy

class BooksSpider(scrapy.Spider):
    name = "books"

    start_urls = [  'https://www.goodreads.com/book/show/1',
                    'https://www.goodreads.com/book/show/2']

    def parse(self, response):
        book = response.url.split()