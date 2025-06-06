import requests

class News:
    def __init__(self, query: str, now: str):
        self.query = query
        self.now = now
    
    def request_news(self):
        url = f"https://newsapi.org/v2/everything?q={self.query}&from={self.now}&sortBy=publishedAt&apiKey="
        response = requests.get(url, headers={"Content-Type": "application/json", "Accept": "application/json"})
        return response.json()
    