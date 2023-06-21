from apiflask import APIFlask
from flask import request, jsonify
from markupsafe import escape

#flask run --reload

app = APIFlask(__name__)

@app.route('/api/ping')
def hello():
    return f'pong'

@app.route('/api/olx/getOffers')
def get_olx_offers():
    return f'Get OLX offers'

@app.route('/api/otomoto/getOffers')
def get_otomoto_offers():
    return f'Get Otomoto offers'

@app.route('/api/offers/findOffer', methods=['GET'])
def find_offer():
    content = request.json
    print(content['manufacturer'])
    return jsonify({"car1":"XD"})
