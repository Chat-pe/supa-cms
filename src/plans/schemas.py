from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional, Literal

class CountryCurrencyPrice(BaseModel):
    country: str
    currency: str
    price: float
    variant_link: str




class Plan(BaseModel):
    
    uniquelink: str
    name: str

    id_alias: dict[str, str]
    metadata: dict[str, str | bool]
    checkout_link: str
    description: str
    max_allowed_members: int
    period: int # in days
    plan_level: int
    features: dict # key value pair of feature and boolean value
    default_price: CountryCurrencyPrice
    price: List[CountryCurrencyPrice]

    is_trial: Optional[bool] = False
    is_monthly: Optional[bool] = True
    status: Optional[Literal["active", "inactive"]] = "inactive"
    
    created_at: Optional[datetime] = datetime.now()
    updated_at: Optional[datetime] = datetime.now()
