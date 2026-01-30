from flask import Flask, render_template_string, request

app = Flask(__name__)

# [cite: 2026-01-30] 인피니티프리 DB 대신 Render 메모리에 저장 (실시간 반영용)
ranking_data = [{"name": "Hero", "score": 100}]

@app.route('/')
@app.route('/index.php')
def index():
    global ranking_data
    name = request.args.get('name')
    score = request.args.get('score')
    
    if name and score:
        ranking_data.append({"name": name, "score": int(score)})
        ranking_data = sorted(ranking_data, key=lambda x: x['score'], reverse=True)[:10]
        return "SUCCESS"

    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8"><title>Samurai Rankings</title>
        <style>
            body { background: #1a1a2e; color: white; text-align: center; font-family: arial; padding-top: 50px; }
            h1 { color: gold; }
            table { margin: 20px auto; border-collapse: collapse; width: 450px; background: #16213e; }
            th, td { padding: 15px; border: 1px solid #0f3460; text-align: center; }
            th { background: #0f3460; color: gold; }
        </style>
    </head>
    <body>
        <h1>🏆 Samurai World Rankings</h1>
        <table>
            <tr><th>Rank</th><th>Name</th><th>Score</th></tr>
            {% for row in rows %}
            <tr><td>{{ loop.index }}</td><td>{{ row.name }}</td><td>{{ row.score }}s</td></tr>
            {% endfor %}
        </table>
    </body>
    </html>
    """
    return render_template_string(html, rows=ranking_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
