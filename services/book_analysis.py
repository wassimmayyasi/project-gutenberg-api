import json
from fastapi import HTTPException
from services.gutenberg_service import get_book_text
from services.text_formatting import clean_text, truncate_text
from services.prompt_service import load_prompt, get_completion
from utils.graph_response_util import prepare_graph


def analyze_book(book_id: str):
    book_text = get_book_text(book_id)

    cleaned_text = clean_text(book_text)
    prompt = load_prompt("prompt.txt", text=cleaned_text)
    truncated_prompt = truncate_text(prompt)
    model_output = get_completion(truncated_prompt)

    try:
        parsed_obj = json.loads(model_output)
    except json.JSONDecodeError:
        raise HTTPException(status_code=500, detail="Failed to parse LLM response")

    return prepare_graph(parsed_obj)
