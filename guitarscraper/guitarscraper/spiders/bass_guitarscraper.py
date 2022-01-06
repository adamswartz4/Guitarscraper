import scrapy
class GuitarScraper(scrapy.Spider):
    
    name= 'bass'
    start_urls = ['https://www.long-mcquade.com/?page=departments&DepartmentsID=13&StockFilter=0&OnSaleOnly=1']

    def parse(self, response):
        count=-1
        for products in response.css('div.products-item '):
            count+=1
            yield{
                'name': products.css('span::text').get(),  
                'model': products.css('span::text')[1].get(),
                'brand': products.css('h5::text').get(),
                'sale price': products.css('span.font-red::text').get(),
                'original price':products.css('p.products-item-price::text').get(), 
                'link': response.css('a.products-item-link')[count].attrib['href']
                }