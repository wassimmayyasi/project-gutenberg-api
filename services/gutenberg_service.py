import requests
from fastapi import HTTPException


def get_book_text(book_id: str) -> str:
    url = f"https://www.gutenberg.org/files/{book_id}/{book_id}-0.txt"
    try:
        response = requests.get(url)
        if not response.ok:
            raise HTTPException(
                status_code=404, detail="Book not found at Project Gutenberg"
            )
        return response.text
    except requests.RequestException:
        raise HTTPException(
            status_code=502, detail="Failed to fetch book from Project Gutenberg"
        )
