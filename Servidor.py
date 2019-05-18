from flask import Flask, jsonify, request
import sqlite3  
from flask import Blueprint, jsonify, request
import request as con

database = {

}
app = Flask(__name__)
usuario_app = Blueprint('usuario_app', __name__, template_folder='templates')

@route('/')
def all():
    return jsonify



if __name__ == '__main__':
    res = input('Você quer criar o  banco de dados?')
    if res == 's':
     con = sqlite3.connect('banco_dados')
     cur = con.cursor()

#Inicio

cur.execute("create table usuario( id integer, nome varchar(100), segredo varchar(10))"),


cur.execute("create table mensagem( id_mensagem integer, id_remetente integer, id_destinatario integer, data datetime,texto varchar(300))"),

#Fim 

    #cur.execute("insert into usuario(id_usuario,nome,segredo)values(:id_usuario,:nome,:segredo)")
    #cur.execute("select * from usuario)")

    con.commit()
    con.close()
app.run(host='localhost', port=5000)