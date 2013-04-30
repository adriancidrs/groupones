import requests
import json
channel='getaways'
if channel == 'getaways':
	r=requests.get("https://api.groupon.com/v2/channels/getaways/deals.json", params = {"client_id":"eb9ff18a490c1d0e00419123560879fa1b16e02d","status":"open"})
	priceamount = json.loads(r.text)["deals"][0]["options"][0]["discount"]["formattedAmount"]
	headline =json.loads(r.text)["deals"][0]['textAd']['headline']
	ciudad = json.loads(r.text)["deals"][0]["options"][0]["redemptionLocations"][0]["city"]
	phone = json.loads(r.text)["deals"][0]["options"][0]["redemptionLocations"][0]["phoneNumber"]
	pais = json.loads(r.text)["deals"][0]["options"][0]["redemptionLocations"][0]["country"]
	estado = json.loads(r.text)["deals"][0]["options"][0]["redemptionLocations"][0]["state"]
	fechafin = json.loads(r.text)["deals"][0]["options"][0]["endAt"]

	print json.loads(r.text)["deals"][1][u'title', u'uuid']
	cat respuesta.json | jq '.deals[] | {textAd, options | {id}, value, expiresAT, title, expiresInDays, details}' |less
	json.loads(r.text)["deals"][0][u'textAd':[headline]]


		
elif channel == 'goods':
	r=requests.get("https://api.groupon.com/v2/channels/goods/deals.json", params = {"client_id":"eb9ff18a490c1d0e00419123560879fa1b16e02d","status":"open"})
elif channel == 'occassions':
	r=requests.get("https://api.groupon.com/v2/channels/occasions/deals.json", params = {"client_id":"eb9ff18a490c1d0e00419123560879fa1b16e02d","status":"open"})
else:
	print 'Consulta incorrecta'




