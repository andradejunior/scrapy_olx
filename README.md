# scrapy_olx

Web crawler for olx website with framework Scrapy.

Spider that crawl data about cars in the website https://rn.olx.com.br/autos-e-pecas/carros-vans-e-utilitarios/ and insert the information in a mongodb database.

## Dependencies
* Mongodb instaled and activated.
* python 3.6+  
Python libraries:  
* Scrapy==1.5.2
* pymongo==3.7.2

## Install libraries
> pip install -r requirements.txt

## Run spider
> cd olx/  
> scrapy crawl cars
