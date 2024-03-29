from flask import Flask, jsonify, request
from arxiv_checker import get_recent_papers

app = Flask(__name__)

@app.route('/arxiv_papers', methods=['GET'])
def arxiv_papers():
    num_papers = request.args.get('num_papers', default=1, type=int)
    return jsonify(get_recent_papers(num_papers=num_papers))
