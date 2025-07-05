# 📚 FastAPI Book Analysis API

This FastAPI app fetches public domain books from Project Gutenberg, processes the text, and sends a prompt to the Groq LLM API for interaction graph generation. The output is returned as a JSON object containing nodes and edges for visualization.

---

## 🚀 Features

- Fetches book content by `book_id` from [Project Gutenberg](https://www.gutenberg.org/)
- Cleans and truncates text using HuggingFace tokenizer
- Sends structured prompt to Groq's LLM API
- Parses response and validates node-edge relationships
- CORS-enabled API ready for frontend consumption

---

## 🗂️ Project Structure
```
project-gutenberg-api/
│
├── main.py # FastAPI entrypoint
├── config.py # Env variable loading
├── services/
│ ├── book_analysis.py # Book analysis orchestration
│ ├── prompt_service.py # Template loader
│ ├── text_formatting.py # Text cleaner & truncator
│ └── gutenberg_service.py # Gutenberg fetch logic
└── utils/
└── graph_response_util.py # Graph node/edge validator

```


## 🧪 Example API Call
```
GET /get_book_analysis?book_id=1342
```

**Response:**

```
{
  "result": {
    "nodes_with_edges": [...],
    "nodes_without_edges": [...],
    "edges": [...]
  }
}
```

## 📈 Future Improvements
- Async I/O and streaming support
- Retry logic for network failures
- Authentication for private API usage

## 🧑‍💻 Author
#### Wassim Mayyasi
#### Full-stack Engineeer