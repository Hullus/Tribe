from fastapi import APIRouter

router = APIRouter(
    prefix="/user",
    tags=["user"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def read_user():
    return [{"username": "Rick"}, {"username": "Morty"}]


@router.post("/")
async def read_user():
    return [{"username": "Rick"}, {"username": "Morty"}]


@router.put("/")
async def read_user():
    return [{"username": "Rick"}, {"username": "Morty"}]


@router.delete("/")
async def read_user():
    return [{"username": "Rick"}, {"username": "Morty"}]


@router.get("/me")
async def read_user():
    return [{"username": "Rick"}, {"username": "Morty"}]


@router.get("/{id}")
async def read_user_by_id():
    return [{"username": "Rick"}, {"username": "Morty"}]
