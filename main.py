from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware

from services.book_analysis import analyze_book

app = FastAPI()

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/get_book_analysis")
def get_book_analysis(book_id: str = Query(...)):
    if len(book_id) > 5 or not book_id.isdigit():
        raise HTTPException(status_code=400, detail="book_id must be 5 or fewer digits")

    result = analyze_book(book_id)
    return {"result": result}
