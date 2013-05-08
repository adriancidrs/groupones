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
    id_escrito = bottle.request.forms.get("id_escrito")
    r = requests.get("https://api.groupon.com/v2/channels/goods/deals.json", params = {"client_id":"eb9ff18a490c1d0e00419123560879fa1b16e02d","status":"open"})
    nombre = json.loads(r.text)["deals"][0]["merchant"]["name"]
    resum = json.loads(r.text)["deals"][0]["dealTypes"][0]["description"]
    fechafini = json.loads(r.text)["deals"][0]["endAt"]
    precio = json.loads(r.text)["deals"][0]["options"][0]["discount"]["formattedAmount"]
    descripcion = json.loads(r.text)["deals"][0]["finePrint"]
    imagen = json.loads(r.text)["deals"][0]["grid4ImageUrl"]
    imagenpeq = json.loads(r.text)["deals"][0]["mediumImageUrl"]
    return bottle.template("respuestagoods", nombre=nombre, resum=resum, fechafini=fechafini, precio=precio, descripcion=descripcion, imagen=imagen, imagenpeq=imagenpeq)

@bottle.route('/occasions')
def cs_occa():
    return bottle.template('occasions')
    
@bottle.route('/respuestaoccasions', method='POST')
def res_occa():
    return bottle.template('occasions')
    id_escrito = bottle.request.forms.get("id_escrito")
    r=requests.get("https://api.groupon.com/v2/channels/occasions/deals.json", params = {"client_id":"eb9ff18a490c1d0e00419123560879fa1b16e02d","status":"open"})
    titulo = json.loads(r.text)["deals"][0]["announcementTitle"]
    resumen = json.loads(r.text)["deals"][0]["finePrint"]
    imagen =json.loads(r.text)["deals"][0]["grid4ImageUrl"]
    datos = json.loads(r.text)["deals"][0]["highlightsHtml"]
    precio = json.loads(r.text)["deals"][0]["options"][0]["discount"]["formattedAmount"]
    fechafin = json.loads(r.text)["deals"][0]["options"][0]["endAt"]
    descripcion = json.loads(r.text)["deals"][0]["options"][0]["details"][0]["description"]
    return bottle.template("respuestaoccasions", titulo=titulo, resumen=resumen, imagen=imagen, datos=datos, precio=precio, fechafin=fechafin, descripcion=descripcion )


bottle.debug(True)
bottle.run(host='localhost', port=8080)
