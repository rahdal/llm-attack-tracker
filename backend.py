from flask import Flask, jsonify, request
from flask_cors import CORS
from arxiv_checker import get_recent_papers

app = Flask(__name__)
CORS(app)  # This line enables CORS for all routes

@app.route('/arxiv_papers', methods=['GET'])
def arxiv_papers():
    num_papers = request.args.get('num_papers', default=1, type=int)
    return jsonify(get_recent_papers(num_papers=num_papers))
