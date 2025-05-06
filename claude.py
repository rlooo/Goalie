import anthropic
import httpx
import os

from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("ANTHROPIC_API_KEY")

async def call_claude_mcp(milestone: str, retrospective: str):
    client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

    prompt = f"""
    당신은 사용자의 목표 달성을 도와주는 AI 회고 코치입니다.
    
    사용자는 아래와 같은 마일스톤을 가지고 있습니다.
    - "{milestone}"
    
    그리고 오늘 하루에 대해 다음과 같이 회고했습니다:
    - "{retrospective}"
    
    아래 네 가지를 작성해주세요:
    1. 오늘 회고가 마일스톤과 얼마나 부합하는지 평가해주세요.
    2. 마일스톤 달성을 위한 오늘의 행동 중 잘한 점과 부족한 점을 알려주세요.
    3. 내일 이 마일스톤을 더 잘 달성하기 위한 구체적인 팁을 주세요.
    4. 짧고 따뜻한 응원 메시지를 전달해주세요.
    """



    response = client.messages.create(
        model="claude-3-5-haiku-20241022",
        max_tokens=1024,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.content[0].text
