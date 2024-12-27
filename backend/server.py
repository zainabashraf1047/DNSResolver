from flask import Flask, request, jsonify
from dns_resolver import resolve

app = Flask(__name__)

@app.route('/resolve', methods=['POST'])
def resolve_domain():
    data = request.json
    domain = data.get('domain')
    query_type = data.get('query_type')
    method = data.get('method')

    if not domain or not query_type or not method:
        return jsonify({'error': 'Invalid input'}), 400

    results = resolve(domain, query_type, method)
    return jsonify({'results': results})

if __name__ == '__main__':
    app.run(debug=True)
