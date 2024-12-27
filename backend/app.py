from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import dns.resolver
from logger import log_query, export_log_to_json, export_log_to_csv  # Import log_query

import os
from logger import export_log_to_json, export_log_to_csv

app = Flask(__name__)
CORS(app)

@app.route('/resolve', methods=['POST'])
def resolve_dns():
    data = request.get_json()
    domain = data.get('domain')
    query_type = data.get('query_type', 'A')
    try:
        resolver = dns.resolver.Resolver()
        answers = resolver.resolve(domain, query_type)
        results = [answer.to_text() for answer in answers]
        # Log the query and result
        log_query(domain, results)
        return jsonify({'results': results})
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/export/json', methods=['GET'])
def export_logs_json():
    try:
        export_log_to_json()
        return send_file(
            "dns_queries.json",
            as_attachment=True,
            mimetype="application/json",
            download_name="dns_queries.json"
        )
    except Exception as e:
        return jsonify({'message': f"Error exporting logs to JSON: {e}"})

@app.route('/export/csv', methods=['GET'])
def export_logs_csv():
    try:
        export_log_to_csv()
        return send_file(
            "dns_queries.csv",
            as_attachment=True,
            mimetype="text/csv",
            download_name="dns_queries.csv"
        )
    except Exception as e:
        return jsonify({'message': f"Error exporting logs to CSV: {e}"})

if __name__ == '__main__':
    app.run(debug=True)
