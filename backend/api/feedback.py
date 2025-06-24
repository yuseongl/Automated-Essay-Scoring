import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def get_feedback_endpoint(essay: str) -> str:
    """
    Provides feedback on the given essay using OpenAI's GPT model.
    
    Args:
        essay (str): The essay text to be evaluated.
    
    Returns:
        str: The feedback on the essay.
    """
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that provides feedback on essays."},
            {"role": "user", "content": f"Please provide feedback on the following essay:\n\n{essay}"}
        ],
        max_tokens=500
    )
    
    return response.choices[0].message.content.strip()