import scrapy
from ..items import BookscrapeItem
from scrapy.loader import ItemLoader


class BooksSpider(scrapy.Spider):
    # spiders name to be called
    name = "books"
    start_id = 20001
    end_id = 30000
    bookId = start_id
    start_urls = ['https://www.goodreads.com/book/show/'+str(start_id)]

    def parse(self, response):
        loader = ItemLoader(item=BookscrapeItem(), response=response)

        loader.add_value('bookId', str(BooksSpider.bookId))
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
        # loader.add_css("isbn13", 'span[itemprop=isbn]::text')
        # loader.add_css("isbn", 'div.infoBoxRowItem::text')
        loader.add_css('isbn', 'div.infoBoxRowItem[itemprop=isbn]::text')
        loader.add_css('isbn', 'span[itemprop=isbn]::text')
        loader.add_css('isbn', 'div.infoBoxRowItem::text')
        loader.add_css('isbn13', 'div.infoBoxRowItem[itemprop=isbn]::text')
        loader.add_css('isbn13', 'span[itemprop=isbn]::text')
        loader.add_css('isbn13', 'div.infoBoxRowItem::text')

        loader.add_css("rated_5",'script[type*="protovis"]::text')
        loader.add_css("rated_4",'script[type*="protovis"]::text')
        loader.add_css("rated_3",'script[type*="protovis"]::text')
        loader.add_css("rated_2",'script[type*="protovis"]::text')
        loader.add_css("rated_1",'script[type*="protovis"]::text')

        loader.add_css("description", 'div#description>span::text')

        yield loader.load_item()
        
        BooksSpider.bookId += 1
        next_page = 'https://www.goodreads.com/book/show/'+str(BooksSpider.bookId)
        if BooksSpider.bookId <= BooksSpider.end_id:
            yield response.follow(next_page, callback=self.parse)