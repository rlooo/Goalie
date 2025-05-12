from fastapi import APIRouter, Request

from claude import get_milestone_feedback
from models.milestones import (
    create_milestone,
    get_user_milestones,
    update_milestone,
    delete_milestone,
    serialize_milestone,
)

router = APIRouter()

@router.get("/milestones")
async def list_milestones(user_id: str):
    milestones = await get_user_milestones(user_id)
    return [serialize_milestone(m) for m in milestones]

@router.post("/milestones")
async def add_milestone(request: Request):
    data = await request.json()
    result =  await create_milestone(data["user_id"], data["title"])
    return {"inserted_id": str(result.inserted_id)}

@router.put("/milestones/{milestone_id}")
async def edit_milestone(milestone_id: str, request: Request):
    data = await request.json()
    result = await update_milestone(milestone_id, data["title"])
    return {"upserted_id": str(result.upserted_id)}

@router.delete("/milestones/{milestone_id}")
async def remove_milestone(milestone_id: str):
    result = await delete_milestone(milestone_id)
    return {"deleted_count": str(result.deleted_count)}

@router.get("/milestones/feedback")
async def add_milestone(request: Request):
    data = await request.json()
    milestone = data.get("title")
    feedback = await get_milestone_feedback(milestone)
    return {"feedback": feedback}