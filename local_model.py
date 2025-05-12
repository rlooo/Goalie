import requests

def get_local_llama_feedback(prompt: str, model: str = "llama3.1:8b-instruct-q4_K_M"):
    url = "http://localhost:11434/api/chat"

    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": "당신은 사용자의 목표 달성을 도와주는 AI 회고 코치입니다."},
            {"role": "user", "content": prompt}
        ],
        "stream": False
    }

    response = requests.post(url, json=payload)

    print(response.text)

    return response.json()["response"]
