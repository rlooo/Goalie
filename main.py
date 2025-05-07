from fastapi import FastAPI
from router.retrospective import router as retrospective_router
from router.milestones import router as milestone_router

app = FastAPI()
app.include_router(retrospective_router)
app.include_router(milestone_router)
