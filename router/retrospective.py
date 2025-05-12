from fastapi import APIRouter, Request

from claude import get_claude_retrospective_feedback
from llama import get_llama_retrospective_feedback
from models.milestones import get_user_milestones
from models.retrospective import save_retrospective

router = APIRouter()

@router.post("/daily-retrospective")
async def daily_retrospective(request: Request):
    try:
        data = await request.json()
        user_id = data.get("user_id")
        retrospective = data.get("retrospective")

        if not user_id or not retrospective:
            return {"error": "user_id와 회고 내용을 입력해주세요."}

        milestones = await get_user_milestones(user_id)
        milestone_titles = [m["title"] for m in milestones]

        feedback = await get_claude_retrospective_feedback(retrospective, milestone_titles)

        await save_retrospective(user_id, ", ".join(milestone_titles), retrospective, feedback)

        return {"feedback": feedback}
    except Exception as e:
        return {"error": str(e)}

@router.post("/llama/daily-retrospective")
async def daily_retrospective(request: Request):
    try:
        data = await request.json()
        user_id = data.get("user_id")
        retrospective = data.get("retrospective")

        if not user_id or not retrospective:
            return {"error": "user_id와 회고 내용을 입력해주세요."}

        milestones = await get_user_milestones(user_id)
        milestone_titles = [m["title"] for m in milestones]

        feedback = await get_llama_retrospective_feedback(retrospective, milestone_titles)

        await save_retrospective(user_id, ", ".join(milestone_titles), retrospective, feedback)

        return {"feedback": feedback}
    except Exception as e:
        return {"error": str(e)}