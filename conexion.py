import requests
r=requests.get("http://api.groupon.com/v2/channels/getaways/deals.xml?client_id=eb9ff18a490c1d0e00419123560879fa1b16e02d&show=title,status,largeImageUrl,mediumImageUrl,isTipped,tippingPoint,endAt,dealUrl,merchant,isSoldOut,tippedAt,soldQuantity,options,announcementTitle,tags HTTP/1.1")
print r.url
r.text
