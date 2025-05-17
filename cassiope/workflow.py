from typing import Dict, List

from agents import Runner
from .config import load_config, save_config

from .agents import (
    generator_titres,
    agent_recherche,
    plan_agent,
    redacteur_initial,
    agent_critique,
    redacteur_final,
    prompt_visuel_agent,
    html_formatter,
)


def refine_title(theme: str) -> List[str]:
    result = Runner.run_sync(generator_titres, theme)
    return result.final_output


def set_title(title: str) -> None:
    cfg = load_config()
    cfg["title"] = title
    save_config(cfg)


def research(title: str) -> str:
    result = Runner.run_sync(agent_recherche, title)
    return result.final_output


def generate_plans(title: str, research_results: str):
    result = Runner.run_sync(plan_agent, f"{title}\n{research_results}")
    return result.final_output


def draft_article(title: str, research_results: str, plan: str):
    cfg = load_config()
    meta = f"Tone: {cfg.get('tone')}\nLongueur: {cfg.get('length')}"
    result = Runner.run_sync(
        redacteur_initial,
        f"{title}\n{plan}\n{research_results}\n{meta}",
    )
    return result.final_output


def critique_article(article_v1: str, feedback: str):
    result = Runner.run_sync(agent_critique, f"{article_v1}\n{feedback}")
    return result.final_output


def revise_article(title: str, research_results: str, plan: str, article_v1: str, critique: str):
    cfg = load_config()
    meta = f"Tone: {cfg.get('tone')}\nLongueur: {cfg.get('length')}"
    result = Runner.run_sync(
        redacteur_final,
        f"{title}\n{plan}\n{research_results}\n{article_v1}\n{critique}\n{meta}",
    )
    return result.final_output


def create_visual_prompt(article: str) -> str:
    result = Runner.run_sync(prompt_visuel_agent, article)
    return result.final_output


def format_html(article: str, image_url: str) -> str:
    cfg = load_config()
    styles = (
        "<style>body{font-family:'Roboto',sans-serif;margin:2rem;}h1{font-weigh"
        "t:500;}img{max-width:100%;height:auto;}</style>"
    )
    meta = f"<p><em>Tone: {cfg.get('tone')} - Longueur: {cfg.get('length')}</em></p>"
    content = f"{styles}<h1>{cfg.get('title','')}</h1>{meta}{article}<img src='{image_url}'>"
    result = Runner.run_sync(html_formatter, content)
    return result.final_output
