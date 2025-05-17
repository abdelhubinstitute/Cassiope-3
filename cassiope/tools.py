import os
import requests
from typing import Optional

from agents import function_tool

@function_tool
def generate_image(
    prompt: str,
    fal_api_key: Optional[str] = None,
    openai_api_key: Optional[str] = None,
) -> str:
    """Generate an image via Fal.ai and return the URL."""
    api_key = fal_api_key or os.environ.get("FAL_API_KEY")
    if not api_key:
        raise ValueError("FAL_API_KEY not set")
    url = (
        "https://api.fal.ai/v1/pipelines/fal-ai/gpt-image-1/text-to-image/byok"
    )
    headers = {"Authorization": f"Key {api_key}"}
    payload = {
        "input": {
            "prompt": prompt,
            "image_size": "auto",
            "num_images": 1,
            "quality": "auto",
            "background": "auto",
            "openai_api_key": openai_api_key or os.environ.get("OPENAI_API_KEY", ""),
        },
        "logs": True,
    }
    response = requests.post(url, json=payload, headers=headers, timeout=60)
    response.raise_for_status()
    data = response.json()
    images = data.get("images") or data.get("data", {}).get("images", [])
    if isinstance(images, list) and images:
        return images[0].get("url", "")
    return ""
