import json
from typing import Any


def ensure_str(content: Any) -> str:
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        return "\n".join(
            json.dumps(x, ensure_ascii=False, indent=2) if isinstance(x, dict) else str(x)
            for x in content
        )
    return str(content)
