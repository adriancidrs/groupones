import bottle
import requests
import json
from bottle import route, static_file

@route('/style/style.css')
def server_static(filename):
    return static_file(filename, root='style/')


@bottle.route('/')
def home_page():
    return bottle.template('index')

@bottle.route('/getaways')
def cs_geta():
    return bottle.template('getaways')

@bottle.route('/respuestagetaways', method='POST')
def res_geta():
    state = bottle.request.forms.get("estado")
    r=requests.get("https://api.groupon.com/v2/channels/getaways/deals.json", params = {"client_id":"eb9ff18a490c1d0e00419123560879fa1b16e02d","status":"open","country":"Spain"})
    getaways = []
    resultado = json.loads(r.text)
    for i in resultado["deals"]:
        getaways.append(i["options"][0]["discount"]["formattedAmount"])
        getaways.append(i['textAd']['headline'])
#        getaways.append(i["options"][0]["redemptionLocations"][0]["city"])
#        getaways.append(i["options"][0]["redemptionLocations"][0]["phoneNumber"])
#        getaways.append(i["options"][0]["redemptionLocations"][0]["country"])
#        getaways.append(i["options"][0]["redemptionLocations"][0]["state"])
        getaways.append(i["options"][0]["endAt"])
        getaways.append(i["options"][0]["details"][0]["description"])
        getaways.append(i["grid4ImageUrl"])
    return bottle.template("respuestagetaways", getaways=getaways)
    
    
@bottle.route('/goods')
def cs_good():
    return bottle.template('goods')

@bottle.route('/respuestagoods', method='POST')
def res_good():
    goodg = bottle.request.forms.get("goodg")
    rg = requests.get("https://api.groupon.com/v2/channels/goods/deals.json", params = {"client_id":"eb9ff18a490c1d0e00419123560879fa1b16e02d","status":"open","name":goodg})
    goods = []
    resultado = json.loads(rg.text)
    for i in resultado["deals"]:
        goods.append(i["merchant"]["name"])
#        goods.append(i["dealTypes"][0]["description"])
        goods.append(i["endAt"])
        goods.append(i["options"][0]["discount"]["formattedAmount"])
        goods.append(i["finePrint"])

    return bottle.template("respuestagoods", goods=goods)

@bottle.route('/occasions')
def cs_occa():
    return bottle.template('occasions')

@bottle.route('/respuestaoccasions', method='POST')
def res_occa():
    occa = bottle.request.forms.get("occa")
    ro=requests.get("https://api.groupon.com/v2/channels/occasions/deals.json", params = {"client_id":"eb9ff18a490c1d0e00419123560879fa1b16e02d","status":"open","tags":["",occa]})
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
    return bottle.template("respuestaoccasions", occasions=occasions)

bottle.debug(True)
bottle.run(host='localhost', port=8080)
