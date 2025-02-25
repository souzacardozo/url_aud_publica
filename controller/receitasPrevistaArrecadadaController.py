from flask import Flask, jsonify, request
from service import receitasPrevistaArrecadadaSevice

app = Flask(__name__)
service =  receitasPrevistaArrecadadaSevice()

@app.route('/api/receitasPrevistaArrecadada', methods=['GET'])
def obter_despesas():
    idquadrimestres = request.args.getlist('idquadrimestres', type=int)
    if not idquadrimestres:
        return jsonify({"error": "idquadrimestres são obrigatórios"}), 400

    try:
        receitas = service.obter_receitasPrevistaArrecadada(idquadrimestres)
        return jsonify(receitas), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)