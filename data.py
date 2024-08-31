
import requests

def generate_questions(amount=10, difficulty='medium', type='boolean') -> dict:
    request_url = f"https://opentdb.com/api.php?amount={amount}&difficulty={difficulty}&type={type}"
    request = requests.get(url=request_url)
    questions_data: dict = request.json()
    return questions_data.get("results")


question_data = generate_questions()
