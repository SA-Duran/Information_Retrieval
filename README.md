# Information_Retrieval

## Overview  
Retrieves relevant documents or text given a user query. Supports indexing, search, and API‑based access.

## Structure & Components

- `src/`: core search/indexing logic and utility modules  
- `research/`: notebooks for experimenting with different methods and datasets  
- `app.py`: REST API endpoint, handles incoming queries and returns results  
- `template.py`: formatting, helper functions for output representation  
- `test.py`: examples or automated tests to verify searching/indexing behavior  
- `requirements.txt` / `pyproject.toml`: dependency declarations

## Technologies & Libraries

| Component | Library / Tool | Role / Connection |
|-----------|------------------|--------------------|
| Indexing & Search Algorithms | Likely scikit‑learn, BM25, or custom vector similarity libraries | Implements how documents/text are indexed and how queries are matched (ranking) |
| Text Processing | pandas, nltk / spaCy / sklearn’s preprocessing modules | Tokenization, normalization, cleaning before indexing |
| API / Web Layer | Flask (or FastAPI) | `app.py` defines routes to receive query payloads and return search results |
| Template / Output Formatting | Python’s standard libraries + `template.py` | Converts raw search results into JSON or other structured output |
| Configuration & Dependency Management | `requirements.txt`, `pyproject.toml` | Ensures reproducible environment; manages library versions |
| Testing / Examples | `test.py` plus notebooks in `research/` | Verifies that indexing + search + API work end‑to‑end; allows experiment tracking/troubleshooting |

## Setup

```bash
git clone https://github.com/SA-Duran/Information_Retrieval.git
cd Information_Retrieval
pip install -r requirements.txt
```

## Usage

- Run the API:

  ```bash
  python app.py
  ```

- Send a search request:

  ```bash
  curl -X POST http://localhost:5000/search \
    -H "Content-Type: application/json" \
    -d '{"query": "your search query"}'
  ```

- Use `test.py` to try example queries or validate indexing/search behavior.

## License  
MIT
