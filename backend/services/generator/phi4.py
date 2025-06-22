def phi4_generator(prompt: str) -> str:
    """
    Generates a response using the Phi-4 model.

    Args:
        prompt (str): The input prompt for the model.

    Returns:
        str: The generated response.
    """
    from app.services.generator.base import generate_response
    return generate_response(prompt, model="phi-4")