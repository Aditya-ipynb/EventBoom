from fastapi import APIRouter
import json

router = APIRouter()

@router.post("/submit-form")
async def submit_form(data: dict):

    with open("responses.json", "a") as f:
        f.write(json.dumps(data) + "\n")

    return {"message": "Response saved"}

@router.get("/responses")
def get_responses():

    responses = []

    with open("responses.json", "r") as f:
        for line in f:
            responses.append(json.loads(line))

    return responses
