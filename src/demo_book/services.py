from datetime import datetime
from src.database import demo_books_client
from .schema import DemoBook
from .dtos import DemoBookDto, UpdateDemoBookDto
from fastapi.encoders import jsonable_encoder

async def create_demo_book(demo_book: DemoBookDto) -> dict:
    demo_book_dict = jsonable_encoder(demo_book)
    demo_book_dict["created_at"] = datetime.now()
    demo_book_dict["updated_at"] = datetime.now()
    
    result = await demo_books_client.demo_books.insert_one(demo_book_dict)
    created_book = await demo_books_client.demo_books.find_one({"_id": result.inserted_id})
    created_book["_id"] = str(created_book["_id"])
    return created_book


async def get_demo_book_by_email(email: str) -> dict:
    demo_book = await demo_books_client.demo_books.find_one({"email": email})
    if demo_book:
        demo_book["_id"] = str(demo_book["_id"])
    return demo_book


async def update_demo_book(email: str, demo_book: UpdateDemoBookDto) -> dict:
    update_data = jsonable_encoder(demo_book, exclude_none=True)
    update_data["updated_at"] = datetime.now()
    
    if update_data:
        await demo_books_client.demo_books.update_one(
            {"email": email},
            {"$set": update_data}
        )
    
    updated_book = await demo_books_client.demo_books.find_one({"email": email})
    if updated_book:
        updated_book["_id"] = str(updated_book["_id"])
    return updated_book


async def delete_demo_book(email: str) -> dict:
    demo_book = await demo_books_client.demo_books.find_one({"email": email})
    if demo_book:
        await demo_books_client.demo_books.delete_one({"email": email})
        demo_book["_id"] = str(demo_book["_id"])
    return demo_book


async def get_all_demo_books(page: int, page_size: int) -> list:
    cursor = demo_books_client.demo_books.find({}).skip((page - 1) * page_size).limit(page_size)
    demo_books = []
    async for book in cursor:
        book["_id"] = str(book["_id"])
        demo_books.append(book)
    return demo_books
