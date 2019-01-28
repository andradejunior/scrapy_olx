"""Spider for cars."""
import scrapy


class CarsSpider(scrapy.Spider):
    """Spider class for cars."""

    name = 'cars'
    allowed_domains = ['rn.olx.com.br']
    start_urls = ['''https://rn.olx.com.br/autos-e-pecas/'''
                  '''carros-vans-e-utilitarios/''']

    def parse(self, response):
        """Parse method for cars."""
        items = response.xpath(
            '//ul[@id="main-ad-list"]/li[not(contains(@class, "list_native"))]'
        )
        self.log(len(items))
        for item in items:
            url = item.xpath('./a/@href').extract_first()
            yield scrapy.Request(url=url, callback=self.parse_detail)

    def parse_detail(self, response):
        """Parse detail method for cars."""
        self.log(response.url)
