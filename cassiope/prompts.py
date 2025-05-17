import json
from pathlib import Path
from typing import Dict

PROMPTS_FILE = Path.home() / '.cassiope_prompts.json'

DEFAULT_PROMPTS: Dict[str, str] = {
    'generator_titres': "Générer 10 titres créatifs et professionnels pour le thème donné.",
    'agent_recherche': (
        "Effectuer une recherche web approfondie sur le titre sélectionné et résumer les résultats en français.") ,
    'plan_agent': "Créer 3 plans détaillés pour l’article basé sur le titre et les recherches.",
    'redacteur_initial': (
        "Rédiger une première version de l’article basée sur le titre, les recherches et le plan."),
    'agent_critique': (
        "Analyser l’article et les retours utilisateur pour proposer 3 suggestions d’amélioration."),
    'redacteur_final': (
        "Réviser l’article en intégrant la critique, le titre, les recherches et le plan."),
    'prompt_visuel_agent': (
        "Générer un prompt visuel détaillé basé sur le contenu de l’article."),
    'html_formatter': (
        "Formatter l’article et les images dans un document HTML publiable avec une mise en page moderne."),
}


def load_prompts() -> Dict[str, str]:
    if PROMPTS_FILE.exists():
        try:
            return json.loads(PROMPTS_FILE.read_text())
        except Exception:
            pass
    PROMPTS_FILE.write_text(json.dumps(DEFAULT_PROMPTS, ensure_ascii=False, indent=2))
    return DEFAULT_PROMPTS.copy()


def save_prompts(prompts: Dict[str, str]) -> None:
    PROMPTS_FILE.write_text(json.dumps(prompts, ensure_ascii=False, indent=2))
