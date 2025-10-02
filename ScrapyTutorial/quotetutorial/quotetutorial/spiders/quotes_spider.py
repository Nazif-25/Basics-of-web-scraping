import scrapy
from ..items import QuotetutorialItem


class QuoteSpider(scrapy.Spider):
    # the "name" and "start_urls" variables are must have variables in any spider
    name = "quotes"
    start_urls = ["https://quotes.toscrape.com/"]

    # response variable contains the source code of the website we're crawling
    def parse(self, response):
        all_div_quotes = response.css('div.quote')

        for quote in all_div_quotes:
            # Create a new item for each loop iteration
            items = QuotetutorialItem()

            items["title"] = quote.css('span.text::text').get()
            items["author"] = quote.css('.author::text').get()
            items["tag"] = quote.css('.tag::text').getall()

            yield items

        # Follow pagination links
        next_page = response.css("li.next a::attr(href)").get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)



