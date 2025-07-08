import scrapy

from bookscraper.items import BookItem


class BookspiderSpider(scrapy.Spider):
    name = "bookspider"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com"]
    page_number = 1

    def parse(self, response):

        books = response.css("article.product_pod")
        for book in books:
            relative_url = book.css("h3 a ::attr(href)").get()

            yield response.follow(relative_url, callback=self.parse_book_page)

        if self.page_number >= 1:
            # Define o numero de paginas
            return
        next_page = response.css("li.next a::attr(href)").get()
        if next_page is not None:
            self.page_number += 1
            yield response.follow(next_page, callback=self.parse)

    def parse_book_page(self, response):
        book_item = BookItem()
        image_url = response.css("div.carousel-inner img::attr(src)").get()

        book_item["url"] = (response.url,)
        book_item["image"] = (response.urljoin(image_url),)
        book_item["title"] = (response.css("div.col-sm-6.product_main h1::text").get(),)
        book_item["description"] = (
            response.css("article.product_page p ::text").getall()[-1].strip(),
        )
        book_item["price_excl_tax"] = (
            response.css("table.table.table-striped td ::text").getall()[2],
        )
        book_item["price_incl_tax"] = (
            response.css("table.table.table-striped td ::text").getall()[3],
        )
        book_item["tax"] = (
            response.css("table.table.table-striped td ::text").getall()[4],
        )

        yield book_item
