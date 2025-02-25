from flask import Flask, jsonify, request
from service.despesaOrcadaPagaService import DespesaOrcadaPagaService
from service.receitasOrcadasArrecadadasSevice import ReceitasOrcadasArrecadadasService
from service.receitasPropriasArrecadadasSevice import ReceitasPropriasArrecadadasService


app = Flask(__name__)

# Create separate instances of each service
despesa_service = DespesaOrcadaPagaService()
receitas_orcadas_service = ReceitasOrcadasArrecadadasService()
receitas_proprias_service = ReceitasPropriasArrecadadasService()


@app.route('/api/despesas', methods=['GET'])
def obter_despesas():
    idquadrimestres = request.args.getlist('idquadrimestres', type=int)
    if not idquadrimestres:
        return jsonify({"error": "idquadrimestres são obrigatórios"}), 400

    try:
        despesas = despesa_service.obter_despesas(idquadrimestres)
        return jsonify(despesas), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/api/receitasOrcadasArrecadadas', methods=['GET'])
def obter_receitasOrcadasArrecadadas():
    idquadrimestres = request.args.getlist('idquadrimestres', type=int)
    if not idquadrimestres:
        return jsonify({"error": "idquadrimestres são obrigatórios"}), 400

    try:
        receitas = receitas_orcadas_service.obter_receitasOrcadasArrecadadas(idquadrimestres)
        return jsonify(receitas), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/api/receitasOrcadasArrecadadasProprias', methods=['GET'])
def obter_receitasPropriasArrecadadas():
    entidades = request.args.getlist('entidades', type=str)
    idquadrimestres = request.args.getlist('idquadrimestres', type=int)
    ano = request.args.getlist('ano', type=int)


    
    print(f"Entidades: {entidades}")
    print(f"ID Quadrimestres: {idquadrimestres}")
    print(f"Ano: {ano}")

    if not entidades:
        return jsonify({"error": "entidades são obrigatórios"}), 400 

    if not idquadrimestres:
        return jsonify({"error": "idquadrimestres são obrigatórios"}), 400
    
    if not ano:
        return jsonify({"error": "ano é obrigatório"}), 400

    try:
        receitas = receitas_proprias_service.obter_receitasPropriasArrecadadas(entidades, idquadrimestres, ano)
        return jsonify(receitas), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True, port=8888)
