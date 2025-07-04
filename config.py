from dotenv import load_dotenv
import os

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
MODEL_USED = os.getenv("MODEL_USED")
TOKENIZER_MODEL = os.getenv("TOKENIZER_MODEL")
MAX_TOKENS = int(os.getenv("MAX_TOKENS", 6000))
