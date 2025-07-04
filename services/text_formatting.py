import re
from transformers import AutoTokenizer
from config import TOKENIZER_MODEL, MAX_TOKENS

tokenizer = AutoTokenizer.from_pretrained(TOKENIZER_MODEL)


def clean_text(text: str) -> str:
    text = text.replace("\n", " ").replace("\r", "")
    return re.sub(r"\s{2,}", " ", text).strip()


def truncate_text(text: str, max_tokens: int = MAX_TOKENS) -> str:
    tokens = tokenizer.encode(text, truncation=True, max_length=max_tokens)
    return tokenizer.decode(tokens, skip_special_tokens=True)
