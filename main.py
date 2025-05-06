from fastapi import FastAPI, Request

from claude import call_claude_mcp

app = FastAPI()

@app.post("/daily-retrospective")
async def daily_retrospective(request: Request):
    data = await request.json()
    milestone = data.get("milestone")
    retrospective = data.get("retrospective")

    if not milestone or not retrospective:
        return {"error": "마일스톤과 회고 내용을 모두 입력해주세요."}

    feedback = await call_claude_mcp(milestone, retrospective)
    return {"feedback": feedback}