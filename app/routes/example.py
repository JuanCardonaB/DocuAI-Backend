from fastapi import APIRouter

router = APIRouter(prefix="/files")

@router.get("/")
def get_file():
    return {"message" : "Hola mundo"}


