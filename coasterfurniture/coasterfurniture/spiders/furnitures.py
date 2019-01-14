# -*- coding: utf-8 -*-
from scrapy import Spider
from scrapy.http import Request

def product_info(response, value):
    return response.xpath('.//div[@class="col-span-2"]/ul/li['+value+']/text()').extract_first().strip()


class FurnituresSpider(Spider):
    name = 'furnitures'
    allowed_domains = ['coasterfurniture.com']
    start_urls = ['http://coasterfurniture.com/']

    def parse(self, response):
        furniture_url = 'adele-contemporary-metallic-eastern-king-bed'
        absolute_furniture_url = response.urljoin(furniture_url)
        yield Request(absolute_furniture_url, callback=self.parse_product)

        # process Dimensions&Weight
        dimensions_url = response.xpath('.//ul[contains(@class,"nav-tabs")]/li[2]/a/@href').extract_first()
        absolute_dimensions_url = response.urljoin(dimensions_url)
        yield Request(absolute_dimensions_url)

    # product information data points
    def parse_product(self, response):
    	brand = response.xpath('.//div/h2/text()').extract_first()
    	title = response.xpath('.//div/h1/text()').extract_first()
    	collection = response.xpath('.//ul[contains(@class,"lead")]/li[1]/text()').extract_first().split(':')[1]
    	sku = response.xpath('.//ul[contains(@class,"lead")]/li[2]/text()').extract_first().split(':')[1]
    	description = response.xpath('.//p[contains(@class,"lead")]/text()').extract_first()
    	setOfproducts = product_info(response,"1").split(':')[1]
    	materials =  product_info(response,"2").split(':')[1]
    	fabricColor = product_info(response,"3").split(':')[1]
    	finishColor = product_info(response,"4").split(':')[1]
    	isAssemblyRequired = product_info(response,"5").split(':')[1]
    	propertySix = product_info(response,"6")
    	propertySeven = product_info(response,"7")
    	propertyEight = product_info(response,"8")
    	
    	yield {
    		'Brand': brand,
    		'Title': title,
    		'Collection': collection,
    		'SKU': sku,
    		'Description': description,
    		'Set includes': setOfproducts,
    		'Materials': materials,
    		'Fabric Color': fabricColor,
    		'Finish Color': finishColor,
    		'Assembly Required': isAssemblyRequired,
    		'Property 6': propertySix,
    		'Property 7': propertySeven,
    		'Property 8': propertyEight
    	}	  

    	    
