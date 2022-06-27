from flask import Flask, jsonify, request 
from flask_cors import CORS
import uuid

app = Flask(__name__)

app.config.from_object(__name__)

CORS(app, resources={r"/*":{'origins':"*"}})
# CORS(app, resources={r'/*':{'origins': 'http://localhost:8080',"allow_headers": "Access-Control-Allow-Origin"}})

# hello world route
@app.route('/', methods=['GET'])
def greetings():
    return("Hello, world!")


EMPRESAS = [
    {   'id': uuid.uuid4().hex,
        'empresa':'sx group',
        'cnpj': 3100,
        'email': 'sx@gmail.com',
        'telefone': 37710758,
        'endereco': 'alameda',
        'colaboradores': ['joao']
    },
    {   'id': uuid.uuid4().hex,
        'empresa':'xx group',
        'cnpj': 31002,
        'email': 'xx@gmail.com',
        'telefone': 377107582,
        'endereco': 'alameda2',
        'colaboradores': ['joao2']
    },
]
USER = [
    {   'id': uuid.uuid4().hex,
        'nome':'othavio',
        'cpf': 114,
        'email': 'othavio@gmail.com',
        'telefone': 997140816,
        'endereco': 'varginha',
        'empresa': 'sx group'
    },
    {   'id': uuid.uuid4().hex,
        'nome':'Pedro',
        'cpf': 196,
        'email': 'pedro@gmail.com',
        'telefone': 994451600,
        'endereco': 'beira alta',
        'empresa': 'xx group'
    },
]


# The GET and POST route handler
@app.route('/login', methods=['GET', 'POST'])
def all_companies():
    response_object = {'status':'success'}
    if request.method == "POST":
        post_data = request.get_json()
        EMPRESAS.append({
            'id' : uuid.uuid4().hex,
            'empresa': post_data.get('nome'),
            'cnpj': post_data.get('cnpj'),
            'email': post_data.get('email'),
            'telefone': post_data.get('telefone'),
            'endereco': post_data.get('local')})
        response_object['message'] =  'company Added!'
    elif request.method == "GET":
        response_object['companies'] = EMPRESAS

    return jsonify(response_object)

@app.route('/user', methods=['GET', 'POST'])
def all_user():
    response_object = {'status':'success'}
    if request.method == "POST":
        post_data = request.get_json()
        USER.append({
            'id' : uuid.uuid4().hex,
            'empresa': post_data.get('empresa'),
            'nome': post_data.get('nome'),
            'cpf': post_data.get('cpf'),
            'email': post_data.get('email'),
            'telefone': post_data.get('telefone'),
            'endereco': post_data.get('local')})

        response_object['message'] =  'user Added!'
    elif request.method == "GET":
        response_object['users'] = USER

    return jsonify(response_object)


#The PUT and DELETE route handler
@app.route('/login/<company_id>', methods =['PUT', 'DELETE'])
def single_company(company_id):
    response_object = {'status':'success'}
    if request.method == "PUT":
        post_data = request.get_json()
        remove_company(company_id)
        EMPRESAS.append({
            'id' : uuid.uuid4().hex,
            'title': post_data.get('title'),
            'genre': post_data.get('genre'),
            'played': post_data.get('played')
        })
        response_object['message'] =  'company Updated!'
    if request.method == "DELETE":
        remove_company(company_id)
        response_object['message'] = 'company removed!'    
    return jsonify(response_object)


# Removing the company to update / delete
def remove_company(id):
    id = id.split(' ')
    if id[1]=='empresa':
        for company in EMPRESAS:
            if company['id'] == id[0]:
                EMPRESAS.remove(company)
                return True
        return False
    else:
        for usuario in USER:
            if usuario['id'] == id[0]:
                USER.remove(usuario)
                return True
        return False
        # return True



if __name__ == "__main__":
    app.run(debug=True)

