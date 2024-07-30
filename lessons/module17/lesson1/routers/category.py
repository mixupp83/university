from fastapi import APIRouter

router = APIRouter(prefix="/category", tags=["category"])

@router.get("/all_categoies")
async def get_all_categories():
    pass

@router.post("/create")
async def create_category():
    pass

@router.put("/update_category")
async def update_category():
    pass

@router.delete("/delete")
async def delete_category():
    pass
