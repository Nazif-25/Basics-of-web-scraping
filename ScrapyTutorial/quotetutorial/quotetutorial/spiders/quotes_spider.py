import scrapy
from ..items import QuotetutorialItem


class QuoteSpider(scrapy.Spider):
    # the "name" and "start_urls" variables are must have variables in any spider
    name = "quotes"
    start_urls = [
        "https://quotes.toscrape.com/"
    ]

    # response variable contains the source code of the website we're crawling
    def parse(self, response):
        items = QuotetutorialItem()

        all_div_quotes = response.css('div.quote')

        for quote in all_div_quotes:
            title = quote.css('span.text::text').extract()
            author = quote.css('.author::text').extract()
            tag = quote.css('.tag::text').extract()

            items["title"] = title
            items["author"] = author
            items["tag"] = tag

            yield items



