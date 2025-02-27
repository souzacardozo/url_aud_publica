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

from service.despesasOrcadasEmpenhadasService import DespesasOrcadasEmpenhadasService
from service.despesasOrcadasEmpenhadasGraficosService import DespesasOrcadasEmpenhadasGraficosService
from service.despesasOrcadasEmpenhadasPorSecretariasService import DespesasOrcadasEmpenhadasPorSecretariasService
from service.despesasOrcadasEmpenhadasPorSecretariasGraficosService import DespesasOrcadasEmpenhadasPorSecretariasGraficosService
from service.despesasOrcadasEmpenhadasPagasService import DespesasOrcadasEmpenhadasPagasService
from service.despesasOrcadasEmpenhadasPagasGraficosService import DespesasOrcadasEmpenhadasPagasGraficosService
from service.despesasOrcadasEmpenhadasPagasPorSecretariasService import DespesasOrcadasEmpenhadasPagasPorSecretariasService
from service.despesasOrcadasEmpenhadasPagasPorSecretariasGraficosService import DespesasOrcadasEmpenhadasPagasPorSecretariasGraficosService

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

despesas_orcadas_empenhadas_service = DespesasOrcadasEmpenhadasService()
despesas_orcadas_empenhadas_graficos_service =  DespesasOrcadasEmpenhadasGraficosService()
despesas_orcadas_empenhadas_por_secretaria_service = DespesasOrcadasEmpenhadasPorSecretariasService()
despesas_orcadas_empenhadas_por_secretaria_graficos_service =  DespesasOrcadasEmpenhadasPorSecretariasGraficosService()
despesas_orcadas_empenhadas_pagas_service = DespesasOrcadasEmpenhadasPagasService()
despesas_orcadas_empenhadas_pagas_graficos_service =  DespesasOrcadasEmpenhadasPagasGraficosService()
despesas_orcadas_empenhadas_pagas_por_secretarias_service = DespesasOrcadasEmpenhadasPagasPorSecretariasService()
despesas_orcadas_empenhadas_pagas_por_secretarias_graficos_service =  DespesasOrcadasEmpenhadasPagasPorSecretariasGraficosService()


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
    

@app.route('/api/despesasOrcadasEmpenhadas', methods=['GET'])
def obter_despesassOrcadasEmpenhadas():
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
        despesas = despesas_orcadas_empenhadas_service.obter_despesasOrcadasEmpenhadasService(entidades, idquadrimestres, ano)
        print(despesas)
        if not despesas:
           raise ValueError("Nenhuma despesa encontrada.")
        return jsonify(despesas), 200    
    except Exception as e:
        return jsonify({"error": str(e)}), 500   
    

@app.route('/api/despesasOrcadasEmpenhadasGraficos', methods=['GET'])
def obter_despesassOrcadasEmpenhadasGraficos():
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
        despesas = despesas_orcadas_empenhadas_graficos_service.obter_despesasOrcadasEmpenhadasGraficosService(entidades, idquadrimestres, ano)
        print(despesas)
        if not despesas:
           raise ValueError("Nenhuma despesa encontrada.")
        return jsonify(despesas), 200    
    except Exception as e:
        return jsonify({"error": str(e)}), 500    
    

@app.route('/api/despesasOrcadasEmpenhadasPorSecretarias', methods=['GET'])
def obter_despesassOrcadasEmpenhadasPorSecretarias():
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
        despesas = despesas_orcadas_empenhadas_por_secretaria_service.obter_despesasOrcadasEmpenhadasPorSecretariasService(entidades, idquadrimestres, ano)
        print(despesas)
        if not despesas:
           raise ValueError("Nenhuma despesa encontrada.")
        return jsonify(despesas), 200    
    except Exception as e:
        return jsonify({"error": str(e)}), 500   
    

@app.route('/api/despesasOrcadasEmpenhadasPorSecretariasGraficos', methods=['GET'])
def obter_despesassOrcadasEmpenhadasPorSecretariasGraficos():
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
        despesas = despesas_orcadas_empenhadas_por_secretaria_graficos_service.obter_despesasOrcadasEmpenhadasPorSecretariasGraficosService(entidades, idquadrimestres, ano)
        print(despesas)
        if not despesas:
           raise ValueError("Nenhuma despesa encontrada.")
        return jsonify(despesas), 200    
    except Exception as e:
        return jsonify({"error": str(e)}), 500      
    

@app.route('/api/despesasOrcadasEmpenhadasPagas', methods=['GET'])
def obter_despesassOrcadasEmpenhadasPagas():
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
        despesas = despesas_orcadas_empenhadas_pagas_service.obter_despesasOrcadasEmpenhadasPagasService(entidades, idquadrimestres, ano)
        print(despesas)
        if not despesas:
           raise ValueError("Nenhuma despesa encontrada.")
        return jsonify(despesas), 200    
    except Exception as e:
        return jsonify({"error": str(e)}), 500   
    

@app.route('/api/despesasOrcadasEmpenhadasPagasGraficos', methods=['GET'])
def obter_despesassOrcadasEmpenhadasPagasGraficos():
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
        despesas = despesas_orcadas_empenhadas_pagas_graficos_service.obter_despesasOrcadasEmpenhadasPagasGraficosService(entidades, idquadrimestres, ano)
        print(despesas)
        if not despesas:
           raise ValueError("Nenhuma despesa encontrada.")
        return jsonify(despesas), 200    
    except Exception as e:
        return jsonify({"error": str(e)}), 500        
    

@app.route('/api/despesasOrcadasEmpenhadasPagasPorSecretarias', methods=['GET'])
def obter_despesassOrcadasEmpenhadasPagasPorSecretarias():
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
        despesas = despesas_orcadas_empenhadas_pagas_por_secretarias_service.obter_despesasOrcadasEmpenhadasPagasPorSecretariasService(entidades, idquadrimestres, ano)
        print(despesas)
        if not despesas:
           raise ValueError("Nenhuma despesa encontrada.")
        return jsonify(despesas), 200    
    except Exception as e:
        return jsonify({"error": str(e)}), 500   
    

@app.route('/api/despesasOrcadasEmpenhadasPagasPorSecretariasGraficos', methods=['GET'])
def obter_despesassOrcadasEmpenhadasPagasPorSecretariasGraficos():
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
        despesas = despesas_orcadas_empenhadas_pagas_por_secretarias_graficos_service.obter_despesasOrcadasEmpenhadasPagasPorSecretariasGraficosService(entidades, idquadrimestres, ano)
        print(despesas)
        if not despesas:
           raise ValueError("Nenhuma despesa encontrada.")
        return jsonify(despesas), 200    
    except Exception as e:
        return jsonify({"error": str(e)}), 500     


if __name__ == '__main__':
    app.run(debug=True, port=8888)
