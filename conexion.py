import requests
r=requests.get("https://api.groupon.com/v2/deals.json", params = {"client_id":"eb9ff18a490c1d0e00419123560879fa1b16e02d","division_id":"san-francisco"})
print r.text


