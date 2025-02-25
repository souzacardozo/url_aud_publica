from flask import Flask, jsonify, request
from service.despesaOrcadaPagaService import DespesaOrcadaPagaService
from service.receitasPrevistaArrecadadaSevice import ReceitasPrevistaArrecadadaService


app = Flask(__name__)
service = DespesaOrcadaPagaService()
service = ReceitasPrevistaArrecadadaService()

@app.route('/api/despesas', methods=['GET'])
def obter_despesas():
    idquadrimestres = request.args.getlist('idquadrimestres', type=int)
    if not idquadrimestres:
        return jsonify({"error": "idquadrimestres são obrigatórios"}), 400

    try:
        despesas = service.obter_despesas(idquadrimestres)
        return jsonify(despesas), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@app.route('/api/receitasPrevistaArrecadada', methods=['GET'])
def obter_receitasPrevistasArrecadadas():
    idquadrimestres = request.args.getlist('idquadrimestres', type=int)
    if not idquadrimestres:
        return jsonify({"error": "idquadrimestres são obrigatórios"}), 400

    try:
        receitas = service.obter_receitasPrevistaArrecadada(idquadrimestres)
        return jsonify(receitas), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500 
    

if __name__ == '__main__':
    app.run(debug=True, port=8888)
