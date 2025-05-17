import json
from pathlib import Path
from typing import Dict, Any

from .prompts import DEFAULT_PROMPTS

CONFIG_FILE = Path.home() / '.cassiope_config.json'

def load_config() -> Dict[str, Any]:
    if CONFIG_FILE.exists():
        with CONFIG_FILE.open() as f:
            return json.load(f)
    return {}

def save_config(cfg: Dict[str, Any]) -> None:
    CONFIG_FILE.write_text(json.dumps(cfg, indent=2))


def load_prompts() -> Dict[str, str]:
    cfg = load_config()
    prompts = cfg.get("prompts") or {}
    if not prompts:
        prompts = DEFAULT_PROMPTS.copy()
        cfg["prompts"] = prompts
        save_config(cfg)
    return prompts


def save_prompts(prompts: Dict[str, str]) -> None:
    cfg = load_config()
    cfg["prompts"] = prompts
    save_config(cfg)
