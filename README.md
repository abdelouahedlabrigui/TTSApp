# 🗞️ News Fetcher and Speaker

This project fetches the latest news articles based on user-provided queries using the [NewsAPI](https://newsapi.org/) and saves them into a file. It also includes a frontend feature that reads the news aloud using the browser's built-in speech synthesis.

---

## 🧠 Features

### Backend (Python + Flask)
- Accepts GET requests to fetch news from NewsAPI based on query terms and date.
- Saves English news article content and descriptions to a timestamped `.txt` file.
- Supports multiple comma-separated query terms in one request.

### Frontend (HTML + JavaScript)
- Reads news content aloud sentence-by-sentence.
- Supports adjustable language, speed (rate), and volume for speech synthesis.
- Allows pausing and resuming the speech.

---

## 🏗️ Project Structure

```
project/
├── index.html              # Web UI with speech synthesis features
├── app.py                 #  Flask backend with `/api/write_news_to_file` endpoint
├── Repo/
│   └── News.py             # Contains the `News` class to fetch news articles
└── README.md               # Project documentation (this file)
```

---

## 🧪 Example API Request

```http
GET /api/write_news_to_file?queries=technology,science&now=2025-06-05
```

### Response

```json
{
  "message": "News written successfully"
}
```

---

## ⚙️ Requirements

- Python 3.8+
- Flask
- requests
- langdetect

### Install dependencies

```bash
pip install flask requests langdetect
```

---

## 🚀 Running the Application

### 1. Start the Flask server

```bash
python app.py
```

### 2. Open the Web UI

Open `index.html` in your browser or connect it via Flask templates if integrated.

---

## 🗣️ Using the Text-to-Speech

- Paste or type the news content into the input box.
- Choose your preferred language, rate, and volume.
- Click **Speak** to start listening.
- Use **Pause** and **Resume** as needed.

---

## 📌 Notes

- You'll need to obtain an API key from [NewsAPI](https://newsapi.org/) and insert it into the `url` in `News.request_news()`:
  ```python
  url = f"...&apiKey=YOUR_API_KEY"
  ```

- Only English-language content is saved to the file (language detection is performed using `langdetect`).

---

## 📄 License

MIT License
