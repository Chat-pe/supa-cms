from pydantic import BaseModel
from typing import Optional
from pydantic import RootModel
class DemoBookDto(BaseModel):
    first_name: str
    last_name: str
    email: str
    job_title: str
    company_name: str
    company_size: str
    industry: Optional[str] = None
    country: Optional[str] = None
    phone_number: Optional[str] = None

class UpdateDemoBookDto(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[str] = None
    job_title: Optional[str] = None
    company_name: Optional[str] = None
    company_size: Optional[str] = None
    industry: Optional[str] = None
    country: Optional[str] = None
    phone_number: Optional[str] = None

class DemoBookListResponse(RootModel):
    root: list[DemoBookDto]