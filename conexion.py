import requests
import json
from bottle import route, static_file, request, template, debug, run

@route('/style/:filename#.*#')
def send_static(filename):
    return static_file(filename, root='./style/')

@route('/')
def home_page():
    return template('index')

@route('/getaways')
def cs_geta():
    return template('getaways')

@route('/respuestagetaways', method='POST')
def res_geta():
    country = request.forms.get("country")
    r=requests.get("https://api.groupon.com/v2/channels/getaways/deals.json", params = {"client_id":"eb9ff18a490c1d0e00419123560879fa1b16e02d","status":"open","country":country})
    getaways = []
    resultado = json.loads(r.text)
    for i in resultado["deals"]:
        getaways.append(i['textAd']['headline'])
        getaways.append(i["options"][0]["discount"]["formattedAmount"])
#        getaways.append(i["options"][0]["redemptionLocations"][0]["city"])
#        getaways.append(i["options"][0]["redemptionLocations"][0]["phoneNumber"])
#        getaways.append(i["options"][0]["redemptionLocations"][0]["country"])
#        getaways.append(i["options"][0]["redemptionLocations"][0]["state"])
        getaways.append(i["options"][0]["endAt"])
        getaways.append(i["options"][0]["details"][0]["description"])
        getaways.append(i["grid4ImageUrl"])
    return template("respuestagetaways", getaways=getaways)
    
    
@route('/goods')
def cs_good():
    return template('goods')

@route('/respuestagoods', method='POST')
def res_good():
    goodg = request.forms.get("goodg")
    rg = requests.get("https://api.groupon.com/v2/channels/goods/deals.json", params = {"client_id":"eb9ff18a490c1d0e00419123560879fa1b16e02d","status":"open","tags":[{"name":"","name":goodg}]})
    goods = []
    resultado = json.loads(rg.text)
    for i in resultado["deals"]:
        goods.append(i["merchant"]["name"])
#        goods.append(i["dealTypes"][0]["description"])
        goods.append(i["endAt"])
        goods.append(i["options"][0]["discount"]["formattedAmount"])
        goods.append(i["finePrint"])
        goods.append(i["grid4ImageUrl"])

    return template("respuestagoods", goods=goods)

@route('/occasions')
def cs_occa():
    return template('occasions')

@route('/respuestaoccasions', method='POST')
def res_occa():
    occa = request.forms.get("occa")
    ro=requests.get("https://api.groupon.com/v2/channels/occasions/deals.json", params = {"client_id":"eb9ff18a490c1d0e00419123560879fa1b16e02d","status":"open","utm_term":occa})
    occasions = []
    resultado = json.loads(ro.text)
    for i in resultado["deals"]:
        occasions.append(i["announcementTitle"])
        occasions.append(i["finePrint"])
        occasions.append(i["grid4ImageUrl"])
        occasions.append(i["highlightsHtml"])
        occasions.append(i["options"][0]["discount"]["formattedAmount"])
        occasions.append(i["options"][0]["endAt"])
        occasions.append(i["options"][0]["details"][0]["description"])
    return template("respuestaoccasions", occasions=occasions)

debug(True)
run(host='localhost', port=8080)
