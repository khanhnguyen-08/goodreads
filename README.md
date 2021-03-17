# goodreads
Goodreads's book crawling project can be used to collect book metadata from Goodreads website.

According to Goodreads, "As of December 8th 2020, Goodreads no longer issues new developer keys for our public developer API and plans to retire the current 
version of these tools.". Therefore, this project is developed by scraping information directly from Goodreads pages by creating spider to crawl a site and extract
html data using [Scrapy](https://docs.scrapy.org/en/latest/).

We used this scraper to collect data for our project of "Book classification and segtimentation" and "Book rating prediction". The scraper is targeted at crawling 
metadat of over 50,000 books from Goodreads for our projects. The raw data will be cleansed and published on Kaggle dataset for those who are also interested in
the dataset.

*Note: Due to limitation of HTTPconnection to Goodreads website, the spider maybe interrupted at some pages, you may need to update the lastest scraped book ID as 
start_ID and re-run the script.*

<br><br>

# What You Need

To run the scripts, you will need Python3 installed with the following libraries:
- [Scrapy](https://docs.scrapy.org/en/latest/intro/install.html)
- [MongoDB](https://docs.mongodb.com/manual/installation/)

*Recommendation: create a new virtual environment using [virtualenv](https://pypi.org/project/virtualenv/) for this project, 
then install these libraries by running 'pip install -r requirements.txt'.*

<br><br>

# Tutorial
1. Download this project using "Git clone https://github.com/KhanhDNg/goodreads.git"
2. Setup MongoDB database and MongoDB Compass for your local machine:
- Tutorial link: [Official tutorial](https://docs.mongodb.com/manual/installation/)
3. Setup virtual environment:
- Install virtualenv.
- Create a new virtual environment.
- Run 'pip install -r requirements.txt' to install libraries.
- Activate the environment to start scraping.
*Note: we recommend using VS Code for this project for more conviniences"
4. Run the script from command line (Make sure you are using the created virtual environment):
- 4.1: On terminal, go to path "goodreads/bookscrape".
- 4.2: Set start_ID and end_ID values in the file 'books_spider.py'.
- 4.3: On terminal, run command 'scrapy crawl books'.
- Repeat 4.2 and 4.3 if the spider is stopped due to HTTPConnection/error.

5. Optional: MongoDB compass
- Connect to local database using MongoDB compass
- Select dbs 'books' --> select collection 'books_tb'
- Now, you are able to see book metadata of records you have creaped from Goodreads.

# Goodreads Book Metadata
## books_spider.py
### Input
This script takes 2 inputs 'start_id' and 'end_id' as the range of book id we want to scrape from Goodreads. The book_id will be looped from start_id to end_id
and replaced into url "'https://www.goodreads.com/book/show/'+str(start_id)" to request html response for spider.

### Output
This script outputs a JSON file for each book with the following information:

- book ID
- book title
- author
- descriptions
- total number of ratings
- total number of reviews
- average rating
- language
- publish date
- first publish date
- series
- list of characters
- list of places
- list of awards
- list of genres
- isbn
- isbn13
- Rating distributions: rated 5, 4, 3, 2, 1

These metadata is loaded into Iteams script for processing, then stored into MongoDB database in pipeline script.

# Dataset
We have exported samples of our data collected as JSOn and CSV in the folder 'db' for experimental purposes.

# Credit
This project is written by Justin Nguyen for learning purpose.

Hope you enjoy your learning! Cheers.
