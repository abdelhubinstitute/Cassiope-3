# Cassiope

Prototype d'application de rédaction d'articles multi-agents en français. Cette application utilise l'SDK OpenAI Agents et Streamlit pour orchestrer plusieurs agents GPT‑4o. Les prompts sont éditables et les paramètres de ton et de longueur sont sauvegardés.

## Installation

```bash
pip install -r requirements.txt
```

## Utilisation

Exécutez l'interface Streamlit :

```bash
streamlit run app.py
```

Ajoutez vos clés API OpenAI et Fal.ai dans le panneau latéral puis suivez les étapes.
Une image est générée via l'API Fal.ai et intégrée à l'article final.
