from flask import Flask, jsonify, request
from flask_cors import CORS
from urllib.parse import unquote
from Repo.News import News
from Repo.Linguistics import LinguisticFeatures
import json
from datetime import datetime
from langdetect import detect

app = Flask(__name__)

@app.route('/api/write_news_to_file', methods=['GET'])
def write_news_to_file():
    try:
        queries = request.args.get('queries')
        now = unquote(request.args.get('now'))
        if not queries or not now:
            return jsonify({"error": "Query parameter is required"}), 400
        file_name = f"latest_news_{str(datetime.now()).replace(' ', '_').replace(':', '_')}.txt"
        # path = "/home/abdelouahedlabrigui/Software/microservices/python-software/news"                
        with open(f'{file_name}', 'w', encoding='utf-8') as f:
            for query in queries.split(','):
                news = News(query=query, now=now)
                articles = news.request_news().get("articles", [])
                print(articles)
                for article in articles:
                    title = article["title"]
                    description: str = str(article["description"]).replace('.', '')
                    content: str = str(article["content"]).split(' [+')[0].replace('.', '')
                    lang = detect(f'{description} {content}')
                    if lang == "en":
                        f.writelines(f'{description} {content}.\n')
        if "error" in articles:
            return jsonify({"error": articles["error"]}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)