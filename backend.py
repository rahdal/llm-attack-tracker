from flask import Flask, jsonify, request
from flask_cors import CORS
from arxiv_checker import get_recent_papers
import json

app = Flask(__name__)
CORS(app)  # This line enables CORS for all routes

def load_manual_attacks():
    try:
        with open('manual_attacks.json', 'r') as file:
            manual_attacks = json.load(file)
        return manual_attacks
    except Exception as e:
        print("Error loading manual attacks:", e)
        return []

@app.route('/arxiv_papers', methods=['GET'])
def arxiv_papers():
    num_papers = request.args.get('num_papers', default=1, type=int)
    recent_papers = get_recent_papers(num_papers=num_papers)
    manual_attacks = load_manual_attacks()
    recent_papers.extend(manual_attacks)
    return jsonify(recent_papers)

if __name__ == "__main__":
    app.run(debug=True)