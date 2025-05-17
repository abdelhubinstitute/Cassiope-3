import json
from pathlib import Path
from typing import Any, Dict

CONFIG_FILE = Path.home() / '.cassiope_config.json'
DEFAULT_CONFIG: Dict[str, Any] = {
    "tone": "professionnel",
    "length": "moyen",
    "OPENAI_API_KEY": "",
    "FAL_API_KEY": "",
}

def load_config() -> Dict[str, Any]:
    if CONFIG_FILE.exists():
        with CONFIG_FILE.open() as f:
            data = json.load(f)
    else:
        data = DEFAULT_CONFIG.copy()
        CONFIG_FILE.write_text(json.dumps(data, indent=2))
    return data

def save_config(cfg: Dict[str, Any]) -> None:
    CONFIG_FILE.write_text(json.dumps(cfg, indent=2))
