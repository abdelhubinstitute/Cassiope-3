from typing import List
from agents import Agent, WebSearchTool
from pydantic import BaseModel

from .prompts import load_prompts

class Plan(BaseModel):
    sections: List[str]

_PROMPTS = load_prompts()

# Define agents using the loaded prompts

generator_titres = Agent(
    name="GénérateurTitres",
    instructions=_PROMPTS["GénérateurTitres"],
    model="gpt-4o",
)

agent_recherche = Agent(
    name="AgentRecherche",
    instructions=_PROMPTS["AgentRecherche"],
    tools=[WebSearchTool()],
    model="gpt-4o",
)

plan_agent = Agent(
    name="GénérateurPlan",
    instructions=_PROMPTS["GénérateurPlan"],
    model="gpt-4o",
    output_type=List[Plan],
)

redacteur_initial = Agent(
    name="RédacteurInitial",
    instructions=_PROMPTS["RédacteurInitial"],
    model="gpt-4o",
)

agent_critique = Agent(
    name="AgentCritique",
    instructions=_PROMPTS["AgentCritique"],
    model="gpt-4o",
)

redacteur_final = Agent(
    name="RédacteurFinal",
    instructions=_PROMPTS["RédacteurFinal"],
    model="gpt-4o",
)

prompt_visuel_agent = Agent(
    name="CréateurPromptVisuel",
    instructions=_PROMPTS["CréateurPromptVisuel"],
    model="gpt-4o",
)

html_formatter = Agent(
    name="FormateurHTML",
    instructions=_PROMPTS["FormateurHTML"],
    model="gpt-4o",
)

# Map names to agents for convenience
AGENTS = {
    "generator_titres": generator_titres,
    "agent_recherche": agent_recherche,
    "plan_agent": plan_agent,
    "redacteur_initial": redacteur_initial,
    "agent_critique": agent_critique,
    "redacteur_final": redacteur_final,
    "prompt_visuel_agent": prompt_visuel_agent,
    "html_formatter": html_formatter,
}
