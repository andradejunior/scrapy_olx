"""Spider for cars."""
import scrapy


class CarsSpider(scrapy.Spider):
    """Spider class for cars."""

    name = 'cars'
    allowed_domains = ['rn.olx.com.br']
    start_urls = ['''https://rn.olx.com.br/autos-e-pecas/
                     carros-vans-e-utilitarios/''']

    def parse(self, response):
        """Parse method for cars."""
        items = response.xpath('//ul[@id="main-ad-list"]/li')
        for item in items:
            self.log(item.xpath('./a/@href').extract_first())
