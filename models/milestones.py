from bson import ObjectId

from config.database import db
from datetime import datetime

milestones = db["milestones"]

async def create_milestone(user_id: str, title: str):
    return await milestones.insert_one({
        "user_id": user_id,
        "title": title,
        "created_at": datetime.utcnow()
    })

async def get_user_milestones(user_id: str):
    cursor = milestones.find({"user_id": user_id}).sort("created_at", -1)
    return await cursor.to_list(length=100)

async def update_milestone(milestone_id: str, title: str):
    return await milestones.update_one(
        {"_id": ObjectId(milestone_id)},
        {"$set": {"title": title}}
    )

async def delete_milestone(milestone_id: str):
    return await milestones.delete_one({"_id": ObjectId(milestone_id)})
