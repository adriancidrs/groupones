import bottle
import requests
import json

@bottle.route('/')
def home_page():
    return bottle.template('index')

@bottle.route('/getaways')
def cs_geta():
    return bottle.template('getaways')

@bottle.route('/respuestagetaways', method='POST')
def res_geta():
    state = bottle.request.forms.get("estado")
    r=requests.get("https://api.groupon.com/v2/channels/getaways/deals.json", params = {"client_id":"eb9ff18a490c1d0e00419123560879fa1b16e02d","status":"open","state":state})
    priceamount = json.loads(r.text)["deals"][0]["options"][0]["discount"]["formattedAmount"]
    headline =json.loads(r.text)["deals"][0]['textAd']['headline']
    ciudad = json.loads(r.text)["deals"][0]["options"][0]["redemptionLocations"][0]["city"]
    phone = json.loads(r.text)["deals"][0]["options"][0]["redemptionLocations"][0]["phoneNumber"]
    pais = json.loads(r.text)["deals"][0]["options"][0]["redemptionLocations"][0]["country"]
    estado = json.loads(r.text)["deals"][0]["options"][0]["redemptionLocations"][0]["state"]
    fechafin = json.loads(r.text)["deals"][0]["options"][0]["endAt"]
    descripcion = json.loads(r.text)["deals"][0]["options"][0]["details"][0]["description"]	
    return bottle.template("respuestagetaways", precio=priceamount, titulo=headline, ciudad=ciudad, telefono=phone, pais=pais, estado=estado, fechafin=fechafin, descripcion=descripcion)

@bottle.route('/goods')
def cs_good():
    return bottle.template('goods')

@bottle.route('/respuestagoods', method='POST')
def res_good():
    return bottle.template('goods')
    goodg = bottle.request.forms.get("goodg")
    rg = requests.get("https://api.groupon.com/v2/channels/goods/deals.json", params = {"client_id":"eb9ff18a490c1d0e00419123560879fa1b16e02d","status":"open"})
    nombreg = json.loads(rg.text)["deals"][0]["merchant"]["name"]
    resumg = json.loads(rg.text)["deals"][0]["dealTypes"][0]["description"]
    fechafinig = json.loads(rg.text)["deals"][0]["endAt"]
    preciog = json.loads(rg.text)["deals"][0]["options"][0]["discount"]["formattedAmount"]
    descripciong = json.loads(rg.text)["deals"][0]["finePrint"]
    imageng = json.loads(rg.text)["deals"][0]["grid4ImageUrl"]
    imagenpeqg = json.loads(rg.text)["deals"][0]["mediumImageUrl"]
    return bottle.template("respuestagoods", nombreg=nombreg, resumg=resumg, fechafinig=fechafinig, preciog=preciog, descripciong=descripciong, imageng=imageng, imagenpeqg=imagenpeqg)

@bottle.route('/occasions')
def cs_occa():
    return bottle.template('occasions')
    
@bottle.route('/respuestaoccasions', method='POST')
def res_occa():
    return bottle.template('occasions')
    occa = bottle.request.forms.get("occa")
    ro=requests.get("https://api.groupon.com/v2/channels/occasions/deals.json", params = {"client_id":"eb9ff18a490c1d0e00419123560879fa1b16e02d","status":"open"})
    tituloo = json.loads(ro.text)["deals"][0]["announcementTitle"]
    resumeno = json.loads(ro.text)["deals"][0]["finePrint"]
    imageno =json.loads(ro.text)["deals"][0]["grid4ImageUrl"]
    datoso = json.loads(ro.text)["deals"][0]["highlightsHtml"]
    precioo = json.loads(ro.text)["deals"][0]["options"][0]["discount"]["formattedAmount"]
    fechafino = json.loads(ro.text)["deals"][0]["options"][0]["endAt"]
    descripciono = json.loads(ro.text)["deals"][0]["options"][0]["details"][0]["description"]
    return bottle.template("respuestaoccasions", tituloo=tituloo, resumeno=resumeno, imageno=imageno, datoso=datoso, precioo=precioo, fechafino=fechafino, descripciono=descripciono )


bottle.debug(True)
bottle.run(host='localhost', port=8080)





