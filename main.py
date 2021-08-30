import requests

url = 'http://brickset.com/sets/year-2007'
r = requests.get(url)

print(r.text)

print("Status code:")
print("\t *", r.status_code)

h = requests.head(url)
print("Header:")
print("**********")

for x in h.headers:
    print("\t ", x, ":", h.headers[x])
print("**********")

headers = {
    'User-Agent' : 'mobile'
}

url2 = 'http://brickset.com/sets/year-2007'
rh = requests.get(url2, headers=headers)
print(rh.request.headers)

import scrapy

class BrickSetSpider(scrapy.Spider):
    name = "brickset_spider"
    start_urls = ['http://brickset.com/sets/year-2007']

    def parse(self, response, **kwargs):
        SET_SELECTOR = '.set'
        for brickset in response.css(SET_SELECTOR):

            IMAGE_SELECTOR = 'img ::attr(src)'
            yield {
                'image': brickset.css(IMAGE_SELECTOR).extract_first(),
            }

        NEXT_PAGE_SELECTOR = '.next a ::attr(href)'
        next_page = response.css(NEXT_PAGE_SELECTOR).extract_first()
        if next_page:
             yield scrapy.Request(
                response.urljoin(next_page),
                callback=self.parse
              )
