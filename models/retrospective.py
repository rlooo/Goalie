from config.database import db
from datetime import datetime

retrospectives = db["retrospectives"]

async def save_retrospective(user_id: str, milestone: str, retrospective: str, feedback: str):
    doc = {
        "user_id": user_id,
        "milestone": milestone,
        "retrospective": retrospective,
        "feedback": feedback,
        "created_at": datetime.utcnow()
    }
    await retrospectives.insert_one(doc)

async def get_user_retros(user_id: str, limit=10):
    cursor = retrospectives.find({"user_id": user_id}).sort("created_at", -1).limit(limit)
    return await cursor.to_list(length=limit)