
from fastapi import APIRouter, Query, Body
from typing import Annotated
from fastapi.responses import JSONResponse
from .services import get_blog_by_unique_link, create_new_blog, update_blog, delete_blog, get_blogs_by_tags, get_all_blogs, get_all_unique_tags
from .dtos import BlogDto, UpdateBlogDto, BlogResponse, BlogListResponse
from fastapi.encoders import jsonable_encoder
router = APIRouter()


@router.get(
            "/{unique_link}",
            response_model=BlogResponse,
        )
async def get_blogs(unique_link: str) -> BlogResponse:
    blog = await get_blog_by_unique_link(unique_link)
    return JSONResponse(status_code=200, content=jsonable_encoder(blog))


@router.post("/", response_model=BlogListResponse)
async def create_blog(blog: BlogDto) -> BlogListResponse:
    blog = await create_new_blog(blog)
    return JSONResponse(status_code=201, content=jsonable_encoder(blog))

@router.put("/{unique_link}", response_model=BlogResponse)
async def update_current_blog(unique_link: str, blog: UpdateBlogDto = Body(...)) -> BlogResponse:
    blog = await update_blog(unique_link, blog)
    return JSONResponse(status_code=200, content=jsonable_encoder(blog))

@router.delete("/{unique_link}", response_model=BlogResponse)
async def delete_current_blog(unique_link: str) -> BlogResponse:
    blog = await delete_blog(unique_link)
    return JSONResponse(status_code=200, content=jsonable_encoder(blog))


@router.post("/tags", response_model=BlogListResponse)
async def get_all_blogs_by_tags(tags: list[str], page: int = Query(default=1, ge=1), page_size: int = Query(default=10, ge=1)) -> BlogListResponse:
    print(tags, page, page_size)
    blogs = await get_blogs_by_tags(tags, page, page_size)
    return JSONResponse(status_code=200, content=jsonable_encoder(blogs))


@router.get("/", response_model=BlogListResponse)
async def get_blogs(page: int = Query(default=1, ge=1), page_size: int = Query(default=10, ge=1)) -> BlogListResponse:
    blogs = await get_all_blogs(page, page_size)
    return JSONResponse(status_code=200, content=jsonable_encoder(blogs))



@router.get("/tags/all", response_model=list[str])
async def get_all_tags() -> list[str]:
    tags = await get_all_unique_tags()
    return JSONResponse(status_code=200, content=jsonable_encoder(tags))

