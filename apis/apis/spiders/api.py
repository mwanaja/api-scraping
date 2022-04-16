import scrapy
from urllib.request import Request

class ApiSpider(scrapy.Spider):
    name = 'api'
    allowed_domains = ['programmableweb.com']
    start_urls = ['https://www.programmableweb.com/category/all/apis']

    def parse(self, response, *args, **kwargs):
        apis = response.xpath('//tbody')
        for api in apis:
            apiName = api.xpath('.//*[@class = "views-field views-field-pw-version-title"]/a/text()').extract_first()
            apiLink = api.xpath('.//*[@class = "views-field views-field-pw-version-title"]/a/@href').extract_first()
            apiDescriptions = api.xpath('.//*[@class = "views-field views-field-search-api-excerpt views-field-field-api-description hidden-xs visible-md visible-sm col-md-8"]/text()').extract_first()
            apiCategory = api.xpath('.//*[@class = "views-field views-field-field-article-primary-category"]/a/text()').extract_first()
            apiCategorylink = api.xpath('.//*[@class = "views-field views-field-field-article-primary-category"]/a/@href').extract_first()
            followers = api.xpath( './/*[@class = "views-field views-field-flag-follow-api-count"][1]/text()').extract_first()
            apiVersions = api.xpath('.//*[@class = "views-field views-field-pw-version-links"]/text()').extract_first()
            apiVersionlink = api.xpath('.//*[@class = "views-field views-field-pw-version-links"]/a/@href').extract_first()

            # Website Link used to create API LINK and API CATEGORY LINK
            link = "https://www.programmableweb.com"

            #Yield part
            yield {
            'API Name ' :apiName,
            'API Link ' : link+apiLink,
            'API Description ' : apiDescriptions,
            'API Category ' : apiCategory,
            'API Category Link ' : link+apiCategorylink,
            'API Followers ' : followers,
            'API Versions ' : apiVersions,
            'API Versions Link ' :link+apiVersionlink
            }
            nextPage =response.xpath('//*[@class = "pager-last"]/a/@href').extract_first()
            absoluteNextPage_url = response.urljoin(nextPage)
            yield scrapy.Request(absoluteNextPage_url)
