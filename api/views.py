from flask import json, jsonify, request
from data.setup_db import create_db
def health():
    """
    Status da API
    """
    responseBody = {
        "status": "Service Running"
    }
    return jsonify(responseBody)

def insert():
    valorReq  = request.args.get('valor')
    dataCompraReq = request.args.get('data_compra')
    descricaoReq = request.args.get('descricao')
    tipoPagamentoReq = request.args.get('tipo_pagamento_id')
    categoriaReq = request.args.get('categoria_id')

    try:
        db = create_db()
        cursor = db.cursor()
        cursor.execute("INSErT INTO despesas (valor, data_compra, descricao, tipo_pagamento_id, categoria_id) "
                       "VALUES(?, ?, ?, ?, ?)",
                       (valorReq, dataCompraReq, descricaoReq, tipoPagamentoReq, categoriaReq))
        db.commit()
        data = cursor.lastrowid
    except:
        db.rollback()

    finally:
        db.close()
        if data != '':
            success = True
        else:
            success = False
    responseBody = {
        "data": data,
        "success": success
    }
    return jsonify(responseBody)
def get():
    db = create_db()
    cursor = db.cursor()
    data = cursor.execute("SELECT * FROM despesas WHERE data_compra BETWEEN Date('now','start of month') "
                          "AND Date('now','start of month','+1 month','-1 day') ")
    db.close()
    if data != '':
        success = True
    else:
        success = False
    responseBody = {
        "data": data,
        "success": success
    }
    return jsonify(responseBody)
