from models.generator import GenerationRequest, GenerationResponse

def generate(prompt: str) -> str:
    """
    Generates a question based on the provided topic and parameters using OpenAI's GPT model.
    
    Args:
        request (GenerationRequest): The request containing the topic, length, style, and parameters for generation.
    
    Returns:
        str: The generated question.
    """
    from ..api import client
    question = client.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=prompt.parameters.get("max_tokens", 300)
    )
    
    return (question.choices[0].text.strip())