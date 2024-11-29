
from .app import app
from .demo_book.router import router as demo_book_router
from .blogs.router import router as blog_router
from .plans.router import router as plans_router

@app.get("/status", include_in_schema=False)
async def status() -> dict[str, str]:
    return {"status": "ok", "version": "Test_v.0.0.0"}


app.include_router(demo_book_router, prefix="/demo-books", tags=["demo-books"])
app.include_router(blog_router, prefix="/blogs", tags=["blogs"])
app.include_router(plans_router, prefix="/plans", tags=["plans"])