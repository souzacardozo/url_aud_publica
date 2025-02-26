from flask import Flask, jsonify, request
from flask_cors import CORS

from service.receitasOrcadasArrecadadasService import ReceitasOrcadasArrecadadasService
from service.receitasOrcadasArrecadadasGraficosService import ReceitasOrcadasArrecadadasGraficosService
from service.receitasOrcadasArrecadadasPropriosService import ReceitasOrcadasArrecadadasPropriosService
from service.receitasOrcadasArrecadadasPropriosGraficosService import ReceitasOrcadasArrecadadasPropriosGraficosService
from service.receitasOrcadasArrecadadasFederaisService import ReceitasOrcadasArrecadadasFederaisService
from service.receitasOrcadasArrecadadasFederaisGraficosService import ReceitasOrcadasArrecadadasFederaisGraficosService
from service.receitasOrcadasArrecadadasEstaduaisService import ReceitasOrcadasArrecadadasEstaduaisService
from service.receitasOrcadasArrecadadasEstaduaisGraficosService import ReceitasOrcadasArrecadadasEstaduaisGraficosService
from service.despesaOrcadaEmpenhadaPagaService import DespesaOrcadaEmpenhadaPagaService

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})

# Create separate instances of each service
receitas_orcadas_arrecadadas_service = ReceitasOrcadasArrecadadasService()
receitas_orcadas_arrecadadas_graficos_service = ReceitasOrcadasArrecadadasGraficosService()
receitas_orcadas_arrecadadas_proprias_service = ReceitasOrcadasArrecadadasPropriosService()
receitas_orcadas_arrecadadas_proprias_graficos_service = ReceitasOrcadasArrecadadasPropriosGraficosService()
receitas_orcadas_arrecadadas_federais_service = ReceitasOrcadasArrecadadasFederaisService()
receitas_orcadas_arrecadadas_federais_graficos_service = ReceitasOrcadasArrecadadasFederaisGraficosService()
receitas_orcadas_arrecadadas_estaduais_service = ReceitasOrcadasArrecadadasEstaduaisService()
receitas_orcadas_arrecadadas_estaduais_graficos_service = ReceitasOrcadasArrecadadasEstaduaisGraficosService()
despesa_orcada_empenhada_paga_service = DespesaOrcadaEmpenhadaPagaService()


@app.route('/api/receitasOrcadasArrecadadas', methods=['GET'])
def obter_receitasOrcadasArrecadadas():
    entidades = request.args.getlist('entidades', type=str) 
    idquadrimestres = request.args.getlist('idquadrimestres', type=str)
    ano = request.args.getlist('ano', type=int)


    
    print(f"Entidades: {entidades}")
    print(f"ID Quadrimestres: {idquadrimestres}")
    print(f"Ano: {ano}")

    if not entidades:
        return jsonify({"error": "entidades são obrigatórios"}), 400 

    if not idquadrimestres:
        return jsonify({"error": "idquadrimestres são obrigatórios"}), 400
    if idquadrimestres == 1:
        idquadrimestres = request.args.getlist('idquadrimestres', type=int)
    else:
        idquadrimestres = request.args.getlist('idquadrimestres', type=str)
    
    if not ano:
        return jsonify({"error": "ano é obrigatório"}), 400

    try:
        receitas = receitas_orcadas_arrecadadas_service.obter_receitasOrcadasArrecadadas(entidades, idquadrimestres, ano)
        return jsonify(receitas), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/api/receitasOrcadasArrecadadasGraficos', methods=['GET'])
def obter_receitasOrcadasArrecadadasGraficos():
    entidades = request.args.getlist('entidades', type=str) 
    idquadrimestres = request.args.getlist('idquadrimestres', type=str)
    ano = request.args.getlist('ano', type=int)


    
    print(f"Entidades: {entidades}")
    print(f"ID Quadrimestres: {idquadrimestres}")
    print(f"Ano: {ano}")

    if not entidades:
        return jsonify({"error": "entidades são obrigatórios"}), 400 

    if not idquadrimestres:
        return jsonify({"error": "idquadrimestres são obrigatórios"}), 400
    if idquadrimestres == 1:
        idquadrimestres = request.args.getlist('idquadrimestres', type=int)
    else:
        idquadrimestres = request.args.getlist('idquadrimestres', type=str)
    
    if not ano:
        return jsonify({"error": "ano é obrigatório"}), 400

    try:
        receitas = receitas_orcadas_arrecadadas_graficos_service.obter_receitasOrcadasArrecadadasGraficos(entidades, idquadrimestres, ano)
        return jsonify(receitas), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/api/receitasOrcadasArrecadadasProprios', methods=['GET'])
def obter_receitasOrcadasArrecadadasProprios():
    entidades = request.args.getlist('entidades', type=str) 
    idquadrimestres = request.args.getlist('idquadrimestres', type=str)
    ano = request.args.getlist('ano', type=int)


    
    print(f"Entidades: {entidades}")
    print(f"ID Quadrimestres: {idquadrimestres}")
    print(f"Ano: {ano}")

    if not entidades:
        return jsonify({"error": "entidades são obrigatórios"}), 400 

    if not idquadrimestres:
        return jsonify({"error": "idquadrimestres são obrigatórios"}), 400
    if idquadrimestres == 1:
        idquadrimestres = request.args.getlist('idquadrimestres', type=int)
    else:
        idquadrimestres = request.args.getlist('idquadrimestres', type=str)
    
    if not ano:
        return jsonify({"error": "ano é obrigatório"}), 400

    try:
        receitas = receitas_orcadas_arrecadadas_proprias_service.obter_receitasOrcadasArrecadadasPropriosService(entidades, idquadrimestres, ano)
        return jsonify(receitas), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/api/receitasOrcadasArrecadadasPropriosGraficos', methods=['GET'])
def obter_receitasOrcadasArrecadadasPropriosGraficos():
    entidades = request.args.getlist('entidades', type=str) 
    idquadrimestres = request.args.getlist('idquadrimestres', type=str)
    ano = request.args.getlist('ano', type=int)


    
    print(f"Entidades: {entidades}")
    print(f"ID Quadrimestres: {idquadrimestres}")
    print(f"Ano: {ano}")

    if not entidades:
        return jsonify({"error": "entidades são obrigatórios"}), 400 

    if not idquadrimestres:
        return jsonify({"error": "idquadrimestres são obrigatórios"}), 400
    if idquadrimestres == 1:
        idquadrimestres = request.args.getlist('idquadrimestres', type=int)
    else:
        idquadrimestres = request.args.getlist('idquadrimestres', type=str)
    
    if not ano:
        return jsonify({"error": "ano é obrigatório"}), 400

    try:
        receitas = receitas_orcadas_arrecadadas_proprias_graficos_service.obter_receitasOrcadasArrecadadasPropriosGraficosService(entidades, idquadrimestres, ano)
        return jsonify(receitas), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/api/receitasOrcadasArrecadadasEstaduais', methods=['GET'])
def obter_receitasOrcadasArrecadadasEstaduais():
    entidades = request.args.getlist('entidades', type=str) 
    idquadrimestres = request.args.getlist('idquadrimestres', type=str)
    ano = request.args.getlist('ano', type=int)


    
    print(f"Entidades: {entidades}")
    print(f"ID Quadrimestres: {idquadrimestres}")
    print(f"Ano: {ano}")

    if not entidades:
        return jsonify({"error": "entidades são obrigatórios"}), 400 

    if not idquadrimestres:
        return jsonify({"error": "idquadrimestres são obrigatórios"}), 400
    if idquadrimestres == 1:
        idquadrimestres = request.args.getlist('idquadrimestres', type=int)
    else:
        idquadrimestres = request.args.getlist('idquadrimestres', type=str)
    
    if not ano:
        return jsonify({"error": "ano é obrigatório"}), 400

    try:
        receitas = receitas_orcadas_arrecadadas_estaduais_service.obter_receitasOrcadasArrecadadasEstaduaisService(entidades, idquadrimestres, ano)
        return jsonify(receitas), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/api/receitasOrcadasArrecadadasEstaduaisGraficos', methods=['GET'])
def obter_receitasOrcadasArrecadadasEstaduaisGraficos():
    entidades = request.args.getlist('entidades', type=str) 
    idquadrimestres = request.args.getlist('idquadrimestres', type=str)
    ano = request.args.getlist('ano', type=int)


    
    print(f"Entidades: {entidades}")
    print(f"ID Quadrimestres: {idquadrimestres}")
    print(f"Ano: {ano}")

    if not entidades:
        return jsonify({"error": "entidades são obrigatórios"}), 400 

    if not idquadrimestres:
        return jsonify({"error": "idquadrimestres são obrigatórios"}), 400
    if idquadrimestres == 1:
        idquadrimestres = request.args.getlist('idquadrimestres', type=int)
    else:
        idquadrimestres = request.args.getlist('idquadrimestres', type=str)
    
    if not ano:
        return jsonify({"error": "ano é obrigatório"}), 400

    try:
        receitas = receitas_orcadas_arrecadadas_estaduais_graficos_service.obter_receitasOrcadasArrecadadasEstaduaisGraficosService(entidades, idquadrimestres, ano)
        return jsonify(receitas), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/api/receitasOrcadasArrecadadasFederais', methods=['GET'])
def obter_receitasOrcadasArrecadadasFederais():
    entidades = request.args.getlist('entidades', type=str) 
    idquadrimestres = request.args.getlist('idquadrimestres', type=str)
    ano = request.args.getlist('ano', type=int)


    
    print(f"Entidades: {entidades}")
    print(f"ID Quadrimestres: {idquadrimestres}")
    print(f"Ano: {ano}")

    if not entidades:
        return jsonify({"error": "entidades são obrigatórios"}), 400 

    if not idquadrimestres:
        return jsonify({"error": "idquadrimestres são obrigatórios"}), 400
    if idquadrimestres == 1:
        idquadrimestres = request.args.getlist('idquadrimestres', type=int)
    else:
        idquadrimestres = request.args.getlist('idquadrimestres', type=str)
    
    if not ano:
        return jsonify({"error": "ano é obrigatório"}), 400

    try:
        receitas = receitas_orcadas_arrecadadas_federais_service.obter_receitasOrcadasArrecadadasFederaisService(entidades, idquadrimestres, ano)
        return jsonify(receitas), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/api/receitasOrcadasArrecadadasFederaisGraficos', methods=['GET'])
def obter_receitasOrcadasArrecadadasFederaisGraficos():
    entidades = request.args.getlist('entidades', type=str) 
    idquadrimestres = request.args.getlist('idquadrimestres', type=str)
    ano = request.args.getlist('ano', type=int)


    
    print(f"Entidades: {entidades}")
    print(f"ID Quadrimestres: {idquadrimestres}")
    print(f"Ano: {ano}")

    if not entidades:
        return jsonify({"error": "entidades são obrigatórios"}), 400 

    if not idquadrimestres:
        return jsonify({"error": "idquadrimestres são obrigatórios"}), 400
    if idquadrimestres == 1:
        idquadrimestres = request.args.getlist('idquadrimestres', type=int)
    else:
        idquadrimestres = request.args.getlist('idquadrimestres', type=str)
    
    if not ano:
        return jsonify({"error": "ano é obrigatório"}), 400

    try:
        receitas = receitas_orcadas_arrecadadas_federais_graficos_service.obter_receitasOrcadasArrecadadasFederaisGraficosService(entidades, idquadrimestres, ano)
        return jsonify(receitas), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

@app.route('/api/despesasOrcadaEmpenhadaPaga', methods=['GET'])
def obter_despesasOrcadaEmpenhadaPaga():
    entidades = request.args.getlist('entidades', type=str) 
    idquadrimestres = request.args.getlist('idquadrimestres', type=str)
    ano = request.args.getlist('ano', type=int)


    
    print(f"Entidades: {entidades}")
    print(f"ID Quadrimestres: {idquadrimestres}")
    print(f"Ano: {ano}")

    if not entidades:
        return jsonify({"error": "entidades são obrigatórios"}), 400 

    if not idquadrimestres:
        return jsonify({"error": "idquadrimestres são obrigatórios"}), 400
    if idquadrimestres == 1:
        idquadrimestres = request.args.getlist('idquadrimestres', type=int)
    else:
        idquadrimestres = request.args.getlist('idquadrimestres', type=str)
    
    if not ano:
        return jsonify({"error": "ano é obrigatório"}), 400

    try:
        despesas = despesa_orcada_empenhada_paga_service.obter_despesaOrcadaEmpenhadaPagaService(entidades, idquadrimestres, ano)
        print(despesas)
        if not despesas:
           raise ValueError("Nenhuma despesa encontrada.")
        return jsonify(despesas), 200    
    except Exception as e:
        return jsonify({"error": str(e)}), 500    


if __name__ == '__main__':
    app.run(debug=True, port=8888)
