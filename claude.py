import anthropic
import os

from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("ANTHROPIC_API_KEY")
client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

async def get_claude_retrospective_feedback(retrospective: str, milestone_list: list[str]):

    milestone_text = "\n".join([f"- {m}" for m in milestone_list]) if milestone_list else "(없음)"

    prompt = f"""
    당신은 사용자의 목표 달성을 도와주는 AI 회고 코치입니다.
    
    사용자는 아래와 같은 마일스톤을 가지고 있습니다.
    - "{milestone_text}"
    
    그리고 오늘 하루에 대해 다음과 같이 회고했습니다:
    - "{retrospective}"
    
    아래 네 가지를 작성해주세요:
    1. 마일스톤 목록 기준으로 오늘 회고가 마일스톤과 얼마나 부합하는지 평가해주세요.
    2. 마일스톤 달성을 위한 오늘의 행동 중 잘한 점과 부족한 점을 알려주세요.
    3. 내일 이 마일스톤들을 더 잘 달성하기 위한 구체적인 팁을 주세요. 
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


async def get_milestone_feedback(milestone: str):

    prompt = f"""
    당신은 사용자의 목표 달성을 돕는 AI 코치입니다. 사용자가 작성한 마일스톤에 대해 다음을 제공해야 합니다:

    1. 마일스톤의 명확성 평가 (구체적인가, 모호한가)
    2. 달성 가능성 평가 (현실적인지, 너무 과도한지)
    3. 만약 필요하다면: 개선된 버전의 마일스톤 제안 
    4. 동기 부여 피드백 메시지

    예시는 다음과 같습니다:

    입력된 마일스톤: "운동 열심히 하기"

    출력 예시:
    - 명확성: 다소 모호함. '열심히'라는 표현은 구체적인 기준이 부족합니다.
    - 달성 가능성: 측정 기준이 없어 진척도를 평가하기 어려움.
    - 개선안: "이번 주에 3회, 30분 이상 유산소 운동을 하기"
    - 피드백: 지금처럼 건강을 신경 쓰는 건 정말 멋진 일이에요! 작게 시작해도 꾸준하면 큰 변화가 생길 거예요.

    ---

    이제 사용자 입력을 평가해주세요.
    마일스톤: "{milestone}"
    """

    response = client.messages.create(
        model="claude-3-5-haiku-20241022",
        max_tokens=1024,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.content[0].text