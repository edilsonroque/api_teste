from flask import Flask, jsonify, request

app = Flask(__name__)

province_names = [
    {   'id': 1,
        'country_name': 'Mozambique',
        'capital': 'Maputo',
        'provinces': ['Nampula', 'Gaza', 'Inhambane', 'Manica', 'Sofala', 'Tete', 'Cabo-Delgado', 'Niassa']
    },
    {   
        'id': 2,
        'country_name': 'South-Africa',
        'capital': 'Pretória',
        'provinces': ['Cape Town', 'Kimberley', 'Mbombela', 'Johannesburg', 'Bhisho']
    }
]

#lista de nome de provincias
@app.route('/province', methods=['GET'])
def get_province():
    return jsonify(province_names)

#busca por provincias por id
@app.route('/province/<int:id>',methods=['GET'])
def get_province_id(id):
    for province in province_names:
        if province.get('id') == id:
            return jsonify(province)
        
#add provincias
@app.route('/province', methods=['POST'])
def add_province():
    new_province = request.get_json()
    province_names.append(new_province)


#Editar provincia
@app.route('/province/<int:id>',methods=['PUT'])
def edit_province(id):
    province_alt = request.get_json()
    for indice, province in enumerate(province_names):
        if province.get('id') == id:
            province_names[indice].update(province_alt)
            return jsonify(province_names[indice])
        

#Deletar provincia
@app.route('/province/<int:id>',methods=['DELETE'])
def del_province(id):
    for indice, province in enumerate(province_names):
        if province.get('id') == id:
            del province_names[indice]
    
    return jsonify(province_names)

app.run(port=5000, host='localhost', debug=True)