from fastapi import APIRouter, HTTPException
from app.models.APIResponseModel import APIResponseModel as ResponseModel
from app.utils.ask_ollama import ask_ollama, load_data
from pydantic import BaseModel

router = APIRouter(prefix="/ask")

class AskRequest(BaseModel):
    prompt: str

@router.post("/ask_question")
async def upload_file(request: AskRequest) -> ResponseModel:
    try:
        if not request.prompt:
            raise HTTPException(status_code=400, detail="Prompt is required")
        
        prompt = request.prompt
        
        if prompt == "":
            return ResponseModel(
                status="error",
                status_code=400,
                message="Prompt is required",
                data={}
            )
        data = load_data()
        data = ask_ollama(data, prompt)

        return ResponseModel(
            status="success",
            status_code=200,
            message="File uploaded successfully",
            data={
                "prompt": data
            }
        )
    except Exception as e:
        return HTTPException(
            status_code=500,
            detail=str(e),
        )