from fastapi import APIRouter, File, UploadFile
from app.utils.extract_text_from_pdf import extract_text_from_pdf
from app.models.APIResponseModel import APIResponseModel as ResponseModel
from app.utils.save_prompt import save_prompt

router = APIRouter(prefix="/files")

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)) -> ResponseModel:
    try:
        file_content = await file.read()
        file_data = await extract_text_from_pdf(file_content)
        file_data_saved = save_prompt(file_data)
        return ResponseModel(
            status="success",
            status_code=200,
            message="File uploaded successfully",
            data={
                "file_data": file_data
            }
        )
    except Exception as e:
        return ResponseModel(
            status="error",
            status_code= 500,
            message="An error occurred",
            data={
                "error": str(e)
            }
        )