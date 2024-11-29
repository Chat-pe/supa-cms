from motor.motor_asyncio import AsyncIOMotorClient
from src.config import MONGO_URI


client = AsyncIOMotorClient(MONGO_URI)



#create clients for blog, newsletter and demo_books
blog_client = client.Blogs.blog
newsletter_client = client.Newsletter.newsletter
demo_books_client = client.DemoBooks.demo_books
plans_client = client.Plans.plans
