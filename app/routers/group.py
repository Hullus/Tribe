from fastapi import APIRouter

router = APIRouter(
    prefix="/group",
    tags=["group"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def read_group():
    return [{"username": "Rick"}, {"username": "Morty"}]


@router.post("/")
async def read_group():
    return [{"username": "Rick"}, {"username": "Morty"}]


@router.put("/")
async def read_group():
    return [{"username": "Rick"}, {"username": "Morty"}]


@router.delete("/")
async def read_group():
    return [{"username": "Rick"}, {"username": "Morty"}]


@router.get("/me")
async def read_group_me():
    return {"username": "fakecurrentuser"}


@router.get("/{id}")
async def read_group_by_id(id: str):
    return {"username": id}
