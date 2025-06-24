import requests

BACKEND_API_URL = "http://localhost:8000/api/grade"  # Update with your backend API URL

def post_essay(essay: str, user_id: str) -> dict:
    """
    Posts an essay to the backend API for grading.

    Args:
        essay (str): The essay text to be graded.
        model (str): The model to use for grading. Default is "phi4".

    Returns:
        dict: The response from the backend API containing the grading results.
    """
    payload = {
        "essay": essay,
        "user_id": user_id
    }
    
    response = requests.post(BACKEND_API_URL, json=payload)
    
    if response.status_code != 200:
        raise Exception(f"Error from backend API: {response.text}")
    
    return response.json()