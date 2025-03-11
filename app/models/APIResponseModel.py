from pydantic import BaseModel

class APIResponseModel(BaseModel):
    status: str
    message: str
    data: dict
    status_code: int