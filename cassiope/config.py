import json
from pathlib import Path
from typing import Dict, Any

DEFAULT_CONFIG: Dict[str, Any] = {
    "tone": "professionnel",
    "length": "standard",
}

CONFIG_FILE = Path.home() / '.cassiope_config.json'

def load_config() -> Dict[str, Any]:
    if CONFIG_FILE.exists():
        with CONFIG_FILE.open() as f:
            cfg = json.load(f)
    else:
        cfg = DEFAULT_CONFIG.copy()
    for k, v in DEFAULT_CONFIG.items():
        cfg.setdefault(k, v)
    return cfg

def save_config(cfg: Dict[str, Any]) -> None:
    CONFIG_FILE.write_text(json.dumps(cfg, indent=2, ensure_ascii=False))
