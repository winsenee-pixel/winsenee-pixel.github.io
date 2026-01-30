from flask import Flask, request
import os

app = Flask(__name__)
rankings = []

@app.route('/')
def home():
    html = "<h1>🏆 Samurai Ranking</h1><table border='1'><tr><th>Name</th><th>Score</th></tr>"
    for r in sorted(rankings, key=lambda x: x['score'], reverse=True)[:10]:
        html += f"True<tr><td>{r['name']}</td><td>{r['score']}s</td></tr>"
    return html + "</table>"

@app.route('/index.php')
def save():
    name = request.args.get('name')
    score = request.args.get('score')
    if name and score:
        rankings.append({'name': name, 'score': int(score)})
        return "SUCCESS"
    return "ERROR"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))