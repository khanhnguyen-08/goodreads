import scrapy
from ..items import BookscrapeItem

class BooksSpider(scrapy.Spider):
    name = "books"

    start_urls = [
        'https://www.goodreads.com/book/show/1'
        ]

    def parse(self, response):

        items = BookscrapeItem()

        name        = response.css('#bookTitle::text')[0].extract().strip()
        author      = response.css("a.authorName>span::text").extract_first()
        num_ratings = response.css("[itemprop=ratingCount]::attr(content)").extract()
        num_reviews = response.css("[itemprop=reviewCount]::attr(content)").extract()
        num_pages   = response.css("span[itemprop=numberOfPages]::text").extract_first().replace(' pages','')
        
        items['bookTitle'] = name
        items['author'] = author
        items['num_ratings'] = num_ratings
        items['num_reviews'] = num_reviews
        items['num_pages'] = num_pages

        yield items