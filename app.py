from flask import Flask, render_template, request, jsonify
from ai_engine.generator import generate_creative
from rules_engine.tesco_rules import validate_creative

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    creative = generate_creative(data)
    validation = validate_creative(creative)
    return jsonify({'creative': creative, 'validation': validation})

if __name__ == '__main__':
    app.run(debug=True)
