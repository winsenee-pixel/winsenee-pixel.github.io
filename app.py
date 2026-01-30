from flask import Flask, render_template_string, request
import pymysql

app = Flask(__name__)

# 인피니티프리 DB 정보 [cite: 2026-01-30]
db_config = {
    'host': 'sql310.infinityfree.com',
    'user': 'if0_41018891',
    'password': 'idkiller1379',
    'db': 'if0_41018891_ranking',
    'charset': 'utf8mb4',
    'cursorclass': pymysql.cursors.DictCursor
}

@app.route('/')
@app.route('/index.php')  # 게임에서 index.php로 요청해도 처리 가능하게 설정 [cite: 2026-01-30]
def index():
    # 점수 저장 기능 [cite: 2026-01-30]
    name = request.args.get('name')
    score = request.args.get('score')
    
    try:
        conn = pymysql.connect(**db_config)
        with conn.cursor() as cursor:
            if name and score:
                sql = "INSERT INTO ranking (name, score) VALUES (%s, %s)"
                cursor.execute(sql, (name, int(score)))
                conn.commit()
            
            # 랭킹 가져오기 [cite: 2026-01-30]
            cursor.execute("SELECT name, score FROM ranking ORDER BY score DESC LIMIT 10")
            rows = cursor.fetchall()
        conn.close()
    except Exception as e:
        return f"DATABASE ERROR: {str(e)}" # 에러 발생 시 상세 내용 출력 [cite: 2026-01-30]

    # 등수가 포함된 HTML 디자인 [cite: 2026-01-30]
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>Samurai World Rankings</title>
        <style>
            body { background: #1a1a2e; color: white; text-align: center; font-family: arial; padding-top: 50px; }
            h1 { color: gold; }
            table { margin: 20px auto; border-collapse: collapse; width: 450px; background: #16213e; }
            th, td { padding: 15px; border: 1px solid #0f3460; text-align: center; }
            th { background: #0f3460; color: gold; }
            tr:nth-child(even) { background: #1b264f; }
        </style>
    </head>
    <body>
        <h1>🏆 Samurai World Rankings</h1>
        <table>
            <tr><th>Rank</th><th>Name</th><th>Score</th></tr>
            {% for row in rows %}
            <tr>
                <td>{{ loop.index }}</td>
                <td>{{ row.name }}</td>
                <td>{{ row.score }}s</td>
            </tr>
            {% endfor %}
        </table>
    </body>
    </html>
    """
    return render_template_string(html, rows=rows)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
