from flask import Flask, render_template, request, jsonify
import mariadb
import re

app = Flask(__name__)

# Database configuration
connection = mariadb.connect(
    host='', #add host
    user='', #add username
    password = '', #add password
    db='miRNA', #add database, miRNA in our case
    port= #add port
)
cursor = connection.cursor(dictionary=True)

@app.route('/')
def index():
    return render_template('npetruni_AJAX_and_charts.html')

@app.route('/histogram', methods=['GET'])
def histogram():
    gene = request.args.get('gene', '').strip()
    if not gene:
        return jsonify([])
    print(f"GENE RECEIVED: '{gene}'")
    cursor.execute(
        "SELECT t.score FROM targets t JOIN gene g ON t.gid = g.gid WHERE g.name = %s",
        (gene,)
    )
    rows = cursor.fetchall()
    scores = [row['score'] for row in rows]
    print("Histogram request for gene:", gene)
    print("Rows returned:", rows)
    return jsonify(scores)

@app.route('/gene_search', methods=['GET'])
def gene_search():
    seq = request.args.get('sequence', '').strip().upper()
    if not seq:
        return jsonify([])
    cursor.execute(
        "SELECT name, seq, chr, start, stop FROM gene WHERE seq REGEXP %s ORDER BY name ASC",
        (seq,)
    )
    rows = cursor.fetchall()
    results = []
    for row in rows:
        sequence_full = row['seq']
        match = re.search(seq, sequence_full)
        if match:
            start_index = max(match.start() - 5, 0)
            end_index = min(match.end() + 5, len(sequence_full))
            context = sequence_full[start_index:end_index]
            results.append({
                'gene': row['name'],
                'sequence_context': context,
                'chromosome': row['chr'],
                'start': row['start'],
                'stop': row['stop']
            })
    return jsonify(results)
