from typing import List
from agents import Agent
from pydantic import BaseModel

from . import config
from .tools import generate_image

class Plan(BaseModel):
    sections: List[str]

# Load prompts from config
PROMPTS = config.load_prompts()

# Define agents following the description

generator_titres = Agent(
    name="GénérateurTitres",
    instructions=PROMPTS.get("GénérateurTitres"),
    model="gpt-4o",
)

agent_recherche = Agent(
    name="AgentRecherche",
    instructions=PROMPTS.get("AgentRecherche"),
    tools=[],  # placeholder for web search tool
    model="gpt-4o",
)

plan_agent = Agent(
    name="GénérateurPlan",
    instructions=PROMPTS.get("GénérateurPlan"),
    model="gpt-4o",
    output_type=List[Plan],
)

redacteur_initial = Agent(
    name="RédacteurInitial",
    instructions=PROMPTS.get("RédacteurInitial"),
    model="gpt-4o",
)

agent_critique = Agent(
    name="AgentCritique",
    instructions=PROMPTS.get("AgentCritique"),
    model="gpt-4o",
)

redacteur_final = Agent(
    name="RédacteurFinal",
    instructions=PROMPTS.get("RédacteurFinal"),
    model="gpt-4o",
)

prompt_visuel_agent = Agent(
    name="CréateurPromptVisuel",
    instructions=PROMPTS.get("CréateurPromptVisuel"),
    model="gpt-4o",
)

html_formatter = Agent(
    name="FormateurHTML",
    instructions=PROMPTS.get("FormateurHTML"),
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
