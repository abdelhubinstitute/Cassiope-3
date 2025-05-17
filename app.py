import os
import streamlit as st
from cassiope import config, workflow
from cassiope import prompts as prompt_cfg

st.set_page_config(page_title="Cassiope", page_icon="✨")

# Roboto font styling
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&display=swap');
    html, body, [class*="css"]  { font-family: 'Roboto', sans-serif; }
    </style>
    """,
    unsafe_allow_html=True,
)

cfg = config.load_config()

st.title("Cassiope – Rédaction d’Articles Intelligente")
import os

openai_key = st.sidebar.text_input("Clé API OpenAI", value=cfg.get("OPENAI_API_KEY"), type="password")
fal_key = st.sidebar.text_input("Clé API Fal.ai", value=cfg.get("FAL_API_KEY"), type="password")
tone = st.sidebar.text_input("Ton de l'article", value=cfg.get("tone", "professionnel"))
length = st.sidebar.text_input("Longueur", value=cfg.get("length", "standard"))

if st.sidebar.button("Enregistrer les clés"):
    cfg["OPENAI_API_KEY"] = openai_key
    cfg["FAL_API_KEY"] = fal_key
    cfg["tone"] = tone
    cfg["length"] = length
    os.environ["OPENAI_API_KEY"] = openai_key
    os.environ["FAL_API_KEY"] = fal_key
    config.save_config(cfg)
    st.sidebar.success("Clés sauvegardées")

with st.sidebar.expander("Prompts"):
    prompts = prompt_cfg.load_prompts()
    agent_name = st.selectbox("Agent", list(prompts.keys()))
    prompt_text = st.text_area("Instructions", prompts[agent_name], height=200)
    if st.button("Enregistrer le prompt"):
        prompts[agent_name] = prompt_text
        prompt_cfg.save_prompts(prompts)
        st.success("Instructions mises à jour")
        st.experimental_rerun()

st.header("Phase 1 : Raffinement du Thème et du Titre")
theme = st.text_input("Thème initial")
if st.button("Générer des titres") and theme:
    titres = workflow.refine_title(theme)
    chosen_title = st.radio("Choisissez un titre", titres)
    st.session_state["title"] = chosen_title

st.header("Phase 2 : Recherche et Planification")
if st.session_state.get("title"):
    if st.button("Lancer la recherche"):
        research_results = workflow.research(st.session_state["title"])
        st.session_state["research"] = research_results
    if st.session_state.get("research"):
        plans = workflow.generate_plans(st.session_state["title"], st.session_state["research"])
        chosen_plan = st.selectbox("Choisissez un plan", plans)
        st.session_state["plan"] = chosen_plan

st.header("Phase 3 : Rédaction Initiale")
if st.session_state.get("plan"):
    if st.button("Rédiger l’article"):
        article_v1 = workflow.draft_article(
            st.session_state["title"],
            st.session_state["research"],
            st.session_state["plan"],
            tone,
            length,
        )
        st.session_state["article_v1"] = article_v1
    if st.session_state.get("article_v1"):
        feedback = st.text_area("Vos retours")
        if st.button("Générer des critiques"):
            critiques = workflow.critique_article(st.session_state["article_v1"], feedback)
            chosen_crit = st.selectbox("Choisissez une critique", critiques)
            st.session_state["critique"] = chosen_crit

st.header("Phase 4 : Révision")
if st.session_state.get("critique"):
    if st.button("Créer la version finale"):
        final_article = workflow.revise_article(
            st.session_state["title"],
            st.session_state["research"],
            st.session_state["plan"],
            st.session_state["article_v1"],
            st.session_state["critique"],
            tone,
            length,
        )
        st.session_state["final_article"] = final_article

st.header("Phase 5 : Visuels")
if st.session_state.get("final_article"):
    if st.button("Générer le prompt visuel"):
        vp = workflow.create_visual_prompt(st.session_state["final_article"])
        st.session_state["vis_prompt"] = vp
    if st.session_state.get("vis_prompt"):
        st.write(st.session_state["vis_prompt"])
        if st.button("Générer l’image"):
            from cassiope.tools import generate_image

            image_url = generate_image(
                st.session_state["vis_prompt"], fal_key, openai_key
            )
            st.session_state["image_url"] = image_url
    if st.session_state.get("image_url"):
        st.image(st.session_state["image_url"])
        if st.button("Générer l’HTML"):
            html = workflow.format_html(st.session_state["final_article"], st.session_state["image_url"])
            st.session_state["html"] = html

if st.session_state.get("html"):
    st.header("Article Final")
    st.write(st.session_state["html"], unsafe_allow_html=True)
