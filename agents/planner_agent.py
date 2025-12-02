import requests
from config import Config

def generate_study_plan(subject, hours):
    url = "https://api.deepseek.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {Config.DEEPSEEK_API_KEY}",
        "Content-Type": "application/json"
    }

    prompt = f"""
    Create a detailed study plan for a student.
    Subject: {subject}
    Total hours: {hours}
    Break into sessions. Give timing suggestions.
    """

    data = {
        "model": "deepseek-chat",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7
    }

    response = requests.post(url, headers=headers, json=data)

    result = response.json()

    # Safety check
    if "choices" not in result:
        return ["AI Error: " + result.get("error", {}).get("message", "Unknown error")]

    plan_text = result["choices"][0]["message"]["content"]

    # Convert AI output into list lines
    plan = [line.strip() for line in plan_text.split("\n") if line.strip()]

    return plan
