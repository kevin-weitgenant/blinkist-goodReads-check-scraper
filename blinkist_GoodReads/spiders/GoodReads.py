import scrapy

class GoodreadsSpider(scrapy.Spider):
    name = 'GoodReads'
    allowed_domains = ['goodreads.com']
    start_urls = ['https://www.goodreads.com/review/list/109133436-kevin-weitgenant?page=1&shelf=to-read']

    def parse(self, response):
        
        next_page = response.xpath("//a[@class = 'next_page']/@href").get()

        titulos = []
        urls = []
        for titulo in response.xpath('//tr[@class = "bookalike review"]'):       
            titulos.append(titulo.xpath('.//td[@class= "field title"]/div/a/@title').get()) #probably not necessary
            urls.append(titulo.xpath('.//td[@class= "field title"]/div/a/@href').get())

        for url in urls:
            yield response.follow(url = url, callback = self.parse_check_otherEditions)   #get all possible names for the book

        if next_page:
            yield response.follow(url=next_page, callback=self.parse) #pagination

    
    def parse_check_otherEditions(self,response):   #check for other editions button
        
        other_editions = response.xpath('//div[@class = "coverButton" and contains(a,"Other editions")]/a/@href').get()
        
        if other_editions:
            yield response.follow(url=other_editions, callback=self.parse_otherEditions, meta = {"book_url": response.url})
            
    def parse_otherEditions(self,response): #function to get all possible names for the book(with pagination)
        
        other_editions = response.xpath('//a[@class="bookTitle"]/text()').getall()
        next_page = response.xpath("//a[@class = 'next_page']/@href").get()
        
        if next_page: #pagination
            yield response.follow(url=next_page, callback=self.parse_otherEditions, meta = {"book_url":  response.request.meta["book_url"]})

        yield{
           response.request.meta["book_url"] : other_editions
        }

