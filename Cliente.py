from flask import request, jsonify, Blueprint 
import requests as cur


response = cur.get('http://localhost:5000/')

usuario_app = Blueprint('usuario_app',__name__, template__folder='templates')
usuario_db = []

mensagem__app = Blueprint('mensagem__app',__name__, template__folder='templates')
mensagem_db = []


@usuario_app.route('/usuario', methods=['GET'])
def listar():
    return jsonify(usuario_db)

@usuario_app.route('/usuario', methods=['POST'])
def novo():
    novo_usuario = request.get_json()
    usuario_db.append(novo_usuario)
    return jsonify(usuario_db)


@mensagem__app.route('mensagem', methods=['GET'])
def listar():
    return jsonify(mensagem_db)

@mensagem_app.route('/mensagem', methods=['POST'])
def nova_mensagem():
    nova_mensagem = request.get_json()
    mensagem_db.append(nova_mensagem)
    return jsonify(mensagem_db) 



print("1 - cadastrar um novo usuário:")
print("2 - listar usuários cadastrados em sistema:")
print("3 - Enviar uma Mensagem:")
print("4 - Listar Mensagens enviadas:")




    