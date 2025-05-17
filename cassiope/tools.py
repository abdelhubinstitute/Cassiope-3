import os
import requests
from typing import Optional

from agents import function_tool

@function_tool
def generate_image(prompt: str, fal_api_key: Optional[str] = None) -> str:
    """Generate an image via Fal.ai and return the URL."""
    api_key = fal_api_key or os.environ.get("FAL_API_KEY")
    if not api_key:
        raise ValueError("FAL_API_KEY not set")
    url = "https://api.fal.ai/v1/images"
    headers = {"Authorization": f"Bearer {api_key}"}
    payload = {"prompt": prompt, "model": "stable-diffusion-v3"}
    response = requests.post(url, json=payload, headers=headers, timeout=30)
    response.raise_for_status()
    return response.json().get("image_url", "")
