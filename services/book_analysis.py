import requests
import json
from fastapi import HTTPException
from services.text_formatting import clean_text, truncate_text
from services.prompt_service import load_prompt, get_completion
from utils.graph_response_util import prepare_graph


def analyze_book(book_id: str):
    if len(book_id) > 5 or not book_id.isdigit():
        raise HTTPException(status_code=400, detail="book_id must be 5 or fewer digits")

    url = f"https://www.gutenberg.org/files/{book_id}/{book_id}-0.txt"
    response = requests.get(url)

    if not response.ok:
        raise HTTPException(
            status_code=404, detail="Book not found at Project Gutenberg"
        )

    cleaned_text = clean_text(response.text)
    prompt = load_prompt("prompt.txt", text=cleaned_text)
    truncated_prompt = truncate_text(prompt)
    model_output = get_completion(truncated_prompt)

    try:
        parsed_obj = json.loads(model_output)
    except json.JSONDecodeError:
        raise HTTPException(status_code=500, detail="Failed to parse LLM response")

    return prepare_graph(parsed_obj)
