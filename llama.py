from local_model import get_local_llama_feedback

def get_llama_retrospective_feedback(retrospective: str, milestone_list: list[str]):
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

    return get_local_llama_feedback(prompt)
