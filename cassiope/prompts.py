import json
from pathlib import Path
from typing import Dict

PROMPTS_FILE = Path(__file__).resolve().parent / "prompts.json"

DEFAULT_PROMPTS: Dict[str, str] = {
    "GénérateurTitres": (
        "Générer 10 titres créatifs et professionnels pour le thème donné."
    ),
    "AgentRecherche": (
        "Effectuer une recherche web approfondie sur le titre sélectionné."
    ),
    "GénérateurPlan": (
        "Créer 3 plans détaillés pour l’article basé sur le titre et les recherches."
    ),
    "RédacteurInitial": (
        "Rédiger une première version de l’article basée sur le titre, les recherches et le plan."
    ),
    "AgentCritique": (
        "Analyser l’article et les retours utilisateur pour proposer 3 suggestions d’amélioration."
    ),
    "RédacteurFinal": (
        "Réviser l’article en intégrant la critique, le titre, les recherches et le plan."
    ),
    "CréateurPromptVisuel": (
        "Générer un prompt visuel détaillé basé sur le contenu de l’article."
    ),
    "FormateurHTML": (
        "Formatter l’article et les images dans un document HTML publiable avec la police Roboto."
    ),
}


def load_prompts() -> Dict[str, str]:
    if PROMPTS_FILE.exists():
        with PROMPTS_FILE.open() as f:
            return json.load(f)
    return DEFAULT_PROMPTS.copy()


def save_prompts(prompts: Dict[str, str]) -> None:
    PROMPTS_FILE.write_text(json.dumps(prompts, indent=2, ensure_ascii=False))
