# Reference
# https://medium.com/@twilightlau94/rest-apis-with-flask-%E7%B3%BB%E5%88%97%E6%95%99%E5%AD%B8%E6%96%87-1-5405216d3166

from flask import Flask, jsonify, request

app = Flask(__name__)

# default data
stores = [{
    'name': 'first',
    'items': [{'name':'my item 1', 'price': 30}]
    },
    {
    'name': 'second',
    'items': [{'name':'my item 2', 'price': 15}]
    }
]

# post /store data: {name :}
@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name':request_data['name'],
        'items':[]
    }
    stores.append(new_store)
    return jsonify(new_store)

# get /store/<name> data: {name :}
@app.route('/store/<string:name>')
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify ({'message': 'store not found'})

# get /store
@app.route('/store')
def get_stores():
    return jsonify(stores)

# post /store/<name> data: {name :}/item
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            stores.remove(store)
    new_item = {
        'name':request_data['name1'],
        'items':[{
            'name': request_data['name2'],
            'price': request_data['price']
        }]
    }   
    stores.append(new_item)
    return jsonify(new_item)

# get /store/<name>/item data: {name :}/item
@app.route('/store/<string:name>/item')
def get_item_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items':store['items']})
    return jsonify ({'message':'store not found'})

# start service
app.run(host='0.0.0.0', port=8080, debug=True)