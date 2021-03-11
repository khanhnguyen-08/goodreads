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

def publish_data_extractor(publish_date):
    if publish_date:
        date_content = [s for s in publish_date if 'published' in s.lower()][0]
        return date_content.split('\n        ')[2]

def first_publish_date_extractor(first_publish_date):
    if first_publish_date:
        date_content = [s for s in first_publish_date if 'first published' in s.lower()][0]
        return re.split('\(|\)|published ', date_content)[2]

def isbn13_filter(isbn13):
    if isbn13 and len(str(isbn13)) == 13 and isbn13.isdigit():
        return isbn13

def isbn_filter(isbn):
    if isbn and len(str(isbn)) == 10 and isbn.isdigit():
        return isbn

def extract_rated_5(txt):
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
    rated_5 = rating_array.split(', ')[0]
    return rated_5

def extract_rated_4(txt):
    codelines = "".join(txt).split(";")
    rating_code = [line.strip() for line in codelines if "renderRatingGraph" in line]
    if not rating_code:
        return None
    rating_code = rating_code[0]
    rating_array = rating_code[rating_code.index("[") + 1 : rating_code.index("]")]
    rated_4 = rating_array.split(', ')[1]
    return rated_4

def extract_rated_3(txt):
    codelines = "".join(txt).split(";")
    rating_code = [line.strip() for line in codelines if "renderRatingGraph" in line]
    if not rating_code:
        return None
    rating_code = rating_code[0]
    rating_array = rating_code[rating_code.index("[") + 1 : rating_code.index("]")]
    rated_3 = rating_array.split(', ')[2]
    return rated_3

def extract_rated_2(txt):
    codelines = "".join(txt).split(";")
    rating_code = [line.strip() for line in codelines if "renderRatingGraph" in line]
    if not rating_code:
        return None
    rating_code = rating_code[0]
    rating_array = rating_code[rating_code.index("[") + 1 : rating_code.index("]")]
    rated_2 = rating_array.split(', ')[3]
    return rated_2

def extract_rated_1(txt):
    codelines = "".join(txt).split(";")
    rating_code = [line.strip() for line in codelines if "renderRatingGraph" in line]
    if not rating_code:
        return None
    rating_code = rating_code[0]
    rating_array = rating_code[rating_code.index("[") + 1 : rating_code.index("]")]
    rated_1 = rating_array.split(', ')[4]
    return rated_1

class BookscrapeItem(scrapy.Item):
    bookId = scrapy.Field()
    title = scrapy.Field(input_processor=MapCompose(str.strip))
    author = scrapy.Field(input_processor=MapCompose(str.strip))
    num_ratings = scrapy.Field(input_processor=MapCompose(str.strip))
    num_reviews = scrapy.Field(input_processor=MapCompose(str.strip))
    num_pages = scrapy.Field(input_processor=MapCompose(str.strip, num_pages_extractor))
    avg_rating = scrapy.Field(input_processor=MapCompose(str.strip))

    language = scrapy.Field(input_processor=MapCompose(str.strip))
    publish_date = scrapy.Field(input_processor=publish_data_extractor)
    first_publish_date = scrapy.Field(input_processor=first_publish_date_extractor)

    series = scrapy.Field(input_processor=MapCompose(str.strip))

    characters = scrapy.Field(output_processor=Identity())
    places = scrapy.Field(output_processor=Identity())
    awards = scrapy.Field(output_processor=Identity())

    genres = scrapy.Field(input_processor=MapCompose(str.strip))
    isbn13 = scrapy.Field(input_processor=MapCompose(str.strip, isbn13_filter))
    isbn = scrapy.Field(input_processor=MapCompose(str.strip, isbn_filter))

    # All ratings (1-5 stars)
    rated_5 = scrapy.Field(input_processor=MapCompose(extract_rated_5))
    rated_4 = scrapy.Field(input_processor=MapCompose(extract_rated_4))
    rated_3 = scrapy.Field(input_processor=MapCompose(extract_rated_3))
    rated_2 = scrapy.Field(input_processor=MapCompose(extract_rated_2))
    rated_1 = scrapy.Field(input_processor=MapCompose(extract_rated_1))

    # Extract description
    description = scrapy.Field(input_processor=MapCompose(str.strip))


    pass
