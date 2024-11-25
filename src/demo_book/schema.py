# have the schema of the demo book
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class DemoBook(BaseModel):
    first_name: str
    last_name: str
    email: str
    job_title: str
    company_name: str
    company_size: str
    industry: Optional[str]
    country: Optional[str]
    phone_number: Optional[str]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
