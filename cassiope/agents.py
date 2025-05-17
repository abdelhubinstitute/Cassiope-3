from typing import List
from agents import Agent, WebSearchTool
from pydantic import BaseModel

from .prompts import load_prompts

class Plan(BaseModel):
    sections: List[str]


_prompts = load_prompts()

# Define agents following the description

generator_titres = Agent(
    name="GénérateurTitres",
    instructions=_prompts["generator_titres"],
    model="gpt-4o",
)

agent_recherche = Agent(
    name="AgentRecherche",
    instructions=_prompts["agent_recherche"],
    tools=[WebSearchTool()],
    model="gpt-4o",
)

plan_agent = Agent(
    name="GénérateurPlan",
    instructions=_prompts["plan_agent"],
    model="gpt-4o",
    output_type=List[Plan],
)

redacteur_initial = Agent(
    name="RédacteurInitial",
    instructions=_prompts["redacteur_initial"],
    model="gpt-4o",
)

agent_critique = Agent(
    name="AgentCritique",
    instructions=_prompts["agent_critique"],
    model="gpt-4o",
)

redacteur_final = Agent(
    name="RédacteurFinal",
    instructions=_prompts["redacteur_final"],
    model="gpt-4o",
)

prompt_visuel_agent = Agent(
    name="CréateurPromptVisuel",
    instructions=_prompts["prompt_visuel_agent"],
    model="gpt-4o",
)

html_formatter = Agent(
    name="FormateurHTML",
    instructions=_prompts["html_formatter"],
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
