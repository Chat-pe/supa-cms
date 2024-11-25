from fastapi import APIRouter, Depends, Query
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from .services import create_demo_book, get_demo_book_by_email, update_demo_book, delete_demo_book, get_all_demo_books
from .dtos import DemoBookDto, UpdateDemoBookDto, DemoBookListResponse
from typing import Annotated
router = APIRouter()

#add options for page number based pagination
@router.get("/", response_model=DemoBookListResponse)
async def get_demo_books(page: int = Query(default=1, ge=1), page_size: int = Query(default=10, ge=1)) -> DemoBookListResponse:
    demo_books = await get_all_demo_books(page, page_size)
    return JSONResponse(status_code=200, content=jsonable_encoder(demo_books))

@router.get("/{email}", response_model=DemoBookDto)
async def get_demo_book(email: str) -> DemoBookDto:
    demo_book = await get_demo_book_by_email(email)
    return JSONResponse(status_code=200, content=jsonable_encoder(demo_book))

@router.post("/", response_model=DemoBookDto)
async def create_book(demo_book: DemoBookDto) -> DemoBookDto:
    created_book = await create_demo_book(demo_book)
    return JSONResponse(status_code=201, content=jsonable_encoder(created_book))

@router.put("/{email}", response_model=DemoBookDto)
async def update_book(email: str, demo_book: Annotated[UpdateDemoBookDto, Depends(get_demo_book_by_email)]) -> DemoBookDto:
    updated_book = await update_demo_book(email, demo_book)
    return JSONResponse(status_code=200, content=jsonable_encoder(updated_book))

@router.delete("/{email}", response_model=DemoBookDto)
async def delete_book(email: str) -> DemoBookDto:
    deleted_book = await delete_demo_book(email)
    return JSONResponse(status_code=200, content=jsonable_encoder(deleted_book))


