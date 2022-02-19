# The Book Spider
A simple Scrapy project to extract data from all 1000 books of books.toscrape.com


The project contains one spider that sneaks through all categories pages in order to extract all book's data from all books in the site.

I'm interested in getting these fields:
- Book Title
- Book Price
- Book Image URL
- Book Details Page URL

About the Spider: 
- It's not a generic spider, it was created using a CrawlSpider template.
- The spider follows two simple rules. The first one is related to the categories. The spider should enter in all categories pages and extract book data from them. The second one is related to the pagination of categories pages. Even if there is more than one page in the specific category the spider should enter in all of them.
