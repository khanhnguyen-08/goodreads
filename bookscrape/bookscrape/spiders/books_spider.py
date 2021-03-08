import scrapy
from ..items import BookscrapeItem
from scrapy.loader import ItemLoader


class BooksSpider(scrapy.Spider):
    # spiders name to be called
    name = "books"

    start_urls = [
        'https://www.goodreads.com/book/show/1'
        ]

    def parse(self, response):

        loader = ItemLoader(item=BookscrapeItem(), response=response)

        loader.add_css("title", "#bookTitle::text")
        loader.add_css("author", "a.authorName>span::text")

        loader.add_css("num_ratings", "[itemprop=ratingCount]::attr(content)")
        loader.add_css("num_reviews", "[itemprop=reviewCount]::attr(content)")
        loader.add_css("avg_rating", "span[itemprop=ratingValue]::text")
        loader.add_css("num_pages", "span[itemprop=numberOfPages]::text")

        loader.add_css("language", "div[itemprop=inLanguage]::text")
        loader.add_css("publish_date", "div.row::text")
        loader.add_css("first_publish_date", "nobr.greyText::text")

        loader.add_css("series", 'h2#bookSeries>a.greyText::text')
        # loader.add_css("series", 'div.InfoBoxRowItem>a[href*="/series/"]::text')
        loader.add_css("characters", 'a[href*="/characters/"]::text')
        loader.add_css("places", 'a[href*="/places/"]::text')
        loader.add_css("awards", 'a.award::text')

        loader.add_css("genres", 'a[href*="/genres/"]::text')
        loader.add_css("isbn13", 'span[itemprop=isbn]::text')
        loader.add_css("isbn", 'div.infoBoxRowItem::text')

        loader.add_css("ratings",'script[type*="protovis"]::text')

        yield loader.load_item()