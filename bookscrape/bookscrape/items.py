# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst, MapCompose, Identity, Compose
import re

def num_pages_extractor(num_pages):
    if num_pages:
        return num_pages.split()[0]
    return None

def publish_data_extractor(publish_date):
    if publish_date:
        date_content = [s for s in publish_date if 'published' in s.lower()][0]
        return date_content.split('\n        ')[2]
    return None

def first_publish_date_extractor(first_publish_date):
    if first_publish_date:
        date_content = [s for s in first_publish_date if 'first published' in s.lower()][0]
        return re.split('\(|\)|published ', date_content)[2]
    return None
def isbn13_filter(isbn13):
    if isbn13 and len(str(isbn13)) == 13 and isbn13.isdigit():
        return isbn13
    return None

def isbn_filter(isbn):
    if isbn and len(str(isbn)) == 10 and isbn.isdigit():
        return isbn
    return None

def extract_ratings(txt):
    """Extract the rating histogram from embedded Javascript code

        The embedded code looks like this:

        |----------------------------------------------------------|
        | renderRatingGraph([6, 3, 2, 2, 1]);                      |
        | if ($('rating_details')) {                               |
        |   $('rating_details').insert({top: $('rating_graph')})   |
        |  }                                                       |
        |----------------------------------------------------------|
    """
    codelines = "".join(txt).split(";")
    rating_code = [line.strip() for line in codelines if "renderRatingGraph" in line]
    if not rating_code:
        return None
    rating_code = rating_code[0]
    rating_array = rating_code[rating_code.index("[") + 1 : rating_code.index("]")]
    ratings = {5 - i:int(x) for i, x in enumerate(rating_array.split(","))}
    return ratings

class BookscrapeItem(scrapy.Item):
    bookId = scrapy.Field()
    title       = scrapy.Field(input_processor=MapCompose(str.strip))
    author      = scrapy.Field(input_processor=MapCompose(str.strip))
    num_ratings = scrapy.Field(input_processor=MapCompose(str.strip, int))
    num_reviews = scrapy.Field(input_processor=MapCompose(str.strip, int))
    num_pages   = scrapy.Field(input_processor=MapCompose(str.strip, num_pages_extractor, int))
    avg_rating = scrapy.Field(input_processor=MapCompose(str.strip, float))

    language = scrapy.Field(input_processor=MapCompose(str.strip))
    publish_date = scrapy.Field(input_processor=publish_data_extractor)
    first_publish_date = scrapy.Field(input_processor=first_publish_date_extractor)

    series = scrapy.Field(input_processor=MapCompose(str.strip))

    characters = scrapy.Field(output_processor=Identity())
    places = scrapy.Field(output_processor=Identity())
    awards = scrapy.Field(output_processor=Identity())

    genres = scrapy.Field(output_processor=Compose(set, list))
    isbn13 = scrapy.Field(input_processor=MapCompose(str.strip, isbn13_filter))
    isbn = scrapy.Field(input_processor=MapCompose(str.strip, isbn_filter))

    # All ratings (1-5 stars)
    ratings = scrapy.Field(input_processor=MapCompose(extract_ratings))

    pass
