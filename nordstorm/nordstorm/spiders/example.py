import scrapy
from scrapy.cmdline import execute
from scrapy.utils.response import open_in_browser


class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['example.com']
    start_urls = ['http://example.com/']

    def parse(self, response):

        url = 'https://www.nordstrom.com/browse/men/clothing/jeans?campaign=0502denimslim&jid=j012877-18627&cm_sp=merch-_-mens_18627_j012877-_-cathead_0_p00_0&offset=2&page=4&filterByFit=slim-fit'
        payload = {}
        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8,gu;q=0.7',
            'cache-control': 'max-age=0',
            # 'cookie': 'no-track=ccpa=false; nordstrom=bagcount=0&firstname=&ispinned=False&isSocial=False&shopperattr=||0|False|-1&shopperid=4372eb869e974f9a981515d9f9229890&USERNAME=; nui=firstVisit=2022-06-09T16%3A25%3A11.439Z&geoLocation=&isModified=false&lme=false; shoppertoken=shopperToken=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI0MzcyZWI4NjllOTc0ZjlhOTgxNTE1ZDlmOTIyOTg5MCIsImF1ZCI6Imd1ZXN0IiwiaXNzIjoibm9yZHN0cm9tLWd1ZXN0LWF1dGgiLCJleHAiOjE5NzA0MTExMTEsInJlZnJlc2giOjE2NTQ4MDYzMTEsImp0aSI6IjdlMTQ4OGM2LTI5MTEtNGI4Mi05ZjY2LWI4ZTdmMmIwNjRhMSIsImlhdCI6MTY1NDc5MTkxMX0.ZU3O-9-FvuWbF6cL84KM0qy9fWIgJJLGDN3KFgSDtg-mjm1HSCen8KS3NXeVCtO9BYnxQBeQJDtDwwrUa4UmxnbYm50J3ogL8hhva7yKUA6JJHaWDvsSrbC_4-tLV9XXZQIHQnX3hNUDO3rCBf075Z4cwJ4R6JmIx-4OPhTOcgjH6-QYf4U7iBwPrDKwOTRWko32wP2mfg6W-uACNqNS9NoAPM3qKNiJS3SA5avIryP5D2o7Ie9Ha6LUXy5CyvA0f4KUD7uy-iBC7uA7c7qlbvYQK4Xy_SL21fdFN2Tb4LIswqnXhYt4doblV-coGZAbrlMnHEhOgAmoUyTenI0LWw; usersession=CookieDomain=nordstrom.com&SessionId=e0dad7c5-73ea-4437-9bb3-67e462d60611; experiments=ExperimentId=1dbba6d7-2500-4a54-a368-6dda4a1f5e9d; Ad34bsY56=A0yuSEmBAQAAYlDJU2Gu3Be5mVD8dXjl_GqUM916QBoLp33gFcEBYxXfwBDtAV1zHLWuckQBwH8AAEB3AAAAAA|1|1|6aee84248e887b7517831dc73b68dacce347e6ca; Bd34bsY56=AwK3SEmBAQAAtMc8FH0R7-lLjTBRFswH3UbmjYw2LAaePPcDGarq2UGlo9_SAV1zHLWuckQBwH8AAEB3AAAAAA==; _gcl_au=1.1.868581938.1654791925; storemode=version=4&postalCode=&selectedStoreIds=&storesById=&localMarketId=&localMarketsById=; session=FILTERSTATE=&RESULTBACK=&RETURNURL=http%3A%2F%2Fshop.nordstrom.com&SEARCHRETURNURL=http%3A%2F%2Fshop.nordstrom.com&FLSEmployeeNumber=&FLSRegisterNumber=&FLSStoreNumber=&FLSPOSType=&gctoken=&CookieDomain=&IsStoreModeActive=0&; _gid=GA1.2.2123569836.1654791933; _scid=d7eb7a2a-78a3-4bd6-b0e4-4021f7228246; ftr_ncd=6; _4c_mc_=251440bd-f82c-464c-a77e-2ea9c133740e; _pin_unauth=dWlkPVlXRm1NREExTWpZdE5qZ3dPUzAwTURJeUxXRmlPVGt0TmpBMlpqTmxNamM0TXpaag; trx=4710870768870341909; _fbp=fb.1.1654791978403.761388846; bluecoreNV=true; _clck=1riofnt|1|f26|0; wlcme=false; internationalshippref=preferredcountry=US&preferredcurrency=USD&preferredcountryname=United%20States; rfx-forex-rate=currencyCode=USD&exchangeRate=1&quoteId=0; bc_invalidateUrlCache_targeting=1654792598903; _gat_UA-107105548-1=1; storeprefs=|100|||2022-06-09T16:40:35.321Z; _gat_UA-107105548-20=1; _uetsid=c8b82bb0e81011ecb23197515707412c; _uetvid=c8b872f0e81011ec9613e9e620fd2e7f; mp_nordstrom_com_mixpanel=%7B%22distinct_id%22%3A%20%2218149493675d-029f66ae3099f9-26021b51-144000-18149493676887%22%2C%22bc_persist_updated%22%3A%201654791943818%2C%22g_search_engine%22%3A%20%22google%22%2C%22bc_last_opaque_id%22%3A%201673561694%7D; forterToken=30e6f56dce024ee3b6f24d3a09f40007_1654792834026__UDF43_6; _ga_XWLT9WQ1YB=GS1.1.1654791936.1.1.1654792846.54; _clsk=1i7mk4b|1654792848254|11|1|f.clarity.ms/collect; _ga=GA1.2.1783561457.1654791933; Ad34bsY56=A9WuUUmBAQAAGaS2MODPAbpsHFDNS7PoyFR_KezIhE63bPAlK_F32MwcCQxxAdiXtFeuckQBwH8AAEB3AAAAAA|1|0|3f3eeea365402df6f6fbbc28ddc852b34a27def6',
            'referer': 'https://www.nordstrom.com/browse/men/clothing/jeans?campaign=0502denimslim&jid=j012877-18627&cm_sp=merch-_-mens_18627_j012877-_-cathead_0_p00_0&filterByFit=slim-fit',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
        }
        
        yield scrapy.FormRequest(url=url,callback=self.parse2,dont_filter=True,headers=headers)
        
    def parse2(self,response):
        open_in_browser(response)

        print("iii")

execute('scrapy crawl example'.split())