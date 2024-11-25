from src.database import blog_client
from fastapi.encoders import jsonable_encoder
from src.blogs.schema import Blog
from src.blogs.dtos import BlogDto, UpdateBlogDto
from fastapi import HTTPException
from datetime import datetime
from src.common import hyphenate_sentence, remove_null_values

async def get_blog_by_unique_link(unique_link: str) -> Blog:
    blog = await blog_client.find_one({"unique_link": unique_link})
    if not blog:
        raise HTTPException(status_code=404, detail="Blog not found")   
    blog["_id"] = str(blog["_id"])
    return Blog(**blog)


async def create_new_blog(blog: BlogDto) -> Blog:
    blog_dict = jsonable_encoder(blog)
    blog_dict["unique_link"] = hyphenate_sentence(blog_dict["title"])
    blog_dict["status"] = "draft"
    blog_dict["created_at"] = datetime.now()
    blog_dict["updated_at"] = datetime.now()
    blog = await blog_client.insert_one(blog_dict)
    return Blog(**blog_dict) 


async def update_blog(unique_link: str, blog: UpdateBlogDto) -> Blog:
    blog_dict = jsonable_encoder(blog)
    blog_dict = remove_null_values(blog_dict)
    print(blog_dict)
    blog_dict["updated_at"] = datetime.now()
    await blog_client.update_one({"unique_link": unique_link}, {"$set": blog_dict})
    return await get_blog_by_unique_link(unique_link)


async def delete_blog(unique_link: str) -> Blog:
    await blog_client.delete_one({"unique_link": unique_link})
    return {"message": "Blog deleted successfully"}



async def get_blogs_by_tags(tags: list[str], page: int = 1, page_size: int = 10) -> list[Blog]:
    if tags:
        cursor = blog_client.find({"tags": {"$in": tags}}) \
                           .skip((page - 1) * page_size) \
                           .limit(page_size)
    else:
        cursor = blog_client.find({}) \
                           .skip((page - 1) * page_size) \
                           .limit(page_size)
    
    blogs = []
    async for blog in cursor:
        blog["_id"] = str(blog["_id"])
        blogs.append(Blog(**blog))
    return blogs



async def get_all_blogs(page: int = 1, page_size: int = 10) -> list[Blog]:
    cursor = blog_client.find({}) \
                       .skip((page - 1) * page_size) \
                       .limit(page_size)
    
    blogs = []
    async for blog in cursor:
        blog["_id"] = str(blog["_id"])
        blogs.append(Blog(**blog))
        
    return blogs


async def get_all_unique_tags() -> list[str]:
    cursor = blog_client.find({}, {"tags": 1})
    all_tags = set()
    
    async for blog in cursor:
        if "tags" in blog and blog["tags"]:
            all_tags.update(blog["tags"])
            
    return sorted(list(all_tags))
