import pandas as pd
import numpy as np
data = pd.read_csv('/home/justin/Documents/goodreads/db/books_tb_csv')
data = data.drop('_id', axis=1)
print(data.shape)
print(data.columns)

# Create lists of attributes for cleansing
num_attribs = ['avg_rating', 'num_pages', 'num_ratings', 'num_reviews', 'rated_1', 'rated_2', 'rated_3', 'rated_4', 'rated_5']
m_cat_attribs = ['author', 'awards', 'characters','description', 'genres', 'language', 'series', 'places']
s_cat_attribs = ['title', 'isbn', 'isbn13', 'bookId']
datetime_attribs = ['first_publish_date', 'publish_date']

# Strip [, ] and " from text data
for col in data.columns:
    data[col] = data[col].str.strip('"[]')
    # data[col] = data[col].str.replace('null', np.NaN)

# Numeric attributes:
# 1. Strip symbols: [, ] and "
# 2. Replace text 'Null' by numpy's nan value
# 3. Convert columns to numeric type 
def num_cols_handler(num_cols):
    for col in num_cols:
        data[col] = data[col].str.strip('"[]')
        data[col] = data[col].replace('Null', np.nan)
        data[col] = pd.to_numeric(data[col])

# Call the function to handle numeric columns
num_cols_handler(num_attribs)
print("\nNumerical cols handler: Completed!")
print(data[num_attribs].describe())

# Single value categorical attributes
# 1. Strip symbols: [, ] and "
# 2. Replace text 'Null' by numpy's nan value
def cat_cols_handler(s_cat_cols):
    for col in s_cat_cols:
        data[col] = data[col].str.strip('"[]()')
        data[col] = data[col].replace('Null', np.nan)

cat_cols_handler(s_cat_attribs+datetime_attribs)
print("\nSingle value categorical cols handler: Completed!")
print(data[s_cat_attribs+datetime_attribs].describe())

# Single value categorical attributes
# 1. Strip symbols: [, ] and "
# 2. Replace text 'Null' by numpy's nan value
# 2. Remove symbols '"'
def m_cat_cols_handler(m_cat_cols):
    for col in m_cat_cols:
        data[col] = data[col].str.replace('["()]', '')
        data[col] = data[col].replace('Null', np.nan)


m_cat_cols_handler(m_cat_attribs)
print("\nMultiple values categorical cols handler: Completed!")
print(data[m_cat_attribs].describe())

print(data.describe(include='all'))
ordered_cols = ['bookId', 'title', 'author', 'series', 'description', 'genres', 'awards', 'characters', 'places', 'isbn', 'isbn13', 'language', 'first_publish_date', 
                'publish_date', 'num_pages', 'num_ratings', 'num_reviews', 'avg_rating', 'rated_1', 'rated_2', 'rated_3', 'rated_4', 'rated_5']
data[ordered_cols].to_excel("Goodreads's Books.xlsx")