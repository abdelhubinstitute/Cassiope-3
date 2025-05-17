from typing import Dict, List

from agents import Runner

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


def research(title: str) -> str:
    result = Runner.run_sync(agent_recherche, title)
    return result.final_output


def generate_plans(title: str, research_results: str):
    result = Runner.run_sync(plan_agent, f"{title}\n{research_results}")
    return result.final_output


def draft_article(title: str, research_results: str, plan: str, tone: str, length: str):
    prompt = f"TON:{tone}\nLONGUEUR:{length}\n{title}\n{plan}\n{research_results}"
    result = Runner.run_sync(redacteur_initial, prompt)
    return result.final_output


def critique_article(article_v1: str, feedback: str):
    result = Runner.run_sync(agent_critique, f"{article_v1}\n{feedback}")
    return result.final_output


def revise_article(title: str, research_results: str, plan: str, article_v1: str, critique: str, tone: str, length: str):
    prompt = (
        f"TON:{tone}\nLONGUEUR:{length}\n{title}\n{plan}\n{research_results}\n{article_v1}\n{critique}"
    )
    result = Runner.run_sync(redacteur_final, prompt)
    return result.final_output


def create_visual_prompt(article: str) -> str:
    result = Runner.run_sync(prompt_visuel_agent, article)
    return result.final_output


def format_html(article: str, image_url: str) -> str:
    content = f"Article:\n{article}\nImage:\n{image_url}"
    result = Runner.run_sync(html_formatter, content)
    return result.final_output
