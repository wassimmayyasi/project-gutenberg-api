from pathlib import Path
from groq import Groq
from config import GROQ_API_KEY, MODEL_USED

client = Groq(api_key=GROQ_API_KEY)


def get_completion(prompt: str) -> str:
    response = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model=MODEL_USED,
    )
    return response.choices[0].message.content.strip("`\n")


def load_prompt(template_path: str, **kwargs) -> str:
    template = Path(template_path).read_text()
    return template.format(**kwargs)
